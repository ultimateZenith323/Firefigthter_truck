from machine import Pin
import time

bomba = Pin(32, Pin.OUT)

try:
    while 1:
        bomba.value(1)
        time.sleep(2)
        bomba.value(0)
        time.sleep(2)
except KeyboardInterrupt:
    print("Cerrando...")