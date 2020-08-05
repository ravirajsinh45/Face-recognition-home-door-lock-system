import RPi.GPIO as GPIO
import time


def Distance(SIG=15):
    '''
    arguments:
    
    SIG: pin at which ultrasonic sensor is set, by default value is 15
    '''
    GPIO.setmode(GPIO.BCM)
    
    #intialisation in case sensor won't work 
    start = time.time()
    end = time.time()
    
    GPIO.setup(SIG,GPIO.OUT)

    GPIO.output(SIG,GPIO.LOW)

    time.sleep(0.0002)

    GPIO.output(SIG,GPIO.HIGH)
    time.sleep(0.000001)
    GPIO.output(SIG,GPIO.LOW)

    GPIO.setup(SIG,GPIO.IN)

    while GPIO.input(SIG)==0:
        start = time.time()

    while GPIO.input(SIG)==1:
        end = time.time()

    sig_time = end - start

    distance = sig_time / 0.000058
    GPIO.cleanup(SIG)
    
    #print('Object is at {} cm'.format(round(distance),4))
    return distance


if __name__ == '__main__':
    try:
        while True:
            dist = Distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        

