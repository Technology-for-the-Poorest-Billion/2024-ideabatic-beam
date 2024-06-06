## Prototyping insights

### 1. CAD design medium

The project was originally planned to be done on OpenSCAD due to the following advantages:
1. Modular programme code
2. Increase accessibility for future design modifications by project groups

![Screen Shot 2024-06-06 at 15 18 48](https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98922660/72d85894-64f0-4542-b7e8-3005bf76e971)
Figure: Assembled OpenSCAD model of SMILE shell.

However, I faced different limitations:
1. [Most important] Original SMILE design files were on Solidwork, compatibility issues as imported .STL files cannot be modified
2. Not able to directly orient or locate .STL files in OpenSCAD
3. Difficult to assemble components, need to constantly refer back to original Solidworks file
4. Axes are sparse and imprecise, no grid visualisation
5. [Less important] Not as visually intuitive as Solidworks, required time to get used to

As the limitations outweight the advantages, this led me to not pursue OpenSCAD as the final design medium. The designs were done using Solidworks.

### 2. 3D printing

List of problems faced using RS 3D printers:
1. Poor tolerance, components do not fit together well
2. Rounded surfaces do not print well
3. Supports require a lot of manual effort and time to remove, hinders rapid prototyping
4. Imperfect removal of supports cause problems in joining interfaces

Higher quality printers (Ultimaker) were occupied by other groups, prioritise using those printers if future project groups are to prototype. Benefits include:
1. No raft support. Raft supports were the most difficult to remove.

![IMG_9136](https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98922660/fcc74617-f9e8-4311-9b0e-8878ca8191db)

