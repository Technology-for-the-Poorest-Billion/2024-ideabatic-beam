# SMILE, by Ideabatic
This is an IIA project, carried out in Easter term with the intention to improve upon the design of the current SMILE prototype.


## Setup (electronics)
In order to set up the electronics, the following parts are required (note only these were used in the final prototype). The specific items used can be found in the ![Bill of Materials][billOfMaterials.md].
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
Rough connections, maybe add in a diagram later. Note all components will work from the 3V3 rail of the Pi:
<br>Display: Power, GND, SDA Board pin 1, SCL Board pin 2
<br>DHT: Power, GND, 1 Wire Board pin 4
<br>Button: GND, Board pin 20
<br>Switch: GND, Board pin 21
<br>Buzzer: GND, Board pin 19

### Pi Setup
1. Install micropython onto the board. 
  - This can be done via thonny; connect the Pi to the computer whilst holding the BOOTSEL button, and install the standard relevant micropython.
2. Install the ssd1306 and dht libraries.
  - This can be also be done via thonny; with the pi connected and responding, click tools -> manage packages and install the libraries there.
3. Port over all items in the code folder.
4. The Pico, on boot, will run main.py by default. For testing, mainTest.py is recommended, as this can "accelerate" the heat loss rate, along with increasing the polling rate, allowing for easy testing of all the features.
