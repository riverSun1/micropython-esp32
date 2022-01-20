import machine
from machine import Pin

# ------------------------------------------------------------------------------
led = Pin (2, Pin.OUT)
led1 = Pin (19, Pin.OUT)
led2 = Pin (23, Pin.OUT)

interruptCounter1 = 0
interruptCounter2 = 0
 
timer1 = machine.Timer(0)  
timer2 = machine.Timer(1)  
 
def handleInterrupt1(timer1): #꼭 timer1을 써야함
  global interruptCounter1
  interruptCounter1 = interruptCounter1+1
  led1.value(not led1.value())
  print("Interrupt has occurred1: " + str(interruptCounter1))
 
timer1.init(period=500, mode=machine.Timer.PERIODIC, callback=handleInterrupt1)

def handleInterrupt2(timer2): #꼭 timer2를 써야함
  global interruptCounter2
  interruptCounter2 = interruptCounter2+1
  led2.value(not led2.value())
  print("Interrupt has occurred2: " + str(interruptCounter2))
 
timer2.init(period=250, mode=machine.Timer.PERIODIC, callback=handleInterrupt2)

while True:
    pass
