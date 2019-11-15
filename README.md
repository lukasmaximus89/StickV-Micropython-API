# StickV-Micropython-API

**Introduction**

An API of Micropython functions for the StickV

## File System
import os

os.listdir() //to list sub directory or alternate location, insert into brackets with "" e.g. "/sd"

os.chdir() change current working director

os.mkdir() creat a new directory

## Clear LCD
import lcd
lcd.clear() //default is black, hex values can be entered to fill the screen with a different color

## Display Text 
//enter x and y coordinate followed by string/variable and predefined color constant or hex value
lcd.draw_string(x,y,”text”,lcd.WHITE)

## Display Image
import image, lcd
img = image.Image("/sd/startup.jpg")
lcd.display(img)

## Initialise button

from fpioa_manager import *
from Maix import *

fm.register(board_info.BUTTON_A, fm.fpioa.GPIO1)
btnA = GPIO(GPIO.GPIO1, GPIO.IN, GPIO.PULL_UP)

fm.register(board_info.BUTTON_B, fm.fpioa.GPIO2)
but_b = GPIO(GPIO.GPIO2, GPIO.IN, GPIO.PULL_UP)

## Initialise RGB-LED

**-BLUE-**
fm.register(board_info.LED_B, fm.fpioa.GPIOHS8)
ledB = GPIO(GPIO.GPIOHS8, GPIO.OUT) 

## Live stream:
import sensor
import image
import lcd

lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)
while True:
    img=sensor.snapshot()
    lcd.display(img)

