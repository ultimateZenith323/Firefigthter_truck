from machine import Pin, time_pulse_us
import time

trigger = Pin(18, Pin.OUT)
echo = Pin(5, Pin.IN)

def medir_distancia():
    distance = None
    while distance == None:
        trigger.off()
        time.sleep_us(2)
        trigger.on()
        time.sleep_us(10)
        trigger.off()
        
        duration = time_pulse_us(echo, 1, 30000)
        if duration < 0:
            distance = None
        else:
            distance = (duration /2) / 29.1
    return distance

try:
    while 1:
        print(medir_distancia(), "cm")
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Cerrando...")