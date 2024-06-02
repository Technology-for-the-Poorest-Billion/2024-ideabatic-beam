Inkeeping with the conservative analysis principles outlined (**insert hyperlink here**), 
an analysis of the feasibility of the DHT being kept inside the module housing was carried out. 


<ins>The Problem to be Solved</ins>

Heat will be dissipated by the electronics module (powered by two AA batteries).

Will this heat cause the temperature inside the module to be significantly different from the actual temperature outside the door?



<ins>Conservative Analysis Assumptions</ins>

1) All of the power consumed by the circuit is produced as heat
2) The internal resistance of the batteries used is at the lower end of the [average range for AA batteries](https://www.researchgate.net/figure/Average-internal-resistance-of-AA-batteries_tbl2_379429848), as this gives the highest heat production.
3) The 'load' (the circuit supplied by the batteries) satisfies the maximum power transfer theorem, as this gives the highest heat production.
4) Convective heat transfer out of the module casing is neglected; all heat transfer is assumed to be conductive




<ins>The Analysis</ins>

Maximum Power Transfer Theorem: 

Resistance of Load = Internal Resistance of Batteries

Two AA batteries$\implies$ R<sub>in,total</sub> = 2 R<sub>in,single battery</sub>

R<sub>L</sub> = R<sub>in,total</sub>

$\implies {R_{total}}$ = 

$\{P_{total}} = \frac{V^2}{\{R_{total}}}$

$\implies$ 

For super-and sub-scripts: a<sub>1</sub> = 12 ms<sup>-2</sup>.

You can also include formulae in LaTeX syntax: $\alpha=\frac{1}{\sqrt{2}}$.
