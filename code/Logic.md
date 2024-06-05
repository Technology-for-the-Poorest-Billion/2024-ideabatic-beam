This file looks to explain the general function of the code at a glance, with more detail that can be found within the individual python files.

Logic Process:
1. First imports all the functions, does so by importing the respective files. When importing test.py, the tests are carried out. If there is an issue, the terminal will let you know where the failure was. Switch/button failure is difficult to detect and so will have to be done in use. Buzzer testing can also be done but can be annoying if tested each time the code is ran.
2. Initialises all the extra electronics: the switch/button/buzzer so that it is ready to be used. Also imports the dictionary in constants.json with all the relevant values stored there.
3. Waits for the button to be pressed before starting the main loop. This is done by raising an interrupt on the rising edge of a button push (active low).
4. Once this is done, the push button is changed to the class SoftSwitch, which allows for debouncing and detection of double clicks, with the appropriate actions carried out, this is explained later.
5. Now, the main loop of the code runs in a try: section. This ensures that if there are any errors that prevent the running of the code, the constants are dumped back to the JSON (important to remember the last known Q for later reversion), and the display is turned back off. 
