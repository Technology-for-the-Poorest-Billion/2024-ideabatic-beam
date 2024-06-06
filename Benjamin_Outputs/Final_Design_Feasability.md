## Validating Analysis of the Final Design across all dimensions


### Modularity: 
- entirely electronically and mechanically modular for easy charging and opt-in 



### Robustness: 
- With the existing sealing not being compromised, water resistance remains
- With the [mechanical solutions implemented](https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/blob/main/mechanical%20design/handover%20notes/drop%20resistance.md), the final product is drop resistant



### Temeprature Prediction Veracity: 
- 1º overestimate proven to be sufficiently accurate

<img width="671" alt="Screenshot 2024-06-06 at 14 01 27" src="https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98609386/2c56ec1e-dc93-4ba6-8c1a-76ee717190f9">


### Cost effectiveness: Validating Analysis
- Take the [worst-case quantity discounting for electronic components](https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/blob/main/Benjamin_Outputs/Initial_Design_Candidates.md)
- Add the single-unit cost of all materials used for housing, assuming no quantity discounting


Material costs:
- 0.9mm thick x 9080mm2 for [aluminium sheet](https://www.metals4u.co.uk/materials/aluminium/aluminium-sheet/aluminium-mill-finish-aluminium-sheet/3123-p?ppm=false&gad_source=1&gclid=Cj0KCQjw9vqyBhCKARIsAIIcLMEcxx1h4nVGUAGYFfs54U9BD60yTGIhoN8M_dy8MsmMGdnNYN7KQmIaAjlwEALw_wcB) for top of module casing
£0.22 for 0.01m2
- 30x14 of [2mm thick acrylic](https://www.perspexsheet.uk/clear-000-perspex/?gad_source=1&gclid=Cj0KCQjw9vqyBhCKARIsAIIcLMEZ89-n_Y2YTYkYBV_6rXlRbnBh4ZYir4bu5BmR-Uv2fd5JJoKAz8saAuZmEALw_wcB) for screen display on top of module case: £0.02 per unit
- 13226.4mm3 of [ABS](https://www.plasticsdirect.co.uk/products/abs-sheet-acrylonitrile-butadiene-styrene), costs £1.37/kg; density is 1 g/cm3, so we are using 13.2264g, so material cost is £0.02; if we want it pre-processed, £0.31.
- two [PVC button covers](
https://undercontrol.co.uk/accessories/switches/pvc-splash-resistant-rocker-switch-cover/), £0.24 each


So only adds £1.03 to material costs.

<br />

Detailed research, including further input from the project partner to quantify the additional manufacturing costs is necessary for a complete analysis, but the original £15 in the [problem definition](https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/blob/main/Benjamin_Outputs/Our_Design_Problem_and_Context.md) was not expected to include manufacturing.


<br />

Hence, the final prototype is costed at £12.02 (electronics) + £1.03 = £13.05 in the worst case. So we remain under budget!


### Insulation: Validating Analysis


*This uses a different model: split the total thermal resistance of ABS into two parts: the insulation in door face and the insulation in all other faces. Then the thermal resistance in door face is reduced by a factor of (62-7)/55, which represents the percentage decrease in thickness; conservatively assuming that air in parallel with insulating material is as bad as just air in the top 7mm of the door*


<img width="140" alt="Screenshot 2024-06-06 at 13 28 40" src="https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98609386/b5f65d59-4d4a-4667-abcb-a47fccc529c8">


Plugging the value for the total thermal resistance of the device into the cool life prediction algorithm, 

<img width="357" alt="Screenshot 2024-06-06 at 15 41 29" src="https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98609386/f64d8208-62f2-4cd0-8fb6-4973d84b2a0c">

It is shown that the new device maintains 96% of the original cool lifetime, scoring an 8.98 on the insulation dimension according to its dimension characteristic.

<br />

All five key dimension requirements are satisfied; a new KPI can be computed based on the slightly reduced insulation, at KPI/1000 = 27. Hence this still remains the best design candidate, and is proven to be a working prototype design. 

The next step is to build the actual product out of the recommended materials. 
