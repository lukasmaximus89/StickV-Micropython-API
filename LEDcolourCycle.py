import utime
from Maix import GPIO
from fpioa_manager import *
import sys
import random

fm.register(board_info.LED_W, fm.fpioa.GPIO3)
fm.register(board_info.LED_R, fm.fpioa.GPIO4)
fm.register(board_info.LED_G, fm.fpioa.GPIO5)
fm.register(board_info.LED_B, fm.fpioa.GPIO6)

led_w = GPIO(GPIO.GPIO3, GPIO.OUT)
led_r = GPIO(GPIO.GPIO4, GPIO.OUT)
led_g = GPIO(GPIO.GPIO5, GPIO.OUT)
led_b = GPIO(GPIO.GPIO6, GPIO.OUT)

dic = []
dic.append(led_w)
dic.append(led_r)
dic.append(led_g)
dic.append(led_b)


def color():
    for i in range(4):
	dic[i%4].value(0)
	utime.sleep(1)
	dic[(i+1)%4].value(0)
	utime.sleep(1)
	dic[i%4].value(1)
	

def shufful():
    sh = []
    for i in range(4):
	sh.append(random.randrange(0, 4))
    while sh[1]==sh[0]:
	sh[1] = random.randrange(0, 4)
    while sh[2]==sh[0] or sh[2]==sh[1]:
	sh[2] = random.randrange(0, 4)
    while sh[3]==sh[0] or sh[3]==sh[1] or sh[3]==sh[2]:
	sh[3] = random.randrange(0, 4)
    return sh

def sort_array(ary):
    new_dic = []
    for i in ary:
	if i == 0:
	    new_dic.append(led_w)
	elif i == 1:
	    new_dic.append(led_r)
	elif i == 2:
	    new_dic.append(led_g)
	else:
	    new_dic.append(led_b)
    return new_dic
	   

try:
    while True:
	color()
	a = shufful()
	print(a)
	dic = sort_array(a)
	print(dic)
	
except:
    sys.exit()
