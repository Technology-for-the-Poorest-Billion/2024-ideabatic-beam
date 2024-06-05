from time import sleep, time
from machine import Pin
from oledDisplay import *
import test
from tempSensor import tempMeasure
from buzzer import buzz
from constants import updateJson, dumpJson

class SoftSwitch():
    """Switch Class
 
    Class for defining a switch. Uses internal state to debounce switch in
    software. To use switch, check the "new_value_available" member and the
    "value" member from the application.
    
    Addition by Romeo: able to detect double clicks, if this doesn't work try
    clicking the button down, then clicking it again quickly, or adjusting the
    sensitivity in self.sensitivity.
    """
    def __init__(self, pin, constants: dict, tempMeasure, changeDisplay, checks=3, check_period=80):
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
        self.sensitivity = 0.35
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
                    self.previousTime = self.currentTime - 1000 #Makes sure the first click isn't a double click
                dummyQ = False
                if self.currentTime - self.previousTime < self.sensitivity: # Check for a double click with sensitivity _
                    print("Double click detected")
                    if self.reverted == False: # Makes sure it only reverts once
                        self.reverted = True 
                        print("Reverting Q to", constants["revertQ"])
                        dummyQ = max(0, constants["revertQ"]) # Makes sure that it doesn't revert the cool life to a negative number; if 0 then can be reset
                        changeDisplay(revert = True)
                    else:
                        changeDisplay(reset = True)
                        dummyQ = constants["Qtotal"]  
                if dummyQ:     
                    global Qleft
                    Qleft = dummyQ
                    temp = tempMeasure()
                    heatLossRate = (temp) / constants["Rth"]
                    timeRemaining = dummyQ / (heatLossRate * (60*60))
                    displayTime(timeRemaining, None)
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
buzzer = Pin(10, Pin.OUT, Pin.PULL_DOWN) # Buzzer is connected between GPIO pin 14 (board pin 19), and ground. Polarity does matter
pushButton = Pin(18, Pin.IN, Pin.PULL_UP) # Push button is connected between GPIO pin 15 (board pin 20) and ground)
doorSwitch = Pin(14, Pin.IN, Pin.PULL_UP) # Door switch is connected between GPIO pin 16 (board pin 21), and ground
constants = updateJson('constants.json') # Import all the relevant constants
Qleft = constants["Qtotal"] # Initialises heat energy.
endBuzz = False

def wait_for_start(x):
    """
    An interrupt raised at the start, caused by the push button.
    This commences the rest of the code.
    """
    pushButton.irq(trigger=0) # Disable the interrupt to prevent further recursions
    global started
    started = True
    return

#try:
pushButton.irq(trigger=Pin.IRQ_RISING, handler=wait_for_start) # Attach the interrupt to the push button
print("Waiting to start; push the button or insert the module to start the timer")
# Waits for the button to be pushed to start the programme
started = False
waitForStart()
while started is False:
    sleep(1)
    continue
print("starting")
pushButton = SoftSwitch(Pin(18, machine.Pin.IN, machine.Pin.PULL_UP), constants, tempMeasure, changeDisplay) # THIS REQUIRES A TECHNICAL PRESS, PUSH THE BUTTON THEN PUSH AGAIN IN QUICK SUCCESSION, OR A QUICK TRIPLE CLICK
count = 0 # A counter for the number of loops the door has been left open
lastTime = time()
while True:
    timeDiff = (time() - lastTime) # Used to calculate the time difference over which heat was lost
    temp = tempMeasure()
    heatLossRate = (temp) / constants["Rth"] # (W), note the temp is actually a temperature difference, but since the ice pack core is 0C, the temperature in Celcius alone works
    QLoss = heatLossRate * (timeDiff) # (Heat energy, J, lost to surroundings).
    Qleft -= QLoss #Calculate remaining Q
    if Qleft <=0:
        pushButton.endTimer()
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
    
#except:
print("Error raised somewhere / KBDInterrupt.")
turnoff()
constants["revertQ"] = Qleft
constants["revertTime"] = time()
dumpJson("constants.json", constants)
