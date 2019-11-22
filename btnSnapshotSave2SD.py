import lcd
import sensor
import image
import time

#ディスプレイ初期化
lcd.init()
lcd.rotation(2)
#イメージセンサー初期化
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
#sensor.skip_frames(time = 2000)

#初期設定
from Maix import GPIO
from fpioa_manager import *
fm.register(board_info.BUTTON_A, fm.fpioa.GPIO1)
but_a=GPIO(GPIO.GPIO1, GPIO.IN, GPIO.PULL_UP)
path = "/sd/image.jpg"

while True:
    img = sensor.snapshot()
    lcd.display(img)
    #Aボタンを押したらSDカードに保存
    if but_a.value() == 0:
        img = sensor.snapshot()
        sensor.run(0) #電圧降下対策
        print("save image")
        time.sleep(1) #電圧降下対策
        img.save(path)
        time.sleep(1)
        sensor.run(1)
