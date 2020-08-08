# Facial-recognition-home-door-lock-system
Made Face recognition door lock with Raspberry Pi and other sensor.  
This repo contains all code require to make your own face recognition door lock system.  

# Raspberry Pi
“The Raspberry Pi is a low cost, credit-card sized computer that plugs into a computer
monitor or TV, and uses a standard keyboard and mouse. It is a capable little
device that enables people of all ages to explore computing, and to learn how to
program in languages like Scratch and Python.”    — Raspberry Pi foundation

* Raspberry Pi is great learning tool.
* You can built many cool project using Pi.

# Prerequisites 
* I assuming that you have little bit of knowledge and work experience with python programming language and raspberry pi as well.
* If you not familiar with pi, i attaching link of some resources which i using.
    * https://www.pyimagesearch.com/ 
    * https://www.youtube.com/watch?v=RpseX2ylEuw
* If you want to know about face Recognition and how it works check below video playlist.  
    * https://www.youtube.com/watch?v=-FfMVnwXrZ0&t=25s

# My Contact Detail
If you have any doubts feel free to ask any quesion at any time:)  
  * LinkedIn:  https://www.linkedin.com/in/ravirajsinh45/  
  * Twitter:   https://twitter.com/Ravirajsinh45  
  * Instagram: https://www.instagram.com/ravirajsinh45/ 


    

# Step by step description of this project

## Overview of the system

* Ultrasonic distance sensor, camera and solenoid lock will connected with Raspberry Pi.
* Ultrasonic sensor measure distance at every second countinuesly, Whenever ultrasonic distance sensor detect object at 150cm or less it turn on camera.
* Whoever person you give access of this system is detected on camera within 20 seconds door will open.
* If within 20 second door won't open camera will turn off and distance sensor will start again measuring distance .....
* Door remains open for only 10 seconds, after that door will lock again.

## Components that I'm using
1. [Raspberry pi 4 model B 2GB Ram](https://www.robocraze.com/raspberry-pi-4-ultimate-kit)   

2. [Pi camera module](https://www.robocraze.com/raspberry-pi-8mp-camera-v2-1080) (You can also use webcam)

3. [3 pin Ultrasonic Distance Sensor](https://www.thingbits.in/products/grove-ultrasonic-distance-sensor)

4. [Solenoid lock](https://www.robocraze.com/12v-dc-lock-electric-solenoid-assembly)

5. Ethernet cable

6. [5V relay module](https://www.robocraze.com/catalog/product/view/id/1660/s/2channel-relay-module-with-optocoupler/)

7. [12V adapter](https://www.robocraze.com/12-volts-1-ampere-adapter)

8. 10 male to male, 10 male to female, 10 female to female

9. Micro HDMI cable (Not necessory unless you have desktop or hdmi compitible tv and you want to connect pi with it.)

[Amazone](https://www.amazon.in/), [Robocraze](https://www.robocraze.com/), and [Thingbits](https://www.thingbits.in/) These website i used to bought components like this. For this project i bought all component from [Robocraze](https://www.robocraze.com/) but you can buy according your location and preferences:)



# Setting up Raspberry pi

If you bought raspberry pi with pre install NOOBs sd card you are ready to go but if have just bought SD card, you have to follow few more steps.
* Download and install [SD card formater](https://www.sdcard.org/downloads/formatter/) on your PC or Laptop and format your sd card.  
* Download [NOOBs](https://www.raspberrypi.org/downloads/noobs/) it easy to install.   
*  Now extract downloaded zip file and go inside extracted folder.
* Copy all files of folder and paste in sd card.

There are several ways to work with pi two of them is here.  
1. Using with TV or desktop
2. Connect Pi with your PC or Laptop using Ethernet cable


    ### 1. Using with TV or desktop
    * If you have HDMI compatible Desktop or tv, USB key board and mouse you connect with each other and  give power supply to pi.
    * You will get screen like this    
    ![](https://github.com/ravirajsinh45/Face-recognition-home-door-lock-system/blob/master/assets/noobs.png)
    * There will be few option for installtion, we only need **Raspbian** to install. select Raspbian and press install it took while to get install.
    * After installtion configure your time zone and reboot the pi and you ready to rock :)

    ### 2. Connect Pi with your PC or Laptop using Ethernet cable
    Update soon ...


## Installation
First of all open terminal(ctrl + alt + t) and run
```
sudo apt-get update && sudo apt-get upgrade -y
```
Install git and cmake by using
```
sudo apt-get install git cmake
```

### 1. OpenCV

For this you have to follow few step so i am attaching Link, this will step by step guide you to all installation require to install [opencv](https://www.pyimagesearch.com/2019/09/16/install-opencv-4-on-raspberry-pi-4-and-raspbian-buster/).

NOTE: IF YOU MAKING VIRTUAL ENVIRONMENT FOR INSTALL OPENCV THAN MAKE SURE YOU INSTALL ALL BELOW PACKAGES IN SAME ENVIRONMENT.
### 2. Face recognition library

Run below command in your terminal, this will take while to install.
```
sudo pip3 install face_recognition
```

### 3. Other libraries and setup
```
sudo pip3 install imutils pypickle
```
Now we have to enable camera on pi for that follow below step
* Open terminal and run
  ```
  raspi-config
  ```
* After that select **Interfacing option** and you will get screen like this  

    ![](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.1nXSVe3RLWhk-cmOi5OxpAHaD3%26pid%3DApi&f=1)

* select camera option and hit enter it will ask you to enable than hit enter.

  
    

# Connecting all sensor with Pi
GPIO Pin Diagram  

![](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.3314R8V6HKbVsmF2ld5tRgHaEQ%26pid%3DApi&f=1)

In Pi there are 40 GPIO pins.

### 1. Camera
![](https://github.com/ravirajsinh45/Face-recognition-home-door-lock-system/blob/master/assets/camera_module.jpeg)  

The camera module is a small circuit board, with a strip of ribbon cable that plugs directly into the Raspberry Pi board. It’s easiest to connect the camera before you plug your Raspberry Pi into any cables.
* Open the camera connector on your Raspberry Pi board which is in between hdmi and audio port, hold the ends between your finger and thumb and gently lift. 
* The plastic parts don’t separate, but they move apart to make a gap. This is where you insert the camera’s cable.
* Hold camera such a way that it facing USB port, after that insert cable in port and press plastic cap.

### 2. Ultrasonic Distance sensor
![](https://github.com/ravirajsinh45/Face-recognition-home-door-lock-system/blob/master/assets/ultrasonic_distance_sensor.jpeg)  
I'm using [3 pin Ultrasonic Distance Sensor](https://www.thingbits.in/products/grove-ultrasonic-distance-sensor). Advantage of using this sensor over [Ultrasonic SR04](https://lastminuteengineers.com/arduino-sr04-ultrasonic-sensor-tutorial/) is you only need 1 signal pin instead of 2 pin(one for trig and other for echo) which save one GPIO pin of Pi. Other advantage is it work on 3.3V and 5V both power while SR04 require 5V.  

NOTE: If you have SR04 sensor it's not problem i will guide as well.

#### How to connect with pi
* Take 3 female to female jumper wire and connect with VCC, GND and SIG on distance sensor. Their is NC pin as well but we don't have to connect with it.
You have to connect 
    * VCC wire with 5V or 3V pin of Pi [I connected with pin which on right side column first pin]
    * GND wire with GND of Pi [I connected with pin which on right side column 3rd pin]
    * SIG wire with any GPIO pin (I connected with GPIO 15 right side column 5th pin)
  ![](https://github.com/ravirajsinh45/Face-recognition-home-door-lock-system/blob/master/assets/ultrasonic_connection.jpeg)  


If you want to check sensor is functioning or not run below code in terminal.  
```
python3 distance_measurement.py
```
Remember I connected ultrasonic sensor on PIN 15, If you want to connect on other pin, change PIN value inside **distance_measurement.py**


### 3. Relay module and solenoid lock

A relay is basically a switch which is operated by an electromagnet. The electromagnet requires a small voltage to get activated which we will give from the Raspberry pi or Arduino and once it is activated, it will pull the contact to make the high voltage circuit.

 <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.3Io6qW4SvbF2RzrGRSR_BQHaFj%26pid%3DApi&f=1" >


The relay module has total of six pins: three on one side and three on other side.On the bottom side, there are three pins which are signal, 5V and ground. We will connect these pins with the Raspberry pi. While on the other side, there are NC (Normally close), COM (Common) and the NO (normally open) which are the output pins of the 5V relay. There, we will connect the output device in our case 12V solenoid lock. So follow below steps  


  *  Take 3 Female to Female jumper wire and connect with bottom pins as shown in image.
      * Connect VCC jumper wire with 5V pin on raspberry pi. [I connected with pin which on right side column second pin]
      * Connect GND jumper wire with any GND pin on raspberry pi. [I connected with last pin of left side column]
      * Connect IN jumper wire with any GPIO pin [I connected with pin 26 second last from left side column]

  ![](https://github.com/ravirajsinh45/Face-recognition-home-door-lock-system/blob/master/assets/relay_module.jpg)

  * Now time for other side of relay module
      * First of take 12V adapter which will have two wire one is Positive(Red wire) and other is Negative(black or blue).
      * Connect Negative(black or blue) wire with NO(normally open) of relay.
      * Connect Positive(Red) wire with positive(Red) wire of solenoid lock.
      * Connect Negative of Solenoid lock with COM of relay.





# Run the program

* First of all connect all sensor with pi as above and turn on the pi.

* open terminal and if you created virtual environment and install all packages in it, activate it first else skip this step.
  ```
  source <whatever your environment name>/bin/activate 
  ```
  Now go to desktop.
  ```
  cd Desktop/
  ```
* After that clone the repo
  ```
  git clone https://github.com/ravirajsinh45/Face-recognition-home-door-lock-system.git
  ```
  and go inside clone repo.
  ```
  cd Face-recognition-home-door-lock-system
  ```
*  There will be one folder named as **dataset**, open it as well. Inside it will have folder names as **Ravirajsinh** with my images:)
* Now make new folder of your name or whoever person you want to recognise and inside it add photos of that person like I added mine.  
* Remember more photo is means more accurate your system.  
NOTE: MAKE SURE PHOTO YOU ADDED IT ONLY HAVE ONE PERSON INSIDE AND THAT FOLDER SHOULD CONTAIN PHOTOS OF SAME PERSON.
* Now once again comeback to terminal and run below code to generate encoding of all images inside **dataset** folder. It will take while so wait or grab cup of coffee:)
   ```
   python3 generating_encoding.py
   ```

* This will generate face_encodings.pickle file which contains encoded value of all photos.
* Now open **final.py** file and go to 75th line of code their will be code like below
    ```
    if match == 'Ravirajsinh': #In Your case whatever your name
                        
        '''
        Here we using solenoid lock to for lock-unlock the door,
        Lock connected with relay module and relay module is set on 26 pin(BCM mode) of Pi.
        '''
        unlock(26)
        time.sleep(10) #Lock will remains open for 10 seconds.
        lock(26)
        GPIO.cleanup(26)
    ```
* Now change 'Ravirajsinh' With your name or whatever person that you want recognize and want to door to open whenever he or she comes.
* (Optional) If you connect relay module on other pin than 26, change it as well.
* Now we have all things ready to run our system. So run below code .....
    ```
    python3 final.py
    ```
* If you done exact things that I tell you above, camera screen pop up on your display and if accesable person detected in camera image, door will unlock. wooooh,Hurrah:)

* If you want to close program hit CTRL+C from your keyboard.

# Thank You:)













