#模拟交通信号灯
import machine
import utime
#外接红led
led_red=machine.Pin(15,machine.Pin.OUT)
#外接黄led
led_yellow=machine.Pin(14,machine.Pin.OUT)
#外接绿led
led_green=machine.Pin(13,machine.Pin.OUT)

while True:
    led_red.value(1)
    #红灯60s
    utime.sleep(60)
    led_red.value(0)
    led_green.value(1)
    #绿灯40s
    utime.sleep(40)
    led_green.value(0)
    led_yellow.value(1)
    #黄灯3s
    utime.sleep(3)
    led_yellow.value(0)
    #循环
