import network
import time

#ssid=wifi名称 password=wifi密码
ssid = 'wifi'
password = '12345678'

#设置连接wifi的参数
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

#等待连接
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)

#连接失败的处理
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    #若连接成功，输出"connected和wifi连接信息"
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )
    led = machine.Pin("LED", machine.Pin.OUT)
    led.on()


