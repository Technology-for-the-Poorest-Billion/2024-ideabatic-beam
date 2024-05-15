# Problem description

- Brief overview of the problem, context and engineering approach to tackle the problem.

## The problem
Current vaccine carriers use cooler boxes which are poorly adapted to the conditions that they are expected to tackle. They often have very poor cooling lifetimes that can mean the vaccine spoils before it reaches it's destination. In field conditions, lasting about 4 hours which is simply not enough as journeys can often last up to 2 days in 25(?)+ C heat. SMILE, by Ideabatic aims to combat this issue with a unique designed cooler box with a single ice pack that can last up to 4 days (120 hours). 
Can talk about requiring 4 ice packs, but only 1 is used? 


# Presentation of the proposal

#### Technical aspects may be described here.

The proposal can be split into two main tasks: Electronic and mechanical. There is a lot more versatility within the electronic task, allowing it to be split further into multiple different subtasks, whilst mechanical has one main concern that is to be tackled, albeit in many different ways, and is rather open ended.
## Electronic:
The main addition that Ideabatic is looking to implement is a functioning, modular and accurate temperature sensing display. The team last year did this through an Arduino, though other avenues are currently being explored, such as a raspberry pi pico. The hope is to have a user-friendly interface that will display whether the vaccines are within the safe temperature range and, upon further interaction, how many hours the vaccines will likely last under the current temperature conditions. There is also the possibility of adding a GPS sensor to locate the cooler and then log this, along with the temperature sensing data, in a storage device that can later be accessed. This should all be incorporated in some module which can be removed and fit when necessary, leading to some intricacies within the actual door design.


Also within the electronic topic is the improvement of the temperature sensing algorithm. Right now, the function works by (INSERT HOW IT WORKS HERE) and incrementally reducing the cool life. It does not currently consider how the door opening will affect the remaining cool life which is something that we are looking to add. 
(There is also the work last years team has done to detect when the door is closed and beep after half a minute of open door. Needs to be investigated) 
## Mechanical

# Assessment of the quality of the proposal

Evaluate its value in the context of the project. What will it solve, is it safe, etc. Check Lara’s slides for what to cover.


