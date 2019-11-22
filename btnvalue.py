import lcd
from fpioa_manager import fm
from Maix import *

lcd.init()
lcd.clear()
fm.register(36, fm.fpioa.GPIO4)
btnA = GPIO(GPIO.GPIO4, GPIO.IN, GPIO.PULL_UP)

while True:
    lcd.draw_string(0,0,str(btnA.value()), lcd.WHITE)

