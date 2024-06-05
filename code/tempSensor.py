from machine import Pin
from time import sleep
from dht import DHT22
# Initialising GPIO und DHT22
dht22_sensor = DHT22(Pin(5, Pin.IN, Pin.PULL_UP))

def tempMeasure():
    """
    Communicates with DHT22 chip and returns the temperature
    """
    dht22_sensor.measure()
    temp = dht22_sensor.temperature()
    return temp

def tempLoop():
    """
    Simple loop for testing; returns the temperature and humidity readings from the DHT22 chip.
    """
    i=0
    while True:
        sleep(2)
        i+=1
        dht22_sensor.measure()
        temp, humi = dht22_sensor.temperature(), dht22_sensor.humidity()
        print('Reading {}, Temperature: {:0.1f}C, Humidity: {:0.1f}%'.format(i, temp, humi))


#Uncomment the below to get temperature values.
        
#tempLoop()
