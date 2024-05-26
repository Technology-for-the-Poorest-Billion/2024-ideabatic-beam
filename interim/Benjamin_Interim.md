• Troubleshooting skills 
My role: Project management, The design problem

## Some additional context:
This project was taken on by a team last year, here is the progress they made and where they fell short:

- successfully made an electronic circuit that displayed the temperature and remaining cool life
- was not modular, was not able to clip on and off from the door
- ambiguity in their recommendation for position of the temperature sensor
- did not quantify the effect of the electronics module compromising insulation
- mechanical issues with door ergonomics, lack of protection for display screen

<br />

## Reassessing and redefining the objective:

Following discussions with our project partner and Alexandre, the objectives for the project have been simplified:

#### Primary goal: (i) Make the electronics modular, (ii) minimise the compromise to insulation.

Secondary objectives (only if primary satisfied): 
- implementing GPS tracking and data logging on the electronics module
- adapting the temperature prediction algorithm to account for the door open vs door closed

  <br />

## Formalising the primary design problem:
- electronics module with temperature sensor to inform algorithm and display for user
- module should be clip on clip off (opt in design, easy charging)
- minimise compromise to insulation
- target budget: £15 (batch size ~3000)

<br />

#### Core Electrical Circuit

<img width="550" alt="Screenshot 2024-05-26 at 15 14 30" src="https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98609386/d8ad377c-824a-41d8-bdd4-f801853df728">

In its simplest state, only requires four components:
Raspberry Pi Pico Microcontroller, DHT22 temperature sensor, 10kΩ resistor and OLED display
* note - temperature sensor series may be subject to change

<br />

### Default Physical Arrangement

![IMG_9413C2C4692F-1](https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98609386/60c86eb5-2260-4c7b-bbe1-881a7b46c9ef)


Why is there a 'default'? Shouldn't this be an open design problem?
Yes, but...
Project partner has her own preferences, particularly concerned with sensor degradation, 

<br />

#### Communication and justification (preferably quantitative) of our design decisions is important!

<br />

# The candidate designs

## 1: Direct Axial Connection

![IMG_E583BCB9C4C2-1](https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98609386/3e06c55b-12ec-494d-95e8-133f6d736d58)


- Design prototyped by last year's group
- They neglected the obvious risk of insulation compromise

### Quantifying Compromise to Insulation

- Manufacturing and design interdependence:
 Smallest wiring ~ 2 mm. Door made of PBS, cast ⇒ ± 1 mm

- Optimising Geometry: Optimal housing for wiring is 'figure 8' shaped, results in: 6.3mm<sup>2</sup> wiring, 20.2mm<sup>2</sup> air.  

- Computing thermal resistance per unit depth of door;

- Running simulation to quantify effect on cool lifetime:
![IMG_9BA91C064C3B-1](https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98609386/778feb40-0244-448c-85c7-256ff3ce7fd7)



- Kitty, our project partner, still very interested in using the temperature sensor on the door. Part of the useful output of this project will be a demonstration of why this is not necessary, by attempting to quantify with a KPI the drawbacks. 




- using the temperature sensor externally only enhances potential for modularity
- if temperature sensor external, we will need to reconsider series used as DHT22 does not have very good water resistance. Will need to revisit component selection. 


Radar plot for 

- Material used for door is Acrylonitrile Butadiene Styrene, or ABS; door is to be manufactured by polymer casting, which would have a tolerance of ~1 mm to a first-order estimation.
- Smallest cables we can source economically will have diameter ~2mm
- Hence in the best case we perfectly house the two cables,
- In the worst case we have a clearance of 1mm either side of open space,
- This does not take into account the 

- Clear illustration of design and manufacturing method being interdependent 


Introducing the Key Performance Indicator: Area of the Radar Plot. Alternatively just a weighted product of the various dimensions. Probably more appropriate since each one is essential, so any one going to zero should give a KPI of zero. 

Dimensions of Radar plot:
- cost
- mechanical robustness
- insulation efficacy
- accuracy and verasity of temperature measurement

Ideal output will be a visual and quantified representation of the experienced or expected suitability of each candidate design.

Experiences for the ones that we actually make into prototypes, 


Each student would ideally present a specific aspect they have contributed to (giving credits to other where appropriate) and briefly explain how the work package they present fits within the overall project

• Team working skills, good log of work done and issues

The most cost-effective way of creating the wireless communication is likely to be 

Cost of making wireless:
Pi Pico + £2
https://thepihut.com/products/raspberry-pi-pico-w?src=raspberrypi

Wireless module microcontroller to communicate with Pi Pico: £4
https://kunkune.co.uk/shop/esp32-esp8266/esp8266-nodemcu-v2-cp2102-lua-wifi-development-board-module/

So adds £6 to the price of electronics module

Even with bulk discounts unlikely to be economical given batch size and budget



My output for tomorrow:
- A schematic of the electrical circuit we are looking to design. 
- An illustration of the added uncertainty caused by putting the temperature sensor external (thermal resistive component)
- Drawing of each overall design considered so far
- Outline of the dimensions of the key performance indicator, some radar plots for each candidate design (to be updated)
- A rough rating of each candidate's rankings on radar plot
(eg a brief calculation showing the insulation lost to a small cylindrical hole for wire through the insulating cuboid 
(in terms of depth of cuboid etc))



References

https://mathworld.wolfram.com/Lens.html


• Where applicable, show an early prototype and demonstrate feasibility;
• Present a summary of team members' personal and technical development (what have you learnt and how have you learned it?);
• Update the project development time-line and present a plan for completion.
