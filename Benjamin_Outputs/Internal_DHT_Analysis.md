Inkeeping with the conservative analysis principles outlined (**insert hyperlink here**), 
an analysis of the feasibility of the DHT being kept inside the module housing was carried out. 


<ins>The Problem to be Solved</ins>

- Our general design is Candidate 5, which integrates the temperature sensor into the electronics module. Heat will be dissipated by the electronics module (powered by two AA batteries).

<br />

Will this heat cause the temperature inside the module to be significantly different from the actual temperature outside the door?

<br />

<ins>Validating Analysis: Worst-Case Assumptions</ins>

1) All of the power consumed by the circuit is produced as heat
2) The internal resistance of the batteries used is at the lower end of the [average range for AA batteries](https://www.researchgate.net/figure/Average-internal-resistance-of-AA-batteries_tbl2_379429848), as this gives the highest heat production.
3) The 'load' (the circuit supplied by the batteries) satisfies the maximum power transfer theorem, as this gives the highest heat production.
4) Convective heat transfer out of the module casing is neglected; only conductive heat transfer is analysed

<br />

<img width="200" alt="Screenshot 2024-06-06 at 15 11 28" src="https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98609386/f23619df-4828-4ee3-bd9b-254a9fe6db3e">

#### [Figure 1](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.geeksforgeeks.org%2Fmaximum-power-transfer-theorem%2F&psig=AOvVaw2DwCYf4Gm9FaJ-gqkSTDGT&ust=1717769472212000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCKCHpouUx4YDFQAAAAAdAAAAABAE): Maximum Power Transfer Theorem

<br />

<ins>The Analysis</ins>

<ins>Maximum Heat Power Produced</ins>

Two AA batteries

$\implies {R_{in,total}}$ = $\{2R_{in,single}}$

Maximum Power Transfer Theorem: Resistance of Load = Internal Resistance of Batteries


$\implies {R_{L}}$ = $\{R_{in,total}}$

$\implies {R_{total}}$ = $\{2R_{in,total}}$ = $\{4R_{in,single}}$

$\{P_{total}} = \frac{V^2}{\{R_{total}}} = \frac{V^2}{\{4R_{in,single}}}$

Maximum Total Voltage = 3V (1.5V per battery); Minimum $\{R_{in,single}}$ = 0.19 Ω

$\implies$ $\{P_{total}} = \frac{3^2}{\{4\times0.19}} =$ 11.84 W

<ins>Heat Conducted Away</ins>

<br />

- In order for heat produced inside the electronics module to be conducted away, it is physically necessary for the temperature inside the module to exceed the actual external temperature. 

- Allow the temperature inside the module casing to exceed external temperature by 1ºC (∆T=1).

#### Check that the cool life prediciton is not drastically affected by a 1ºC overestimate in the ambient temperature:

- Plugging into the [temperature prediction algorithm](https://colab.research.google.com/drive/1pOM9zMMuzmkzLNehpk7Lr7O0WtXEk16u?authuser=1#scrollTo=-TuyIuoOHyXr), the effect is quantified:

<img width="426" alt="Screenshot 2024-06-06 at 15 16 24" src="https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98609386/330470d3-9019-4dde-8927-4d99c566bf1d">

#### Figure 2: Overestimate in ambient temperature results in only a 4% underestimate in cool lifetime (acceptable)

<br />
<br />

#### For a 1ºC maximum overestimate:

$\dot{Q} = \frac{∆T}{\{R_{th}}}$

To conduct away enough heat to remain in the acceptable range, $\dot{Q} \ge$ Heat produced $=$ 11.84 W

$\implies {R_{th}} = \frac{l}{\lambda\times{A}} \le \frac{1}{\{11.84}}$ = 0.084 KW<sup>-1</sup>

$\lambda_{aluminium}$ = 237 Wm<sup>-1</sup>K<sup>-1</sup>

$\implies$ For an aluminium casing, $\frac{l}{\{A}} \le 237\times{0.084} =$ 19.9 m<sup>-1</sup>


If any part of the module casing is made with aluminium which meets this aspect ratio, then any other sections (eg the transparent section for screen viewing) can be modelled as parallel resistive components in the heat analysis, only further improving the cooling capability of the casing. Thus manufacturing the casing with a section of aluminium meeting the aspect ratio required is sufficient to ensure that the temperature measured remains within the acceptable range. 

Aluminium thermal conductivity:

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10144406/#:~:text=Aluminum%20has%20a%20thermal%20conductivity,1%2C2%2C3%5D.

Cost of aluminium sheeting:

https://www.aluminiumwarehouse.co.uk/products/1-5-mm-5251-h22-aluminium-sheet?variant=42412383240380&utm_source=google&utm_medium=organic&utm_campaign=UK%20-%20Aluminium%20Warehouse&utm_content=1.5%20mm%20-%205251%20H22%20-%20Aluminium%20Sheet¤cy=GBP&utm_source=google&utm_medium=cpc&utm_campaign=Pmax%20tier%201%20-%20others&utm_id=20993447663&utm_term=&gad_source=1&gclid=Cj0KCQjwsPCyBhD4ARIsAPaaRf3k0eqC-FZWQaHwsebMHXSQ9EdVMUEPBOZF0SQjGx6mZrish0z4w_8aAsqzEALw_wcB

