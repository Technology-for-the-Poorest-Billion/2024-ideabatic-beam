# Benjamin's Work done so far
<br />


## Formalising the primary design problem:
- electronics module with temperature sensor to inform algorithm and display for user
- module should be clip on clip off (opt in design, easy charging)
- minimise compromise to insulation
- target budget: £15 (batch size ~3000)

<br />

## Some additional context:
This project was taken on by a team last year, here is the progress they made and where they fell short:

- successfully made an electronic circuit that displayed the temperature and remaining cool life
- was not very modular, required removal of door which was tedious in practice.
- ambiguous in their final recommendation for position of the temperature sensor
- did not quantify the effect of the electronics module compromising insulation
- mechanical issues with door ergonomics, lack of protection for display screen

<br />

## Our Design Process

<br />

#### Core Electrical Circuit

<img width="550" alt="Screenshot 2024-05-26 at 15 14 30" src="https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98609386/d8ad377c-824a-41d8-bdd4-f801853df728">

In its simplest state, only requires four components:
Raspberry Pi Pico Microcontroller, DHT22 temperature sensor, 10kΩ resistor and OLED display
* note - temperature sensor series may be subject to change

<br />

### Default Physical Arrangement

![IMG_9413C2C4692F-1](https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98609386/60c86eb5-2260-4c7b-bbe1-881a7b46c9ef)


*Why is there a 'default'? Shouldn't this be an open design problem?*

Yes, but...

Project partner has her own preferences, particularly concerned with sensor degradation, exposure to heat from electronics module, veracity of temperature prediction.

<br />

Part of the useful output of this project will be a demonstration of why this is might not be necessary/optimal, by attempting to visualise, and quantify with a KPI, the drawbacks.


#### Communication and justification of our design decisions is important!

<br />

# The candidate designs
![IMG_548055A1CA77-1](https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98609386/4a9dc1aa-215c-462d-ad70-416d689262e8)

<br />
<br />

## 1: Direct Axial Connection - Feasability Assessment

<img width="500" alt="Screenshot 2024-05-27 at 10 57 20" src="https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98609386/ae1fbc5b-4113-426e-a840-3b8d7522d0d4">

<br />
<br />

- This is the design prototyped by last year's group
- They neglected the obvious risk of insulation compromise

### Quantifying Compromise to Insulation

- Manufacturing and design interdependence:
 Smallest wiring ~ 2 mm. Door made of PBS, manufactured by casting ⇒ ± 1 mm

![IMG_BBFAF02D5158-1](https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98609386/e295f11e-0cd9-4e65-a32e-ce5a66196fa9)

- Optimising Geometry: Optimal housing for wiring is 'figure 8' shaped, results in: 6.3mm<sup>2</sup> wiring, 20.2mm<sup>2</sup> air.  

- Computing thermal resistance per unit depth of door;

- Running simulation to quantify effect on cool lifetime:


<img width="625" alt="Screenshot 2024-05-27 at 10 22 40" src="https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98609386/5056e698-d9bb-46e1-b047-cd04820a952a">


Cool lifetime at 24ºC ambient temperature reduces from 97.5 hours to 14.5 hours.

This is worst case (can cover ends etc.), but clearly worth worrying about! 

 
<br />
<br />






## 2: Wireless Communication - Feasability Assessment

Cost of making wireless (two microcontrollers cheaper than buying wireless temperature sensor):

Pi Pico → Pi Pico W: £2

Wireless module microcontroller (ESP8266) to communicate with Pi Pico: £4

So adds £6 to the single-unit price of electronics module

Might *just* be feasible if there are no other cost incurred (see below)


### Budget Feasability

| Part Description | Single Unit Cost | Bulk 100+ Unit Cost |  |
|-|-|-|-|
|Raspberry Pi Pico| £4.02 | £3.14 | 
|DHT22| £4.74 | £3.56 | 
| OLED Display | £10.19 | Pending (supplier contacted) ~ £7.95 |  

#### Per-unit cost for 100+ units: £14.65

<img width="554" alt="Screenshot 2024-05-27 at 09 31 38" src="https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98609386/ce9f7c97-dcb2-4112-bca8-47bfbc8a6cdc">

<img width="294" alt="Screenshot 2024-05-26 at 22 03 47" src="https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98609386/8339f98f-2ae2-430d-b406-43770354d9cf">

#### Optimistic Per-unit cost of core electronics module for 3000 units: £11.37 
(Assumes continuation of logarithmic pricing trend, such that per-unit cost falls to 60% of single-unit cost)

<br />

Hence,
**Single-unit cost that could feasibly be added: (15-11.37)/0.6 = £6.05** ≈ £6

<br />

# Communicating Design Decisions

To justify design decisions, score each in the following dimensions, resulting in Key Performance Indicator

Radar plot for visualisation of rankings:

<img width="450" alt="Screenshot 2024-05-27 at 10 17 01" src="https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98609386/c045e667-ff44-4336-966f-8e713be696de">

<img width="450" alt="Screenshot 2024-05-27 at 10 15 11" src="https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98609386/e665e3ba-2e67-4c85-8292-c0a53bb3d79b">

<br />
<br />

Since each dimension critical, a better KPI might be a weighted *product* of the scores in each dimension. 

- which candidates to proceed with
- relative strengths and weaknesses
- areas for improvement 

<br />

# Benjamin's Personal and Technical Development
- Redefining the objectives: what is really necessary?
- Discussing changes of direction with project partner
- Applying conceptual engineering skills to a real problem (eg heat transfer, manufacturing + design interplay, circuit design)
- Learning how to develop code in Raspberry Pi's Micropython IDE Thonny (not shown in this presentation)
- Clear documentation and communication of design decisions for partner
- Communicating directly with suppliers
- Budgeting, including obtaining quotes for bulk orders
- Project direction and management

**How I have learnt/acquired these developments**: Direct exposure by doing

<br />

**References**

https://mathworld.wolfram.com/Lens.html

https://thepihut.com/products/raspberry-pi-pico-w?src=raspberrypi

https://kunkune.co.uk/shop/esp32-esp8266/esp8266-nodemcu-v2-cp2102-lua-wifi-development-board-module/

https://chachart.net/radar?lang=en
