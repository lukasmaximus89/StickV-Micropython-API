import time
from fpioa_manager import *
from Maix import *

fm.register(board_info.LED_B, fm.fpioa.GPIOHS8)
ledB = GPIO(GPIO.GPIOHS8, GPIO.OUT) 

while(True):
    time.sleep_ms(1000)
    ledB.value(1)
    time.sleep_ms(1000)
    ledB.value(0)
        
