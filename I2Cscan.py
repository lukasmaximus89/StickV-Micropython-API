from machine import I2C
import lcd
from fpioa_manager import fm

lcd.init()
lcd.clear()
fm.register(35, fm.fpioa.I2C2_SDA, force=True)
fm.register(34, fm.fpioa.I2C2_SCLK, force=True)
i2cport = I2C(I2C.I2C2)
i2cport.scan()
lcd.draw_string(0,0,str(i2cport.scan()), lcd.WHITE)

