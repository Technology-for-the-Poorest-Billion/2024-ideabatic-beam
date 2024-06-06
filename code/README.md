### This folder contains the relevant code required to run the Pi. [For setup instructions, click here.](https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/tree/main)
# Logic Process:
1. The code imports all the functions, does so by importing the respective files. When importing test.py, the tests are carried out. If there is an issue, the terminal will let you know where the failure was. Switch/button failure is difficult to detect and so will have to be done in use. Buzzer testing can also be done but can be annoying if tested each time the code is ran.
2. Initialises all the extra electronics: the switch/button/buzzer so that it is ready to be used. Also imports the dictionary in constants.json with all the relevant values stored there.
3. Waits for the button to be pressed before starting the main loop. This is done by raising an interrupt on the rising edge of a button push (active low).
4. Once this is done, the push button is changed to the class SoftSwitch, which allows for debouncing and detection of double clicks, which on first click will revert the time remaining to the last measured time before boot up. Any further clicks will reset the cool life completely.
5. Now, the main loop of the code runs in a try: section. This ensures that if there are any errors that prevent the running of the code, the constants are dumped back to the JSON (important to remember the last known Q for later reversion), and the display is safely turned back off. 
6. The heat life calculations run first, where the heat loss rate is calculate using the temperature difference between the core and outside (T_outside - 0) and the (constant) thermal resistance of the cooler box. An estimation of the remaining cool life is made based on the assumption that the temperature remains constant, though this is updated every loop (of time period tdelta, default 5 minutes). If the remaining cool life is negative, the code will cause the buzzer to buzz for 2 seconds.
7. The remaining cool life is then displayed and the door switch is checked. If the door has been open for two consecutive checks, the switch will buzz every 5 minutes until it is shut. Note that the buzzer sound is irritating at worst.
9. The code then sleeps for tdelta, default 5 minutes before running the main loop again until power is cut.

# Issues and further improvements
- The battery life of the module can certainly be improved. When sleeping, the module sips 30mA at 3V which depletes 2 AA batteries in 78 hours, whilst the expected cool life at 22 degrees is just over 100 hours. 
  - The pico's power draw can be reduced by using machine.lightsleep instead of sleep, and additionally reducing the power draw of the display (i.e. by using a lower display brightness, using the display with a duty cycle).
    - Note that lightsleep may cut power to the display, and can have problems with the external modules. It is also incredibly annoying to prototype with, requiring a manual reconnect of the usb connector after each use.
    - If this is used, it may be beneficial to have the display only run when the button is pressed via an interrupt; this takes advantage of this aspect to further reduce the power consumption
- A relatively easy improvement to the code would be to have the display turn on for a second when the button is pressed once, before shutting off again, though this will make the module less useful; this was considered but decided against.
- A smaller on circuit temperature sensing component can be used (i.e. a TMP36) instead of the bulky DHT22 module currently used to improve the power draw, and allowing for more flexibility instead of relying on a library.
- The overall size of the module can be reduced by sourcing more use case specific components.
- A rechargeable battery can be used to provide the required lifetime, though this would require a battery management system too, along with a USB port which could reduce water resistance.
- A different microcontroller with even lower power draw may be preferable, possibly an ESP32, which has the added benefit of being very small.

