from machine import Pin, I2C
from time import sleep
from dht import DHT22
from ssd1306 import SSD1306_I2C


# Initialising GPIO, DHT22, and the display.
dht22_sensor = DHT22(Pin(2, Pin.IN, Pin.PULL_UP))
i2c=I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 32, i2c)
oled.contrast(128)
oled.poweron()

def displayTest():
    """
    Checks that the display is responding.
    """
    try:
        i2c=I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
        if len(i2c.scan()) == 0:
            print("No I2C device found in board pins 1, 2:  check connection.")
            raise AssertionError
    except:
        raise AssertionError

def tempTest():
    """
    Checks that the DHT22 temperature sensor is responding.
    """
    try:
        dht22_sensor.measure()
    except:
        print("Temperature sensor not responding, check connection.")
        raise AssertionError
    
    
""""
The tests below are run sequentially, and lets you know which part failed.
Note that if the display fails, it needs to be fixed before the temperature
sensor can be tested. This is intended to be a quick test each run.
Testing each component individually is recommended.
"""
display, temp = False, False
try:
    displayTest()
    display = True
    tempTest()
    temp = True
    #oled.fill(0)
    #oled.text("Tests Passed", 0, 0)
    #oled.show()
    #print("Tests Passed")
except:
    print("Tests failed. Display: {}, Temp: {}".format(display,temp))
    if display == True:
        oled.fill(0)
        oled.text("Temperature", 0, 0)
        oled.text("sensor failed",0,8)
        oled.text("Check connections",0,16)
        oled.show()
