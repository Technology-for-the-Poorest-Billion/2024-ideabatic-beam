# SMILE, by Ideabatic
This is an IIA project, carried out in Easter term with the intention to improve upon the design of the current SMILE prototype.

# To Navigate Through this Repository

- The design considerations are linked coherently in a logic order, starting with a [formalisation of the design problem](https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/blob/main/Benjamin_Outputs/Our_Design_Problem_and_Context.md).

- The key information for mechanical design and prototyping can be found [here](https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/tree/main/mechanical%20design)

- The key information for electronic design and prototyping can be found [here](


## Setup (electronics)
In the final prototype, [the items listed here were used.](https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/blob/main/BillOfMaterials.md)

### Connections
The pi should be connected as [described here.](https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/blob/main/ElectricalConnections.md)
The connections can be switched around as long as they are appropriately changed in the code. The sensors initiate the pins in their own pieces of code, whereas the button, switch, and buzzer are initialised in main.py.

### Pi Setup
1. Install micropython onto the board. 
  - This can be done via thonny; connect the Pi to the computer whilst holding the BOOTSEL button, and install the standard relevant micropython.
2. Install the ssd1306 and dht libraries.
  - This can be also be done via thonny; with the pi connected and responding, click tools -> manage packages and install the libraries there.
3. Port over all items in the code folder.
4. The Pico, on boot, will run main.py by default. For testing, mainTest.py is recommended, as this changes the polling rate to 1 per second, and artificially inflates the heat loss so that the display stages can be shown. This also allows for testing of the buzzer.
