from machine import Pin
import time

flame1 = Pin(2, Pin.IN)
flame2 = Pin(0, Pin.IN)
flame3 = Pin(4, Pin.IN)

def detectar_fuego(flame):
    if flame == 1:
        return True if flame1.value() == 0 else False
    elif flame == 2:
        return True if flame2.value() == 0 else False
    elif flame == 3:
        return True if flame3.value() == 0 else False
    else:
        return False

try:
    while 1:
        if detectar_fuego(1):
            print("Fuego en primero")
        elif detectar_fuego(2):
            print("Fuego en segundo")
        elif detectar_fuego(3):
            print("Fuego en tercero")
        else:
            print("No hay fuego")
        time.sleep(0.5)
        
except KeyboardInterrupt:
    print("Cerrando...")