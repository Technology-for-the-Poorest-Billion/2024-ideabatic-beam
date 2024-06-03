from time import sleep, time
from machine import Pin
from oledDisplay import *
import test
from tempSensor import tempMeasure
from buzzer import buzz
from constants import updateJson, dumpJson


"""
This is a variant of main.py used for testing the functions.

Differences:
Uses a tdelta/polling rate of 1 second, as opposed to 5 minutes. Allows for quick testing of buzzer.
Greatly accelerates heat loss, by a factor of 3600, to model 1 hour passing every second.
Upon bootup, will always choose revertQ to be half of the cool life; around 54 hours at 21.5C.
"""


class SoftSwitch():
    """Switch Class
 
    Class for defining a switch. Uses internal state to debounce switch in
    software. To use switch, check the "new_value_available" member and the
    "value" member from the application.
    
    Addition by Romeo: able to detect double clicks, if this doesn't work try
    clicking the button down, then clicking it again quickly, or adjusting the
    sensitivity in self.sensitivity.
    """
    def __init__(self, pin, constants: dict, checks=3, check_period=100):
        self.pin = pin
        self.pin.irq(handler=self._switch_change,
                     trigger= machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING)
 
        self.debounce_timer = machine.Timer(-1)
        self.new_value_available = False
        self.value = pin.value
        self.prev_value = None
        self.debounce_checks = 0
        self.checks = checks
        self.check_period = check_period
        self.sensitivity = 0.75
        self.reverted = False
        self.timeFinished = False
        self.previousTime = False
        
    def endTimer(self):
        self.timeFinished = True
 
    def _switch_change(self, pin):
        self.value = pin.value
        # Start timer to check for debounce
        self.debounce_checks = 0
        self._start_debounce_timer()
 
        # Disable IRQs for GPIO pin while debouncing
        self.pin.irq(trigger=0)
 
    def _start_debounce_timer(self):
        self.debounce_timer.init(period=self.check_period, mode=machine.Timer.ONE_SHOT,
                                 callback=self._check_debounce)
 
    def _check_debounce(self, _):
        new_value = self.pin.value
 
        if new_value == self.value:
            self.debounce_checks += 1
 
            if self.debounce_checks == self.checks:
                # Values are the same, debouncing done
 
                # Check if this is actually a new value for the application
                if self.prev_value != self.value:
                    self.new_value_available = True
                    self.prev_value = self.value
                
                if self.prev_value == None:
                    started = True
                    
                    
                self.currentTime = time()
                if not self.previousTime:
                    self.previousTime = self.currentTime
                dummyQ = False
                if self.currentTime - self.previousTime < self.sensitivity:
                    print("Double click detected")
                    if self.timeFinished:
                        dummyQ = constants["Qtotal"]
                    else:
                        if self.reverted == False:
                            self.reverted = True
                            print("Reverting Q to", constants["revertQ"])
                            dummyQ = max(0, constants["revertQ"])
                            displayStrings("Reverting to previous Q", None)
                            sleep(1)
                        else:
                            print("Already reverted Q")
                if dummyQ:     
                    global Qleft
                    Qleft = dummyQ
                self.previousTime = self.currentTime

 
                # Re-enable the Switch IRQ to get the next change
                self.pin.irq(handler=self._switch_change,
                             trigger = machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING)
            else:
                # Start the timer over to make sure debounce value stays the same
                self._start_debounce_timer()
        else:
            # Values are not the same, update value we're checking for and
            # delay again
            self.debounce_checks = 0
            self.value = new_value
            self._start_debounce_timer()

#initialise extra components
buzzer = Pin(14, Pin.OUT, Pin.PULL_DOWN) # Buzzer is connected between GPIO pin 14 (board pin 19), and ground. Polarity does matter
bottomButton = Pin(15, Pin.IN, Pin.PULL_UP) # Bottom button is connected between GPIO pin 15 (board pin 20) and ground)
doorSwitch = Pin(16, Pin.IN, Pin.PULL_UP) # Door switch is connected between GPIO pin 16 (board pin 21), and ground
endBuzz = False


constants = updateJson('constants.json') # Import all the relevant constants
Qleft = constants["Qtotal"] # Initialises the heat energy


constants["tdelta"] = 1 # 1 second polling rate
constants["revertQ"] = 434200 # Half of the original Q
# ^ used for testing.


def wait_for_start(x):
    """
    An interrupt raised at the start, caused by the button at the bottom of the module.
    This commences the rest of the code.
    """
    bottomButton.irq(trigger=0) # Disable the interrupt to prevent further recursions
    global started
    started = True
    return

try:
    bottomButton.irq(trigger=Pin.IRQ_RISING, handler=wait_for_start) # Set the interrupt to the bottom button
    print("Waiting to start; push the bottom button or insert the module to start the timer")
    # Waits for the button (at the bottom of the module) to be pushed to start the programme
    started = False
    waitForStart()
    while started is False:
        sleep(1)
        continue
    print("starting")
    bottomButton = SoftSwitch(Pin(15, machine.Pin.IN, machine.Pin.PULL_UP), constants) # THIS REQUIRES A TECHNICAL PRESS, PUSH THE BUTTON THEN PUSH AGAIN IN QUICK SUCCESSION, OR A QUICK TRIPLE CLICK
    count = 0 # A counter for the number of loops the door has been left open
    lastTime = time()
    while True:
        timeDiff = (time() - lastTime) # Used to calculate the time difference over which heat was lost
        temp, humi = tempMeasure()
        heatLossRate = (temp) / constants["Rth"] # (W), note the temp is actually a temperature difference, but since the ice pack core is 0C, the temperature in Celcius alone works
        QLoss = heatLossRate * timeDiff * 3600 # Heat energy, J, lost to surroundings, with scaling factor to accommodate testing
        Qleft -= QLoss #Calculate remaining Q
        if Qleft <=0:
            bottomButton.endTimer()
            if endBuzz == False:
                buzz(buzzer, 2)
                endBuzz = True
        timeRemaining = Qleft / (heatLossRate * (60*60)) # in hours
        print(timeRemaining) # For testing, note that at 1s intervals, approx time loss in hrs is 0.00028 (at constant T)
        displayTime(timeRemaining, False)                                                                         
        lastTime = time()
        currentSwitch = doorSwitch.value()
        if currentSwitch == 1: # Checks if the door is open. Waits another iteration: if the door is still open, buzz
            count+=1
            if count >=2:
                #count = 0
                buzz(buzzer, 1)
        else:
            count = 0
        sleep(constants["tdelta"]) # Polling rate of tdelta, default 5 mins
    
except:
    print("Error raised somewhere / KBDInterrupt")
    turnoff()
    constants["revertQ"] = Qleft
    constants["revertTime"] = time()
    dumpJson("constants.json", constants)

    







