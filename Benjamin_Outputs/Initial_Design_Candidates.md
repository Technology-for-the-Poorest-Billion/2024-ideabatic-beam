

# The candidate designs

Based on previous work informing a ['default design'](https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/blob/main/Benjamin_Outputs/Our_Design_Problem_and_Context.md), four general candidate designs following this archetype were brainstormed, along with one outside of the archetype (Candidate 5):


![IMG_548055A1CA77-1](https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98609386/4a9dc1aa-215c-462d-ad70-416d689262e8)

<br />
<br />

Applying the [conservative principles for analysis](https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/blob/main/Benjamin_Outputs/Conservative_Analysis_Principles.md), each design was analysed via *eliminating analysis*, to result in a quantified measure of its best-case performance. Best-case performance was analysed at this stage to ensure that no viable designs were discarded. 

<br />


## Candidate 1: Direct Axial Connection - Eliminating Analysis on the Insulation Dimension

<img width="500" alt="Screenshot 2024-05-27 at 10 57 20" src="https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98609386/ae1fbc5b-4113-426e-a840-3b8d7522d0d4">

<br />
<br />

- This is the design prototyped by last year's group
- They neglected the obvious risk of insulation compromise

The first dimension on which Candidate 1 will be scored is insulation, in an attempt to elimiinate it early on the grounds that it compromises insulation to an unacceptable level. 

### The Problem:
- Electrical wiring, made of copper, is very thermally conductive, so an axial path of heat flow is effectively short-circuited.
- Additionally, there is a manufturing and design interdependence. Given that the door is intended to be manufactured by polymer casting, there is significant tolerance. 
- To ensure that the wires fit in the door, the design therefore needs to made too wide. Then with the tolerance, the best case still results in some parts in the manufacturing batch containing a significant air gap around the wires. 


Inkeeping with the conservative analysis principles, the analysis will be done with the following assumptions, each of which leads to the most conservative estimate of insulation compromise:
- the wiring used is has the lowest readily available diameter, 1 mm
- manufacturing is done with maximal precision. For casting a polymer, this is of order ±1 mm accuracy on casting

- the change in area of the door cross-section is neglected

### Optimising Geometry: 
Coordinate geometry reveals that the optimal housing for wiring is 'figure 8' shaped.
Evaluating the area of the lens shape created by the two tunnels overlapping, this results in: 1.57mm<sup>2</sup> wiring, 3.83mm<sup>2</sup> air.

![IMG_BBFAF02D5158-1](https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98609386/e295f11e-0cd9-4e65-a32e-ce5a66196fa9)

The bulk of the door is made of the insulating material tricast. 
Previous contributors computed the average thermal resistance *per unit depth* of door to be 

$\ {R_{th, tri}} =$ = 198.6 KW<sup>-1</sup>m<sup>-1</sup>

The area of copper in two 1mm diameter copper wires is 1.57 mm<sup>2</sup>, 

$\implies$ *per unit depth*,

$\ {R_{th, copper}} =\frac{1}{\lambda\times{A}} =\frac{1}{{398}\times{1.57\times{10^-6}}} =$ 1600 KW<sup>-1</sup>m<sup>-1</sup>

$\ {R_{th, air}} =\frac{1}{\lambda\times{A}} =\frac{1}{{0.025}\times{3.83\times{10^-6}}} =$ 10.4 x 10<sup>6</sup> KW<sup>-1</sup>m<sup>-1</sup>

The three resistive elements are in parallel through the entire depth of the door, so 

*modelling these as a thermal resistances in parallel with the insulating material tricast*,

$\frac{1}{R_{th, total}} = \frac{1}{R_{th, copper}} + \frac{1}{R_{th, air}} + \frac{1}{R_{th, tri}}$

$\implies {R_{th, total}} =$ 176.7 KW<sup>-1</sup>m<sup>-1</sup>

Thus the thermal insulation of the door per-unit depth is reduced by 11.04%. 

Using data from previous contributors to compute the new total thermal resistance between the ice pack at the centre of the cooling device and the external air, the thermal resistance is found to be reduced from 9.72 to 8.88 KW<sup>-1

The new value for overall thermal reistance was simulated in the cool life estimation algorithm, and the effect of the axial connection was plotted:

<img width="601" alt="Screenshot 2024-06-03 at 22 38 47" src="https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98609386/a737c389-ac74-4d22-b0e9-230d6f306884">


Cool life decreases from 97.5 hours to 89.1 hours in 24ºC ambient temperature. 


This is deemed feasible - the reduction in cool lifetime is not drastic enough to eliminate this candidate entirely. 

However, it will be scored lower than the other design candidates, which don't threaten any significant reduction in insulation. 

According to the scoring characteristic, this design therefore receives a score of 7.6 on the insulation dimension. 



## Candidate 2: Wireless Communication - Eliminating Analysis on the Cost Effectiveness Dimensions

The dimension on which this design is most liekly to be unfeasible is cost effectiveness. 

According to conservative analysis principles, the best-case possibility is explored: 
- the lowest-cost implementation is used, which is to use a second microcontroller which can wirelessly communicate with the Pi Pico
- the quantity discounts for bulk-ordering is assumed to follow the best-case exponential decay per-unit cost curve derived below

### The electrical components needed

- Pi Pico → Pi Pico W to allow for wireless communication

- Wireless module microcontroller (ESP8266) to operate temeprature sensor and communicate with Pi Pico

- AA batteries x2 needed to power ESP8266

- Holder for AA batteries


### Deriving Possible Quantity Discount Curves
- Most electrical component websites offered limited information on the discounts offered for ordering components in large quantites:

<img width="300" alt="Screenshot 2024-06-02 at 16 25 21" src="https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98609386/b18de748-69dd-4355-bce0-9ec4ba21493f">

#### Table 1: Example of publicly avaialble quantity discounting data

- Via private communication with suppliers about buk orders, a more detailed range of possible quantity discounting curves were obtained.
- The discounting data received only extends to 1000 units at most, whereas our batch size was 3000
- By modelling the quantity discounts a logarithmic decay, the range of cost curves were extrapolated to a batch size of 3000 to obtain a best-case and worst-case estimate for the quantity discount offered on electrical components. 
 
<img width="200" alt="Screenshot 2024-06-06 at 14 56 32" src="https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98609386/4a36b463-b2b1-4282-b673-373ed80a3c44">

<img width="671" alt="Screenshot 2024-06-06 at 14 01 27" src="https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98609386/2c56ec1e-dc93-4ba6-8c1a-76ee717190f9">

- For a best-case eliminating analysis, the most generous discounting rate across websites and components was assumed 
  

****Per-unit price for 3000 units = 0.6 x Per-unit price for 1 unit****

This is the best-case estimate which is used for the cost-effectiveness feasability assessment of Design Candidate 2. 

### Best-case cost effectiveness of Candidate 2

| Part Description | Single Unit Cost | Per-Unit Cost in batch of 3000 | 
|-|-|-|
|Raspberry Pi Pico W| £5.80 | £3.48 | 
|ESP8266| £4.22 | £2.53 | 
|DHT22| £4.74 | £2.84 | 
| OLED Display | £4.98 | £2.99 | 
| Door-sensing switch | £1.02 | £0.61 |
|Buzzer for door open alert| £2.15 | £1.29 | 
|Battery holder x2 | £1.96 | £1.18 | 
|AA Batteries x4 | £2.316 | £1.39 | 

The cost of electrical wiring, resistors and capacitors is neglected. 

#### Best-case per-unit cost for 3000 units: £16.31

- already above budget, without accounting for the cost of housing the module

This is above the budget, making the cost effectiveness score zero, giving Candidate 2 a KPI of zero. 

Candidate 2 will therefore be eliminated from consideration without further consideration. 

(the increased cost from the base module is the cost of two AA batteries + one battery holder + ESP8266 + Cost of converting Pi Pico to Pi Pico W, which totals to £5.02 increased cost, in the best case.)





<br />
Scoring each design on according to the scoring criteria outline on Design_Approach.md, the following table was constructed, representing the overall performance. Candidate 2 was not scored as it was proven inviable on the insulation dimension. 

<br />

| Dimension | Candidate 1 Score | Candidate 2 Score | Candidate 3 Score | Candidate 4 Score | Candidate 5 Score | 
|-|-|-|-|-|-|
| Cost effectiveness | 5 | 0 | 5 | 5 |5 | 
| Robustness | 5 | - | 8 | 8 |10 | 
| Insulation | 7.6 | - | 10 | 10 |10 | 
| Temp Prediction Veracity | 10 | - | 10 | 10 |6 | 
| Modularity | 6 | - | 6 | 6 |10 | 
| **Overall KPI /1000** | **11.4** | - | **24** | **24** | **30** |


<br />


<img width="330" alt="Screenshot 2024-06-04 at 10 44 39" src="https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98609386/d133f17e-0e13-45d1-b63c-70eb4346e0cb">

<img width="339" alt="Screenshot 2024-06-04 at 10 47 37" src="https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98609386/d9a9a7b7-a551-46d5-ad39-c126b3f9e75e">

<img width="330" alt="Screenshot 2024-06-04 at 10 49 19" src="https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98609386/4b986d9e-1efa-4eb6-bb1d-3931d1883591">



Hence, the design taken forward is candidate 5, with a specific focus on improving/validating its performance in the 'temperature prediction veracity' dimension, and ensuring that its cost effectiveness, robustness, insulation and modularity are upheld, as it is selected for its good performance across these dimensions. 


<br />
<br />
