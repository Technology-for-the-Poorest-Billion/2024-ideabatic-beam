### This file looks to explain the general function of the code at a glance, with more detail that can be found within the individual python files.

# Logic Process of main.py:
1. The code imports all the functions, does so by importing the respective files. When importing test.py, the tests are carried out. If there is an issue, the terminal will let you know where the failure was. Switch/button failure is difficult to detect and so will have to be done in use. Buzzer testing can also be done but can be annoying if tested each time the code is ran.
2. Initialises all the extra electronics: the switch/button/buzzer so that it is ready to be used. Also imports the dictionary in constants.json with all the relevant values stored there.
3. Waits for the button to be pressed before starting the main loop. This is done by raising an interrupt on the rising edge of a button push (active low).
4. Once this is done, the push button is changed to the class SoftSwitch, which allows for debouncing and detection of double clicks, which on first click will revert the time remaining to the last measured time before boot up. Any further clicks will reset the cool life completely.
5. Now, the main loop of the code runs in a try: section. This ensures that if there are any errors that prevent the running of the code, the constants are dumped back to the JSON (important to remember the last known Q for later reversion), and the display is turned back off. 
6. The heat life calculations run first, where the heat loss rate is calculate using the temperature difference between the core and outside (ie T_outside - 0) and the (constant) thermal resistance of the cooler box. An estimation of the remaining cool life is made based on the assumption that the temperature remains constant, though this is updated every loop (of time period tdelta, default 5 minutes). If the remaining cool life is negative, the code will cause the buzzer to buzz for 2 seconds.
7. The remaining cool life is then displayed and the door switch is checked. If the door has been open for two consecutive checks, the switch will buzz every 5 minutes until it is shut. Note that the buzzer sound is irritating at worst.
9. The code then sleeps for tdelta, default 5 minutes before running the main loop again until power is cut.
    
