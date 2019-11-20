import time
from fpioa_manager import *
from Maix import *

fm.register(board_info.LED_W, fm.fpioa.GPIO7)
fm.register(board_info.LED_R, fm.fpioa.GPIO6)
fm.register(board_info.LED_G, fm.fpioa.GPIOHS9)
fm.register(board_info.LED_B, fm.fpioa.GPIOHS8)

ledW = GPIO(GPIO.GPIO7, GPIO.OUT) 
ledR = GPIO(GPIO.GPIO6, GPIO.OUT) 
ledG = GPIO(GPIO.GPIOHS9, GPIO.OUT) 
ledB = GPIO(GPIO.GPIOHS8, GPIO.OUT) 

while(True):
    time.sleep_ms(1000)
    ledB.value(1)
    time.sleep_ms(1000)
    ledB.value(0)
    ledR.value(1)
    time.sleep_ms(1000)
    ledR.value(0)
    ledG.value(1)     
    time.sleep_ms(1000)
    ledG.value(0) 
    ledW.value(1)
