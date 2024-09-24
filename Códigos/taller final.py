from machine import Pin, PWM, ADC, time_pulse_us
import time

class motor:
    def __init__(self, pin1, pin2, pwm, invertir):
        if invertir:
            self.pinA = Pin(pin2, Pin.OUT)
            self.pinB = Pin(pin1, Pin.OUT)
        else:
            self.pinA = Pin(pin1, Pin.OUT)
            self.pinB = Pin(pin2, Pin.OUT)
        self.PWM = PWM(Pin(pwm, Pin.OUT), freq = 1000)
    
    def adelante2(self, duty):
        self.pinA.on()
        self.pinB.off()
        self.PWM.duty(duty)
        
    def atras2(self, duty):
        self.pinA.off()
        self.pinB.on()
        self.PWM.duty(duty)
    
    def adelante(self):
        self.pinA.on()
        self.pinB.off()
        self.PWM.duty(1023)
    def atras(self):
        self.pinA.off()
        self.pinB.on()
        self.PWM.duty(1023)
    def parar(self):
        self.pinA.off()
        self.pinB.off()
        self.PWM.duty(0)          

class flame:
    def __init__(self, pin):
        self.sensor = Pin(pin, Pin.IN)
    def detectar_fuego(self):
        return True if self.sensor.value() == 0 else False

motor1 = motor(14, 12, 27, False)
motor2 = motor(33, 26, 25, False)

motor1.parar()
motor2.parar()

# Primer sensor
flame1 = flame(2)

# Segundo sensor
flame2 = flame(0)

# Tercer sensor
flame3 = flame(4)

# Sensor ultrasonido
trigger = Pin(18, Pin.OUT)
echo = Pin(5, Pin.IN)

# Bomba
pump = Pin(32, Pin.OUT)

def moverse_tiempo (distancia, reversa):
    tiempo = distancia/0.27
    inicio = time.time()
    while time.time() - inicio <= tiempo:
        if not reversa:
            motor1.adelante()
            motor2.adelante()
        else:
            motor1.atras()
            motor2.atras()

def rotar_derecha ():
    motor1.adelante()
    motor2.atras()

def rotar_izquierda ():
    motor1.atras()
    motor2.adelante()
    
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

while True:
    if flame2.detectar_fuego():
        motor1.parar()
        motor2.parar()
        time.sleep(2)
        
        if medir_distancia() > 10:
            motor1.adelante2(600)
            motor2.adelante2(600)
        elif medir_distancia() < 9:
            motor1.atras2(600)
            motor2.atras2(600)
        else:
            while flame2.detectar_fuego():
                # Activar la bomba y el servo
                pump.value(1)
                time.sleep(0.5)
            pump.value(0)
        
    elif flame1.detectar_fuego():
        inicio = time.time()
        while not flame2.detectar_fuego() and time.time() - inicio <= 5:
            rotar_derecha()
            
    elif flame3.detectar_fuego():
        inicio = time.time()
        while not flame2.detectar_fuego() and time.time() - inicio <= 5:
            rotar_izquierda()
            
    else:
        motor1.parar()
        motor2.parar()
        print("no hay fuego")
    time.sleep(0.2)   

           
  
motor1.parar()
motor2.parar()