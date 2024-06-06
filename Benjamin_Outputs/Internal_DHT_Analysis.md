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
4) Convective heat transfer out of the module casing is neglected; all heat transfer is assumed to be conductive




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

- Allow the temperature inside the module casing to exceed external temperature by 1ºC (∆T=1), *This is asssumed small enough to have a negligible impact on the temperature prediction. Assumption checked in Final_Design_Feasability.md*
- (Error caused by mismatch: Quantify with a plot from Notebook).

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

