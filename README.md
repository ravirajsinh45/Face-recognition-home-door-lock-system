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

# Assumption 
* I assuming that you have little bit of knowledge and work experience with raspberry pi.
* If you not familiar with pi, i attaching link of some resources which i using.
    * https://www.pyimagesearch.com/ 
    * https://www.youtube.com/watch?v=RpseX2ylEuw

If you have any doubts feel free to ask any quesion at any time:)  
  * LinkedIn:  https://www.linkedin.com/in/ravirajsinh45/  
  * Twitter:   https://twitter.com/Ravirajsinh45  
  * Instagram: https://www.instagram.com/ravirajsinh45/ 


    

# Step by step description of this project

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
    ![](https://www.raspberrypi.org/documentation/installation/images/noobs.png)
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
After that select **Interfacing option** and you will get screen like this  

![](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.1nXSVe3RLWhk-cmOi5OxpAHaD3%26pid%3DApi&f=1)

select camera option and hit enter it will ask you to enable than hit enter.

  
    

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

### 2. Ultrasonic sensor

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

### 3. Relay module and solenoid lock















