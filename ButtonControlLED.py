import sensor, image, time, lcd, fpioa_manager
from fpioa_manager import *
from Maix import *

lcd.init()

fm.register(board_info.BUTTON_A, fm.fpioa.GPIO1)
btnA = GPIO(GPIO.GPIO1, GPIO.IN, GPIO.PULL_UP)
fm.register(board_info.LED_B, fm.fpioa.GPIOHS8)
ledB = GPIO(GPIO.GPIOHS8, GPIO.OUT) 

while(True):
    if(btnA.value() == 1):
        ledB.value(1)
    else:
        ledB.value(0)
        
