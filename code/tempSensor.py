from machine import Pin
from time import sleep
from dht import DHT22
# Initialising GPIO und DHT22
dht22_sensor = DHT22(Pin(5, Pin.IN, Pin.PULL_UP))

def tempMeasure():
    dht22_sensor.measure()
    temp = dht22_sensor.temperature()
    humi = dht22_sensor.humidity()
    return temp, humi

def tempLoop():
    i=0
    while True:
        sleep(2)
        i+=1
        temp, humi = tempMeasure()
        print('Reading {}, Temperature: {:0.1f}C, Humidity: {:0.1f}%'.format(i, temp, humi))


#Uncomment the below to get temperature values.
        
#tempLoop()
