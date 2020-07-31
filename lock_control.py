import RPi.GPIO as GPIO
import time


def unlock(pin=26):
    '''
    pin: pin which you attach on your pi with solenoid lock, default is 26
    '''
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,True)
    

def lock(pin=26):
    '''
    pin: pin which you attach on your pi with solenoid lock, default is 26
    '''
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,False)
    

if __name__ == '__main__':
    unlock()
    time.sleep(2)
    lock()
    GPIO.cleanup(26)

