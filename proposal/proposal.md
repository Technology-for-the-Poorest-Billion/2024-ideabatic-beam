# Problem description


<!-- Brief overview of the problem, context and engineering approach to tackle the problem.-->

Current vaccine carriers use cooler boxes which are poorly adapted to the conditions that they are expected to tackle, often with very poor cooling lifetimes that can mean vaccines spoil before they reaches their destination. These were shown to last approximately 4 hours in field conditions, which is simply not enough for journeys that can often last 2 days in over 25ºC heat. Human error is also a large problem, as healthcare workers may unknowingly leave cooler boxes open for long periods of time, significantly reducing the cooling lifetime. There is also an issue in which, despite requiring four standard ice packs placed appropriately, workers may end up only using one or two, placed haphazardly. 

SMILE, by Ideabatic, aims to combat this issue with a uniquely designed cooler box containing only a single ice pack that can keep 18 vaccines cool for up to 4 days (120 hours), along with a self-closing door mechanism to reduce human error. The design also incorporates a waterproof casing with further insulation and straps for comfortable carry as a backpack. Clearly responding to a genuine need, the impact of SMILE can be assessed against UN's sustainable development goals. 


# Presentation of the proposal

<!--Technical aspects may be described here--> 

The aim of the proposal is to improve upon the current design in two main areas, electronic and mechanical. There is a lot more versatility within the electronic task, allowing it to be split further into multiple different subtasks, whilst mechanical has one main concern that is to be tackled, albeit in many different ways, and is rather open ended. 

## Electronics
The main electronic addition that Ideabatic is looking to implement is a functioning, modular and accurate temperature sensing display. The team last year did this through an Arduino, though our group is looking to use a Raspberry Pi Pico. The hope is to have a user-friendly interface that will display whether the vaccines are within the safe temperature range and, upon further interaction, how many hours the vaccines stored inside will likely last under the current temperature conditions. There is also the possibility of adding a GPS sensor to locate the cooler and then log this, along with the temperature sensing data, in a storage device that can later be accessed. This should all be incorporated in a module which can be removed and fit as desired, leading to some intricacies within the actual door design. This module will contain a temperature sensor, measuring the ambient temperature, and there will also be a static temperature sensor embedded inside the door. The module will then be able to interact with this sensor when attached to the door. 


Also within the electronic task is the improvement of the temperature sensing algorithm. The current function works by calculating the heat energy lost to the surroundings (treating the thermal resistance and total ice pack energy as constants) and decrementing the cool life accordingly. It does not currently consider how the door opening will affect the remaining cool life which is something that we are looking to add. The team last year has also worked on a system that detects when the door is left open and beeps after a given time. This currently works off of a simple button switch, with some different designs explored, though ultimately more testing needs to be done to figure out how well it worked, or if there are different methods we need to look at.

## Mechanical
The mechanical component involves designing a compatible “snap-fit” electronics module housing and door slot design, as well as improving on previous iterations of the ergonomics and robustness of the self-closing door mechanism.


OpenSCAD would ideally be used for the individual designs of the electronics module housing, door slot, internal placement of sensors, and spring mechanism. 3D printing would then be used to test and redesign components iteratively. Surveys could be done to assess the effectiveness of the design in achieving ergonomics and preferences of users. Some important features to be included in the improved design is resistance to damage in case of dropping, as well as containing minimal parts for easy manufacturing. The thickness of the electronics module and casing is also important to consider such that insulation thickness at the door is not significantly affected. Stress and life cycle analysis of the torsional spring may be investigated to check robustness. Additional aspects such as waterproofing may be explored. The outcome should be a modular, integrated electronics casing and door system with improved ergonomics and mechanism robustness.


# Assessment of the quality of the proposal

<!--Evaluate its value in the context of the project. What will it solve, is it safe, etc. Check Lara’s slides for what to cover.-->


The SMILE coolbox works as it is, and is safe for users. Despite this, it has come up against approval and funding issues. Ideabatic has decided to take the device to developed markets (such as the UK) as a proof of concept, along with the addition of further features which can be included or removed as costs require for developing market applications. 


There are three core improvements to the existing design that we are looking to implement:

The door being self-closing, and/or warning users if left open, has been proven by field tests to be a functional necessity. Due to carelessness, the door is often left open, which leads to unnecessary spoiling of the vaccines. Ergonomics of the door opeartion is essential for ease of use, and must accommodate the varied nature of applications and shapes and sizes of users. 


Implementing a simple display, showing the cool life remaining, or at its simplest, an 'OK' or 'NOT OK' signal, is a high-impact safety feature, which allows the administer of vaccines to be aware when vaccines have spoiled, and when they need to return to restock the icepack. Here, information saves lives. 

The current algorithm for estimating the temperature in each vaccine compartment has been calibrated assuming that the SMILE door is closed at all times. In reality, the door will frequently be opened, especically during an administration session. This leads to much faster cooling rates (extent to be determined), and thus shorter cool lifetimes. To obtain an accurate temperature estimate and make the display worthwhile, the algorithm should thus be improved to include the effect of the open door; preferably coupled with a real-time sensor on the door to indicate its state. 
