from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from time import sleep

#initialise display with data pins at GPIO 0,1 / board 1,2
i2c=I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 32, i2c)
oled.contrast(255)
oled.poweron()
oled.fill(0)

def waitForStart():
    """
    Displays a message prompting the user to start the programme.
    """
    oled.fill(0)
    displayStrings(["Waiting for the", "programme to", "start:", " Insert Module"], None)
    oled.show()

def splitString(string: str, n = 15):
    """
    Splits a string into multiple strings of length n to fit on screen.
    n=15 works best for the current screen, but for larger displays this may not be an issue.
    """
    out = [(string[i:i+n]) for i in range(0, len(string), n)]
    #print("split {} into {}".format(string, out))
    return out

def displayStrings(listring: list, timeleft: float):
    """
    Takes an input of multiple strings, and displays it with an optional timeleft
    """
    oled.fill(0)
    for i in range(len(listring)):
        oled.text(listring[i], 0, 0 + 8*i)
    if timeleft:
        oled.text(str(int(round(timeleft,0))) + " hours", 0, 8*(i + 2))
    else:
        return 
    
def turnoff():
    """
    Makes sure the display resets the buffer and shuts off properly.
    """
    oled.poweroff()


def displayTime(timeleft: int, printer: bool):
    """
    Displays the time left in the appropriate format.
    Will have a black background with yellow text when safe to use,
    and a yellow background with black text when unsafe (inverted).
    Assumes there is a 2 hour leniency during which the vaccines may still be okay.
    """
    oled.fill(0)
    if timeleft >= 10 and timeleft < 300:
        #print("Device is okay to continue using")
        statement = "Remaining cool life:"
        if printer == True: (print(statement + " {:1.0f} hours.".format(timeleft)))
        displayStrings(splitString(statement, 15), timeleft)
        #do that
    elif timeleft > 0 and timeleft < 10:
        statement = "Warning, cool  life is low:"
        if printer == True: (print(statement + " {:1.0f} hours.".format(timeleft)))
        displayStrings(splitString(statement, 15), timeleft)
    elif timeleft <= 0 and timeleft >= -2:
        oled.invert(1)
        statements = ["Vaccines have ", "left safe zone", "proceed with", "caution"]
        #print(splitString(statements, 15))
        #displayStrings(splitString(statements, 15), None)
        displayStrings(statements, None)
        if printer == True: (print("Vaccines have left safe zone proceed with caution"))
        # LIGHT UP SCREEN, SAY 0 HOURS REMAINING, REPLACE ICE PACK AND RESET MODULE
    elif timeleft <= -2:
        oled.fill(0)
        oled.invert(1)
        displayStrings(["Vaccines are", "not okay ", "to use"], None)
        print("Vaccines are not okay to use")
    else:
        raise ValueError
    oled.show()
    return

def changeDisplay(revert = False, reset = False):
    """
    Lets the user know that the double click has been detected and what the code is doing in response.
    """
    if revert:  
        print("Reverting cool life")
        oled.fill(0)
        oled.text("Reverting cool", 0, 0)
        oled.text("lifetime", 0, 8)
    elif reset:
        print("Resetting cool life")
        oled.fill(0)
        oled.text("Resetting cool",0 , 0)
        oled.text("lifetime", 0, 8)
    else:
        return 
    oled.show()
    sleep(1)
    
#to test display, uncomment the below and run.
#displayTime(0, True)
#oled.text("test", 0, 0)
#oled.show()

