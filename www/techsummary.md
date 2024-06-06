---
title: Technical Summary
---


#### Modularise the electronics. Minimise the compromise to insulation.

As the electronics module is an additional opt-in product, we must ensure the design must still be watertight and properly insulated without the electronics module. Five key performance indicators (cost effectiveness, robustness, insulation, veracity of temperature prediction and modularity) were used to rank design candidates and determine our project direction.

![Screen Shot 2024-06-06 at 04 48 58](https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98922660/8e2888ef-57e2-454c-93f6-874d0a5d42a3)

One significant feature of our final design is having only one singular module that contains all of the electronics components, which diverges from previous designs which had another separate module for the temperature sensor.

Rapid prototyping techniques like CAD modelling and 3D printing were used to test various aspects of design, such as joint interfacing. Careful consideration was also taken to choose quality electronics and materials for the final product within our target budget.

<img width="450" alt="IMG_9140" src="https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98922660/b849253e-2078-4433-824c-92219873adc6">
<img width="253" alt="IMG_9139" src="https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98922660/43f5a139-c3ba-4566-b0a9-43eeaa229190">



### Electronics module
Within the electronics module, all the electrical componens are housed with a focus towards maintaining water resistance. 
The list of components used in the final prototype can be found below, with the appropriate soldering carried out:
- Pi Pico 
- OLED display
- DHT22 temperature sensor
- Buzzer
- Push button
- Button switch
- Battery holder (for two AA batteries)

A simplified logic process behind the code is described below. [For more details, click here](/code)
1. Initialises components, like the temperature sensor and display, making sure these are connected properly.
2. Prompts the user via the display to press the button to then commence calculating the remaining cool lifetime.
3. Main loop runs, calculating and displaying the remaining cool lifetime with appropriate warnings displayed once theres a certain cool lifetime left.
4. The door switch is then checked, and if it has been open for more than 2 consecutive times (ie if the door has been detected as being open in two runs of the main loop), it will buzz the buzzer.
5. Main loop sleeps for 5 minutes before repeating steps 3 onwards until the battery dies.






Authors: Ness, Romeo
