## Benjamin

### Stage 1: Overall Design

#### Possiblilities considered for overall design:
- The five candidates shown
- Feasibility assessments and spider diagram ranking of each one; justify pursuing the uni-modular design, with a specific focus on improving the environmental resistance
- Single mode design also has the disadvantage of having no information about when the ice packs have just been put in.
- Need a manual 'reset cool lifetime' button. What if they forget to press button? What if they accidentally press it?
- Put the button on the bottom of the module to be automatically pressed when module reloaded: difficulties with each method, this is another user problem to be solved. 


### Stage 3: Solving the temperature sensor problem
- Compare the two designs for temperature sensor: external, waterproof sensor (cost and mounting issues) vs internal DHT22 (innacurate temperature issue - back up with conductivity requirement, cost)
- upper limit heat corrpution effects: heat power = electronic power for batteries and display
- Output: the minimum surface area that needs to be made with conductive material, show that it is within budget + the area with 


### Stage 4: Solving the door switch and button problem

- Considered cutting out a large region, inserting module to fill the gap, but this compromises water resistance when module removed (either by leaving water seal intact but providing a parallel path straight through, or but taking out a chunk of the water seal)
- Also considered mounting entire module on the top of the door (could do a mechanical impulse analysis) but makes it less drop-resistant (module breaks off) and requires outside ridge of box to be raised so that button can still be pressed, also probably a less secure clipping mechanism if not indenting into door
- Final prototype solution (copy in conceptual drawing): top of module slightly indented so it goes flush with top of button arm, with is entirely on top of door so as not to compromise water seal + Plastic boxes to make entire things rectangular, giving better mechanical robustness
+ Cylinders with hemispherical ends at each corner to give drop protection
- Means that when module is removed, the door is still fully functional and has minimal compromise to its insulation (calculation supporting)

<br />
  
- Going to need a way of waterproofing buttons: solid casing + rubbery button topper to prevent water ingress. 
- Considered possibility of an auto-press button for resetting the timer (see above)

<br />

- Feasability assessments and rankings, clearly communicating design decisions

<br />

- eliminate all alternative designs on feasibility grounds
- make the compartment out of three things: cheap, clear, conductive. 
- material selection (conductivity, heat resistance, cost)
- graphene may not be a mature material in 3D printing technology
- manufacturing complexity
- rough sketch of preferred design

<br />

- Need manual button to reset cool life: where to put button? Difficult to access place - maybe aturomatically pressed when module clipped back on, solves water resistance (lifetime of button?)


## Romeo
- Calculate expected power consumption of electronics module, justifying choice of battery (cost, recharge/overcharge?). PASS POWER CONSUMPTION DATA TO BENJAMIN.
- How long are AA batteries expected to last? Is the electronics module always on?
- Assemble electronics module (screen working/updating + switch informing buzzer) and test. PASS DIMENSIONS OF MODULE TO NESS. 
- Getting it working with Code 
- Mount it into correct shape (collb w Ness)




## Ness
- Cad model of the actual case, including a see-through compartment and a conductive compartment, ready to be 3D-printed.  (Romeo tells dimensions after assembling circuit)
- Cad model of the door that is receptive to the case being clipped on (choose and justify clipping mechanism)
- Outline file compatibility issues between OpenSCAD and SolidWorks
- 3D print and assemble door + case of electronics module (collaborate w Romeo): *Working prototype*
- Suggestion of how the different materials can be joined together (eg the see-through section of the case, the main body of the case and the heat-conductive section of the case) (talk to Romeo about this)
