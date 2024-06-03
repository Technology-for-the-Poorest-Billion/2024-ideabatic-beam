from machine import Pin
from time import time, sleep

def buzz(pin, time: float):
    """
    Buzzes the buzzer for the labelled time
    """
    pin.toggle()
    sleep(time)
    pin.toggle()


#Uncomment the below to test the buzzer.

#buzzer = Pin(14, Pin.OUT, Pin.PULL_DOWN)
#buzz(buzzer, 0.5)
#buzz.toggle