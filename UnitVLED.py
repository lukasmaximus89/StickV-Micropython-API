import time
from modules import ws2812

a = class_ws2812 = ws2812(8,1)

def RGB_LED():
    a = class_ws2812.set_led(0,(0,0,255))
    a = class_ws2812.display()
    time.sleep(0.5)
    a = class_ws2812.set_led(0,(0,0,0))
    a = class_ws2812.display()

while(True):
    RGB_LED()

