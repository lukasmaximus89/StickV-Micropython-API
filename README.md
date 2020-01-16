# StickV-Micropython-API

**Introduction**

An API of Micropython functions for the StickV

## File System
import os

os.listdir() //to list sub directory or alternate location, insert into brackets with "" e.g. "/sd"

os.chdir() change current working director

os.mkdir() creat a new directory

## LCD

**Clear LCD**

import lcd

lcd.clear(0xffffff) //default is black, hex values can be entered to fill the screen with a different color

**Display Text** 
//enter x and y coordinate followed by string/variable and 2 predefined color constant or hex values, 
1 for text color and one for text background color

lcd.draw_string(x,y,”text”,lcd.WHITE, lcd.RED)

**Display Image**
import image, lcd

img = image.Image("/sd/startup.jpg")
lcd.display(img)

**Draw Rectangle**
import image, lcd, sensor

img = sensor.snapshot()
disp_img = img.copy()

// enter x, y ,width, height, color (color = (255,255,255) or (lcd.WHITE) or (0xffffff)), thickness = 1
disp_img.draw_rectangle(100, 150, 15, 15, lcd.WHITE, thickness = 1)

**Draw Circle**
// enter x, y , radius, color (color = (255,255,255) or (lcd.WHITE) or (0xffffff)), thickness = 1
disp_img.draw_circle(80, 150, 15, color = (255,0,0), thickness = 1)

**Draw Ellipse**
// enter x, y ,width, height, color (color = (255,255,255) or (lcd.WHITE) or (0xffffff)), thickness = 1
disp_img.draw_ellipse(80, 150, 15, 20, color = (255,0,0), thickness = 1)

**Draw Line**
//enter origin and ending points  x1, y1 ,x2, y2, color (color = (255,255,255) or (lcd.WHITE) or (0xffffff)), thickness = 1
disp_img.draw_line(50,50,200,100, 0xffffff, thickness = 5)

**Draw Arrow**
//enter origin and ending points  x1, y1 ,x2, y2, color (color = (255,255,255) or (lcd.WHITE) or (0xffffff)), thickness = 1
disp_img.draw_arrow(50,50,200,100, 0x00ffff, thickness = 5)

**Draw Cross**
//enter x, y , color (color = (255,255,255) or (lcd.WHITE) or (0xffffff)), thickness = 1
disp_img.draw_cross(80, 150, color = (255,0,0), thickness = 5)

## Initialise button

from fpioa_manager import *
from Maix import *

fm.register(board_info.BUTTON_A, fm.fpioa.GPIO1)
btnA = GPIO(GPIO.GPIO1, GPIO.IN, GPIO.PULL_UP)

fm.register(board_info.BUTTON_B, fm.fpioa.GPIO2)
but_b = GPIO(GPIO.GPIO2, GPIO.IN, GPIO.PULL_UP)

## Initialise RGB-LED

from fpioa_manager import *
from Maix import *

**-White-**
fm.register(board_info.LED_W, fm.fpioa.GPIO7)
ledW = GPIO(GPIO.GPIO7, GPIO.OUT) 
ledW.value(1)

**-BLUE-**
fm.register(board_info.LED_B, fm.fpioa.GPIOHS8)
ledB = GPIO(GPIO.GPIOHS8, GPIO.OUT) 
ledB.value(1)

**-UnitV LED-**

The RGB LED of UnitV is on gpio8

a = class_ws2812 = ws2812(8,1)

def RGB_LED():
    a = class_ws2812.set_led(0,(0,0,255)) //enter RGB values here
    a = class_ws2812.display()
    time.sleep(0.5)
    a = class_ws2812.set_led(0,(0,0,0))
    a = class_ws2812.display()

while(True):
    RGB_LED()


## I2C

from machine import I2C

i2c = I2C(I2C.I2C0, freq=100000, scl=28, sda=29)
devices = i2c.scan()
print(devices)

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

