import face_recognition
import imutils
import pickle
import time
import cv2
import os


KNOWN_FACES_DIR = 'dataset'

print('Loading known faces...')
known_faces = []
known_names = []

# We oranize known faces as subfolders of KNOWN_FACES_DIR
# Each subfolder's name becomes our label (name)
for name in os.listdir(KNOWN_FACES_DIR):

    # Next we load every file of faces of known person
    for filename in os.listdir(f'{KNOWN_FACES_DIR}/{name}'):
        print(f'Processing image of: {name}')
        # Load an image
        image = face_recognition.load_image_file(f'{KNOWN_FACES_DIR}/{name}/{filename}')

        # Get 128-dimension face encoding
        # Always returns a list of found faces, for this purpose we take first face only (assuming one face per image as you can't be twice on one image)
        try:
            encoding = face_recognition.face_encodings(image)[0]
        except IndexError:
            continue
        # Append encodings and name
        known_faces.append(encoding)
        known_names.append(name)



print("[INFO] serializing encodings...")
data =[known_faces, known_names]
f = open('face_encodings.pickle', "wb")
f.write(pickle.dumps(data))
f.close()


