
from imutils.video import VideoStream
from imutils.video import FPS
import face_recognition
import imutils
import pickle
import time
import cv2
import os
from lock_control import unlock, lock
from distance_measurement import Distance
import RPi.GPIO as GPIO
'''
dist = Distance()
print('distance {}'.format(dist))
if dist<10:
    unlock()
    
'''

TOLERANCE = 0.4
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = 'hog'

# Returns (R, G, B) from name
def name_to_color(name):
    # Take 3 first letters, tolower()
    # lowercased character ord() value rage is 97 to 122, substract 97, multiply by 8
    color = [(ord(c.lower())-97)*8 for c in name[:3]]
    return color

vs = VideoStream(usePiCamera=True).start()
time.sleep(1)
print("[INFO] loading encodings + face detector...")
known_faces, known_names= pickle.loads(open('face_encodings.pickle', "rb").read())
print('Processing...')


while True:
    try:
        dist = Distance()
    except KeyboardInterrupt:
        break
    print('Distance is {}'.format(dist))
    if dist < 150:
        tic = time.time()      
        while True:
            
            # Load image
            image  = vs.read()
            image = imutils.resize(image, width=416)
            # This time we first grab face locations - we'll need them to draw boxes

            locations = face_recognition.face_locations(image, model=MODEL)

            # Now since we know loctions, we can pass them to face_encodings as second argument
            # Without that it will search for faces once again slowing down whole process
            encodings = face_recognition.face_encodings(image, locations)

            # We passed our image through face_locations and face_encodings, so we can modify it
            # First we need to convert it from RGB to BGR as we are going to work with cv2
            #image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # But this time we assume that there might be more faces in an image - we can find faces of dirrerent people
            print(f', found {len(encodings)} face(s)')
            for face_encoding, face_location in zip(encodings, locations):

                # We use compare_faces (but might use face_distance as well)
                # Returns array of True/False values in order of passed known_faces
                results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)

                # Since order is being preserved, we check if any face was found then grab index
                # then label (name) of first matching known face withing a tolerance
                match = None
                if True in results:  # If at least one is true, get a name of first of found labels
                    match = known_names[results.index(True)]
                    
                    if match == 'Ravirajsinh': #In Your case whatever your name
                        unlock()
                        time.sleep(10)
                        lock()
                        GPIO.cleanup(26)
                        
                    
                    # Each location contains positions in order: top, right, bottom, left
                    top_left = (face_location[3], face_location[0])
                    bottom_right = (face_location[1], face_location[2])

                    # Get color by name using our fancy function
                    color = name_to_color(match)

                    # Paint frame
                    cv2.rectangle(image, top_left, bottom_right, color, FRAME_THICKNESS)

                    # Now we need smaller, filled grame below for a name
                    # This time we use bottom in both corners - to start from bottom and move 50 pixels down
                    top_left = (face_location[3], face_location[2])
                    bottom_right = (face_location[1], face_location[2] + 22)

                    # Paint frame
                    cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)

                    # Wite a name
                    cv2.putText(image, match, (face_location[3] + 10, face_location[2] + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), FONT_THICKNESS)
                           
           
            tok = time.time() 
            # Show image
            
            cv2.imshow('webcam', image)
            if cv2.waitKey(1) == ord('q'):
                cv2.destroyAllWindows()
                break
            
            
            
            if tok-tic>20:
                #cv2.destroyAllWindows()
                break
        
        
