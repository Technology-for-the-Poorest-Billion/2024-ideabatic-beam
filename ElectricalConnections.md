# Electrical connections to Pi Pico
Note that the below makes reference to the board pins and GPIO pins.. See pico.pinout.xyz for more information.

## Pinout:
|Board|GPIO/V|Purpose|
|-|-|-|
|1|GP0|Display SDA|
|2|GP1|Display SCL|
|3|GND|Display GND |
|7|GP5|DHT22 1 wire |
|8|GND|DHT22 GND|
|13|GND|Buzzer GND|
|14|GP10|Buzzer Positive end|
|18|GND|Switch (bidirectional)|
|19|GP14|Switch (bidirectional)|
|23|GND|Push button (bidirectional)|
|24|GP18|Push button (bidirectional)|
|29|GP22|Connected to board 36(3V3 Out). Used as an extended positive terminal for further wires. (Display Vin and DHT Vin are connected to this)|
|36|3V3 Out|Connected to board 29 (GP22). Used as an extended positive terminal for further wires. (Display Vin and DHT22 Vin are connected to this)|
|38|GND|Battery holder positive terminal|
|39|VSYS|Battery holder positive terminal|




<BR>Board 1 (GP0): Display SDA
<br>Board 2 (GP1): Display SCL
<br>Board 3 (GND): Display GND 
<br>Board 7 (GP5): DHT22 1 wire 
<br>Board 8 (GND): DHT22 GND
<br>Board 13 (GND): Buzzer GND
<br>Board 14 (GP10): Buzzer Positive end
<br>Board 18 (GND): Switch (bidirectional)
<br>Board 19 (GP14): Switch (bidirectional)
<br>Board 23 (GND): Push button (bidirectional)
<br>Board 24 (GP18): Push button (bidirectional)
<br>Board 29 (GP22): Connected to 3V3. Used as an extended positive terminal for further wires. (Display Vin and DHT Vin are connected to this)
<br>Board 36 (3V3 Out): Connected to board 29 (GP22). Used as an extended positive terminal for further wires. (Display Vin and DHT22 Vin are connected to this)
<br>Board 38 (GND): Battery holder positive terminal
<br>Board 39 (VSYS): Battery holder positive terminal

![Electrical Connections][Electrical_Connections.jpeg]
