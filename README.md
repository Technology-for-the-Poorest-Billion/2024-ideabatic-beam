# SMILE, by Ideabatic
This is an IIA project, carried out in Easter term with the intention to improve upon the design of the current SMILE prototype.


## Setup (electronics)
In order to set up the electronics, the following parts are required (note only these were used in the final prototype). [The specific items used can be found here.](https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/blob/main/BillOfMaterials.md)
<br>
|Item|Quantity Used|
|-|-|
|Raspberry Pi Pico|1|
|Oled Display|1|
|DHT22 Temperature Sensor|1|
|Button|1|
|Switch|1|
|Buzzer|1|
|Dual AA Battery Holder (with batteries)|1|

### Connections
The pi should be connected as shown in the following picture:
The connections can be switched around as long as they are appropriately changed in the code. The sensors initiate the pins in their own pieces of code, whereas the button, switch, and buzzer are initialised in main.py.

![Electrical Connections](https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/blob/main/Pictures/ElectricalConnections.png)

[For more detail, click here](https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/blob/main/ElectricalConnections.md)

### Pi Setup
1. Install micropython onto the board. 
  - This can be done via thonny; connect the Pi to the computer whilst holding the BOOTSEL button, and install the standard relevant micropython.
2. Install the ssd1306 and dht libraries.
  - This can be also be done via thonny; with the pi connected and responding, click tools -> manage packages and install the libraries there.
3. Port over all items in the code folder.
4. The Pico, on boot, will run main.py by default. For testing, mainTest.py is recommended, as this can "accelerate" the heat loss rate, along with increasing the polling rate, allowing for easy testing of all the features.
