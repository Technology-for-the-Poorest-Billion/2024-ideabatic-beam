# Problem description

- Brief overview of the problem, context and engineering approach to tackle the problem.

## The problem
Current vaccine carriers use cooler boxes which are poorly adapted to the conditions that they are expected to tackle. They often have very poor cooling lifetimes that can mean the vaccine spoils before it reaches its destination. They were shown to last about 4 hours in field conditions, which is simply not enough as journeys can often last up to 2 days in over 25ºC heat. Human error is also a large problem, as healthcare workers may leave cooler boxes open for hours, significantly reducing its cooling lifetime. SMILE, by Ideabatic, aims to combat this issue with a uniquely designed cooler box containing only a single ice pack that can last up to 4 days (120 hours), compared to usual cooler boxes that need four, along with a self-closing door mechanism to reduce human error.

# Presentation of the proposal

#### Technical aspects may be described here.

The proposal can be split into two main tasks: Electronic and mechanical. There is a lot more versatility within the electronic task, allowing it to be split further into multiple different subtasks, whilst mechanical has one main concern that is to be tackled, albeit in many different ways, and is rather open ended.
## Electronics
The main addition that Ideabatic is looking to implement is a functioning, modular and accurate temperature sensing display. The team last year did this through an Arduino, though other avenues are currently being explored, such as a raspberry pi pico. The hope is to have a user-friendly interface that will display whether the vaccines are within the safe temperature range and, upon further interaction, how many hours the vaccines will likely last under the current temperature conditions. There is also the possibility of adding a GPS sensor to locate the cooler and then log this, along with the temperature sensing data, in a storage device that can later be accessed. This should all be incorporated in some module which can be removed and fit when necessary, leading to some intricacies within the actual door design.


Also within the electronic topic is the improvement of the temperature sensing algorithm. Right now, the function works by (INSERT HOW IT WORKS HERE) and incrementally reducing the cool life. It does not currently consider how the door opening will affect the remaining cool life which is something that we are looking to add. 
(There is also the work last years team has done to detect when the door is closed and beep after half a minute of open door. Needs to be investigated) 

## Mechanical
The mechanical component involves designing a compatible “snap-fit” electronics module housing and door slot design, as well as improving on previous iterations of the ergonomics and robustness of the self-closing door mechanism.


OpenSCAD would ideally be used for the individual designs of the electronics module housing, door slot, internal placement of sensors, and spring mechanism. 3D printing would then be used to test and redesign components iteratively. Important features of the improved design is its resistance to damage in case of dropping, as well as containing minimal parts for easy manufacturing. The thickness of the electronics module and casing is also important to consider such that insulation thickness at the door is not significantly affected. Stress and life cycle analysis of the torsional spring may be investigated to check robustness. Additional aspects such as waterproofing may be explored. The outcome should be a modular, integrated electronics casing and door system with improved ergonomics and mechanism robustness.


# Assessment of the quality of the proposal

Evaluate its value in the context of the project. What will it solve, is it safe, etc. Check Lara’s slides for what to cover.


