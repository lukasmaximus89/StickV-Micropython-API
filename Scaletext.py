import sensor
import lcd
lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_hmirror(1)
sensor.set_vflip(1)
sensor.run(1)
while 1:
    img = sensor.snapshot()
    img.draw_string(30,50, "Hello", scale=8)
    lcd.display(img)
