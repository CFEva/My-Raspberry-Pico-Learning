#引用machine和utime库
import machine  
import utime

#设置led变量（若使用pico 将"LED"改为25）
led=machine.Pin("LED",machine.Pin.OUT)
while True:
    #进行循环，以一秒为周期重复led的开与关
    led.on()
    utime.sleep(1)
    led.off()
    utime.sleep(1)
