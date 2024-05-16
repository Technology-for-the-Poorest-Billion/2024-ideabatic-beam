# Project management plan


## The people
`Team members strengths and weaknesses.`
`Skills required, training needed.`

### Romeo
Have experience prototyping electronics with a Pi 4 and different sensors, with understanding of different communication protocols used, and have used tkinter within python to make a very simple display on an LCD. Have experience with 3-D printing, having done so both in department and at home. 
<br> Requires training, or examples given, for C++ code, and for building a display interface.

### Ness
Training needed on rapid prototyping skills such as OpenSCAD and 3D printing.


## The resources needed
`Costing, parts required.`
| Part Description | Quantity| Unit Cost | Link |
|-|-|-|-|
|`BATTERY??? Can use powerbank?`| 1 | £? |  |
|`CONNECTORS FOR MODULE TO FIT INTO`| 1 | £? |  |
| Temperature sensor | 2 | £6.83 | https://uk.farnell.com/dfrobot/sen0137/dht22-temp-humidity-sensor-arduino/dp/3517874?ost=3517874 | 
| OLED Display | 1 | £14.04 | https://uk.farnell.com/seeed-studio/101020452/oled-display-1-12-128-x-128-pixels/dp/4007703?ost=4007703 | 
| Raspbery Pi Pico H | 1 | £4.73 |  https://uk.farnell.com/raspberry-pi/raspberry-pi-pico-h/raspberry-pi-board-arm-cortex/dp/3996081| 
| Solderless Breadboard | 2 | £3.38 | https://uk.farnell.com/multicomp/mcbb400/breadboard-solderless-300v-abs/dp/2395961 | 
| Buzzer | 1 | £3.26 | https://uk.farnell.com/projects-unlimited/ai-3245-tf-lw95-r/audible-signal/dp/1653528 | 
| Wires | 1 | £3.32 | https://uk.farnell.com/multicomp-pro/mp006282/jumper-wire-kit-male-to-male-100mm/dp/3617770?st=jumper%20wire | 
| Switch | 1 | £1.98 | https://uk.farnell.com/omron-electronic-components/d2ffl/microswitch-hinge-lever-1a-pcb/dp/1961095?st=lever%20switch | 
| 3D Printed Parts | Unknown | £5 | N/A | 

## The timeline

`NEED TO MAKE ROUGH TIMELINE`

## The assessment of the risks and safety

| Potential Hazard | Risk Level | Hazard Control Strategies |
|-|-|-|
| Excessive exposure to VOCs and <br> ultrafine particles from 3D printer| Medium | Proper ventilation <br> Check material is safe to use <br> Turn off printer if jammed|
| Burning oneself with soldering iron | Medium | Take care when using soldering iron, exhibit appropriate precautions |
| Burns from hot surfaces on printer | Medium | Wear protective gloves <br> Don't touch extruder or molten plastic <br> Check bed temperature before handling printed item|
| Getting trapped by moving parts <br> in 3D printer | Low | Keep clear of all moving parts|


## Contingency plans
What could go wrong? What to do when it happens?

### Electronics

#### Module unable to be compressed well enough whilst still allowing optimal functionality
The design can be reverted to include all components within the door, whilst having the door be modular. This effectively solves the issue of keeping the electronics modular, though isn't as feasible to do.


#### Failure to rebuild code for Pi Pico
The decision to switch to a Pi Pico has been done as the Pi Pico is a lot cheaper than an Arduino nano (and thus a lot more befitting of the project), and for familiarity with the team. If converting the available code to work with the pico takes too long, it may be a better idea to switch back to the Arduino, as the code has already been proven to work. 

#### Failure to add GPS tracking, or data logging
These are effectively "nice to haves" and aren't primary objectives. 


#### Failure to improve upon previous temperature sensing algorithm

### Mechanical

#### Failure to design "snap-fit" module and door:
The snap fit mechanism needs to be decided on rather early in the design process to ensure compatibility between different parts. If such a mechanism could not be reliably prototyped or functional, it would cause difficulties in continuing with other aspects of the project. Therefore it should be the first point of investigation before deciding on other aspects of design.

#### Difficulties integrating electronics with casing design:
As the casing design is dependent on the type and number of components used by the electronics team, later changes to the design of electronics may affect the design of the casing. If it takes a long time to settle on a design for the electronics module, there may not be enough time to complete the casing design. Ensure the dimensions of slot and casing prototypes can be easily changed in later iterations to accomodate changes in size of the module, and work with electronics team to ensure shape of module is reasonable.

#### No time for improving robustness of spring mechanism: 
It is foreseeable that we may run out of time to deeply investigate the self-closing door mechanism, as it involves improving on many iterations of previous designs that may have explored most aspects of torsional springs, and may require extensive testing to yield new results. It is not the most critical aspect of this design project.
