## Main objectives
- Modularised electronics: create a compatible casing and slot.
- Improve ergonomics: lip of lid and torsional spring parameters.
- Transfer of models to open source CAD: increase accessibility for future design modifications.

## Design considerations
- Slot for connector and temperature sensor on door.
- Soft ridge around electronics module slot (preliminary OpenSCAD design shown with hard ridge).
![Screen Shot 2024-05-27 at 12 49 04](https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98922660/230af53f-4ea0-40a9-ad0e-0e69329a3fb9)
- Ridges on component interfaces to facilitate joining and compatability.

## Tasks completed
- Learned basic skills in OpenSCAD and exporting .STL files.
- Preliminary design of electronics module casing on OpenSCAD ready for future compatibility adjustments.
![Screen Shot 2024-05-27 at 12 02 42](https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98922660/e13515fc-5577-4896-a343-caf2d73fa6c8)
- Transfer of SMILE design files into OpenSCAD (chassis, casing and door) and assemble components.
![Screen Shot 2024-05-27 at 12 08 57](https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98922660/0c5be530-7ee1-4a42-ad3c-5d66ba3289ef)
- Edits of door design on Solidworks (connector placement, temperature sensor slot).
- Compiled literature on door ergonomics design.

## Issues faced and solutions
Understanding OpenSCAD syntax:
- Simple but required time to get used to and not as intuitive as Solidworks.
- Consult online forums and wiki.

Assembling components:
- Difficult to assemble components, need to constantly refer back to Solidworks file to check how they fit.
- Scales on OpenSCAD are not precise, dimensions of downloaded .STL models are not well defined.
- Used online .STL measurement tools to obtain precise measurements.
![Screen Shot 2024-05-27 at 13 17 05](https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98922660/6fac668d-58c6-40d3-876e-c00197562814)

Limitations with editing .STL files:
- Using difference/intersection commands to edit .STL imported files becomes rather buggy.
- Unable to edit directly on OpenSCAD, therefore instead modifying door using Solidworks as modelling a new door in OpenSCAD is too difficult.
- Download as .STL to interface with other components in OpenSCAD.

## Next steps
- Adding ridges to the casing/casing cap and casing bottom/door slot interfaces to facilitate joiningof components.

![plastic-to-metal-300x268](https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98922660/fa2993a0-f6a4-4fce-9b40-bad383336df5)
- Finish first door lip design modification on Solidworks.
- 3D print door to start testing ergonomics.
- Once electronics team has a model of the electronics components, edit the casing and door hole dimensions.
- 3D print new door top and casing.

## Personal and technical developments
- Practiced using OpenSCad and interfacing with Solidworks through .STL files.
- Github documentation of OpenSCAD code.
- Learned design strategies for in field use (preventing drop damage).

Next:
- 3D printing.
