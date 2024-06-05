# Electrical connections to Pi Pico
Note that the below makes reference to the board pins and GPIO pins.. See pico.pinout.xyz for more information.

Pinout:
Board 1 (GP0): Display SDA
Board 2 (GP1): Display SCL
Board 3 (GND): Display GND 
Board 7 (GP5): DHT22 1 wire 
Board 8 (GND): DHT22 GND
Board 13 (GND): Buzzer GND
Board 14 (GP10): Buzzer Positive end
Board 18 (GND): Switch (bidirectional)
Board 19 (GP14): Switch (bidirectional)
Board 23 (GND): Push button (bidirectional)
Board 24 (GP18): Push button (bidirectional)
Board 29 (GP22): Connected to 3V3. Used as an extended positive terminal for further wires. (Display Vin and DHT Vin are connected to this)
Board 36 (3V3 Out): Connected to board 29 (GP22). Used as an extended positive terminal for further wires. (Display Vin and DHT22 Vin are connected to this)
Board 38 (GND): Battery holder positive terminal
Board 39 (VSYS): Battery holder positive terminal

![Electrical Connections][Electrical_Connections.jpeg]
