from machine import Pin, PWM
import time

pinA = Pin(14, Pin.OUT)
pinB = Pin(12, Pin.OUT)
pinPWM = PWM(Pin(27, Pin.OUT), freq = 1000)

pinA2 = Pin(33, Pin.OUT)
pinB2 = Pin(26, Pin.OUT)
pinPWM2 = PWM(Pin(25, Pin.OUT), freq = 1000)

def adelante():
    pinA.on()
    pinB.off()
    
    pinA2.on()
    pinB2.off()
    
    pinPWM.duty(1023)
    pinPWM2.duty(1023)
    
def atras():
    pinA.off()
    pinB.on()
    
    pinA2.off()
    pinB2.on()
    
    pinPWM.duty(1023)
    pinPWM2.duty(1023)
    
def parar():
    pinA.off()
    pinB.off()
    
    pinA2.off()
    pinB2.off()
    
    pinPWM.duty(0)
    pinPWM2.duty(0)
    
def rotar_derecha():
    pinA.on()
    pinB.off()
    
    pinA2.off()
    pinB2.on()
    
    pinPWM.duty(1023)
    pinPWM2.duty(1023)
    
def rotar_izquierda():
    pinA.off()
    pinB.on()
    
    pinA2.on()
    pinB2.off()
    
    pinPWM.duty(1023)
    pinPWM2.duty(1023)

try:
    while 1:
        adelante()
        time.sleep(2)
        atras()
        time.sleep(2)
except KeyboardInterrupt:
    parar()
    print("Cerrando...")