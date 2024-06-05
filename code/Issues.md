# Issues and further improvements
- The battery life of the module can certainly be improved. When sleeping, the module sips 30mA at 3V which depletes 2 AA batteries in under 3 days. 
  - The pico's power draw can be reduced by using machine.lightsleep instead of sleep, and additionally reducing the power draw of the display (ie by using a lower display brightness).
    - Note that lightsleep may cut power to the display, and can have problems with the external modules. It is also incredibly annoying to prototype with, requiring a manual reconnect of the usb connector after each use.
- A relatively easy improvement to the code would be to have the display turn on for a second when the button is pressed once, before shutting off again, though this will make the display less useful.
- A smaller on circuit temperature sensing component can be used (possibly a TMP36) instead of the bulky DHT22 module currently used to improve the power draw, and allowing for more flexibility instead of relying on a library.
- The overall size of the module can be reduced by sourcing more use case specific components.
- A rechargeable battery can be used to provide the required lifetime, though this would require a battery management system too, along with a USB port which could reduce water resistance.
- A different microcontroller with even lower power draw may be preferable.
