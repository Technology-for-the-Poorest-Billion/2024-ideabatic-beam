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

### Default Physical Arrangement

![IMG_9413C2C4692F-1](https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98609386/60c86eb5-2260-4c7b-bbe1-881a7b46c9ef)


*Why is there a 'default'? Shouldn't this be an open design problem?*

This is an open design problem, but it has a starting point. 

The starting point reflects the initial preferences of the project partner, which are informed by designs and analysis presented to her by previous contributors to this project. 

Given this, the quality of the communication and justification of our design decisions is crucial. 

# Communicating Design Decisions

Part of this project's useful output is a thorough documentation and justification of all design decisions made, quantified and visualised where possible. 

This is useful in the immediate term, as a means of presenting and justifying design decisions to the project partner, and also in the future, as subsequent work on this design problem will be streamlined by the clarity of this discussion, illustrating possibilities that have already been explored and eliminated. 

<br />

To quantify the performace of each design candidate, it will be scored in each of five dimensions:
- Cost effectiveness
- Robustness: Environmental resistance and mechanical robustness
- Insulation
- Veracity of temperature prediction
- User friendliness, primarily concerned with modularity

A candidate's performance can be visualised using a radar plot.

<img width="450" alt="Screenshot 2024-05-27 at 10 17 01" src="https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98609386/c045e667-ff44-4336-966f-8e713be696de">

****Figure X: Example of a radar plot****

The scores assigned will be 

- somethinng here about the non-linear characteristic curves of threshold dimensions

The scores will then be combined to give a Key Performance Indicator (KPI), which quantifies the overall performance potential of a design. 

Given that a failure to be fit for purpose in any of the five dimensions would render a design unsuitable, the KPI is calculated as the product of the five scores.

$\{KPI}$ = Score 1 $\times$ Score 2 $\times$ Score 3 $\times$ Score 4 $\times$ Score 5

This product-rating method is also useful for eliminating design candidates: evidence that a candidate is unsuitable on any of the five dimensions immediately sets its KPI to zero and eliminates it from the design process. 

As such, each candidate is checked first against its most problematic dimension, so that it can be quickly eliminated if unfeasible. 

The radar plot conveniently visualises three important things:
- Area shows which design candidates to proceed with
- Relative strengths and weaknesses of each design candidate
- Areas for maximum improvement on each design candidate

<br />


# The candidate designs
![IMG_548055A1CA77-1](https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98609386/4a9dc1aa-215c-462d-ad70-416d689262e8)

<br />
<br />

## Candidate 1: Direct Axial Connection - KPI

<img width="500" alt="Screenshot 2024-05-27 at 10 57 20" src="https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98609386/ae1fbc5b-4113-426e-a840-3b8d7522d0d4">

<br />
<br />

- This is the design prototyped by last year's group
- They neglected the obvious risk of insulation compromise

### Scoring Candidate 1 on the 'Insulation' Dimension

- Manufacturing and design interdependence:
Wiring ~ 2 mm. Door made of PBS, manufactured by casting ⇒ ± 1 mm

![IMG_BBFAF02D5158-1](https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98609386/e295f11e-0cd9-4e65-a32e-ce5a66196fa9)

- Optimising Geometry: Optimal housing for wiring is 'figure 8' shaped, results in: 6.3mm<sup>2</sup> wiring, 20.2mm<sup>2</sup> air.  

- Computing thermal resistance per unit depth of door;

- Running simulation to quantify effect on cool lifetime:


<img width="625" alt="Screenshot 2024-05-27 at 10 22 40" src="https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98609386/5056e698-d9bb-46e1-b047-cd04820a952a">


Cool lifetime at 24ºC ambient temperature reduces from 97.5 hours to 14.5 hours.

This is worst case (can cover ends etc.), but clearly worth worrying about! 

 
<br />
<br />



## Candidate 2: Wireless Communication - KPI

The dimension on which this design is most liekly to be unfeasible is cost effectiveness. 

In the interests of fairness, the best-case possibility is explored: 
- the lowest-cost implementation is used, which is to use a second microcontroller which can wirelessly communicate with the Pi Pico
- the quantity discounts for bulk-ordering is assumed to follow the best-case exponential decay per-unit cost curve derived below

### Deriving the Best-case Quantity Discount Curve

- Pricing tables for the components of interest were obtained from suppliers, either via direct contact or from their websites (see example).
 
<img width="300" alt="Screenshot 2024-06-02 at 16 25 21" src="https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98609386/b18de748-69dd-4355-bce0-9ec4ba21493f">

****Figure X: Example of quantity discount table****

- The most generous discounting rate across websites and components was assumed, and plotted on logarithmic axis
  
<img width="600" alt="Screenshot 2024-06-02 at 16 26 31" src="https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98609386/92732948-9a31-4829-a735-5a382bf50f22">

- The discounting rate was extrapolated past its usual limit of 100 components, up to our batch size of 3000 components resulting in the following best-case quantity discount:

****Per-unit price for 3000 units = 0.6 x Per-unit price for 1 unit****

This is the best-case estimate which is used for the cost-effectiveness feasability assessment of Design Candidate 2. 

### Best-case cost effectiveness of Candidate 2

| Part Description | Single Unit Cost | Per-Unit Cost in batch of 3000 | 
|-|-|-|
|Raspberry Pi Pico| £4.02 | £2.41 | 
|DHT22| £4.74 | £2.84 | 
| OLED Display | £10.19 | £6.11 | 
|Battery holder| £4.74 | £2.844 | 
|AA Batteries x2 | £4.74 | £2.88 | 

#### Per-unit cost for 100+ units: £14.65

Cost of making wireless (two microcontrollers cheaper than buying wireless temperature sensor):

Pi Pico → Pi Pico W: £2

Wireless module microcontroller (ESP8266) to communicate with Pi Pico: £4


- also need to take into account the cost of housing

So adds £6 to the single-unit price of electronics module

Might *just* be feasible if there are no other cost incurred (see below)





#### Optimistic Per-unit cost of core electronics module for 3000 units: £11.37 
(Assumes continuation of logarithmic pricing trend, such that per-unit cost falls to 60% of single-unit cost)

<br />

Hence,
**Single-unit cost that could feasibly be added: (15-11.37)/0.6 = £6.05** ≈ £6

<br />


## 3: Connection through Hinges - Feasability Assessment


## 4: Connection across Door Sensor - Feasability Assessment


Design candidates 3 and 4 are suitable, but offered no advantage according to their KPI over candidate 5, and threatened significantly more manufacturing complexity. 

Hence, the design taken forward is candidate 5. 


<img width="450" alt="Screenshot 2024-05-27 at 10 17 01" src="https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98609386/c045e667-ff44-4336-966f-8e713be696de">

<img width="450" alt="Screenshot 2024-05-27 at 10 15 11" src="https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98609386/e665e3ba-2e67-4c85-8292-c0a53bb3d79b">

<br />
<br />
