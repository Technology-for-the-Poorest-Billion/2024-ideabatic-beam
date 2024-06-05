# Issues and further improvements
- The battery life of the module can certainly be improved. When sleeping, the module sips 30mA at 3V which depletes 2 AA batteries in under 3 days. 
  - The pico's power draw can be reduced by using machine.lightsleep instead of sleep to cut down on the power draw of the pico, and additionally reducing the power draw of the display (ie by using a lower display brightness).
- A relatively easy improvement to the code would be to have the display turn on for a second when the button is pressed once, before shutting off again, though this will make the display less useful.
- A smaller on circuit temperature sensing component can be used (possibly a TMP36) instead of the bulky DHT22 module currently used to improve the power draw, and allowing for more flexibility instead of relying on a library.
- 
