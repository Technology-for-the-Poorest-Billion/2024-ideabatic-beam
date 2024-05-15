# Romeo's minutes
-	Focus on making sure the temperature sensing function works really well.
-	Electronics: simple, easy to understand and reliable. Focus on simplicity: for screen simply display: OK or NOT OK, then upon further click display the remaining cool life in hours?
-	Freedom to choose what is included in the actual display.
-	Worth surveying people: blind trialling?
-	Once the above is done well, then detect if the door is open and adjust algorithm accordingly.
-	Focus on the user side, ease of access and simplicity.
-	Modular electronics, within its own casing to clip onto the door element, instead of having separate elements -- difficult installation to be avoided.
-	Idea is to have the battery easily removed (presumably along with the screen for charging?
-	GPS and data logging are more of a nice to have but probably relatively easy to implement.
-	Rechargeable batteries are preferred over standard replaceable batteries.
-	When designing handles, avoid deeper that will occupy space that could have been used for insulation.
-	Smaller LCD preferred over larger – can look towards which size might be ideal for getting across the information. Look into how necessary buttons are.
-	Wider and thinner designs preferred over deeper (again for insulation)
-	Waterproofing nice to have but prioritise design.
-	Make current handle less wide? Look into more prototyping.
-	Documentation should have more information on how you got to the final design – this holds important information for future designers – especially why things didn’t quite work. Might be good to have backups of the prior iterative designs.
-	Think about drops – how might we protect the screen? Slightly deeper than surrounding area.
-	Think about the modularity – how easy is this to do. Clips to have the “screen module” attach to the door? Ideally have the battery and screen/sensor/microcontroller etc all in one module that then attaches, research required to look into best way of implementing this – using magnets instead of clips would be interesting, but depending on mass of module may not be powerful enough.
-	Outside sensor mainly used for remaining cool life, inner for backup/monitoring (?)
-	Private GitHub preferred, WhatsApp questions – maybe even make a shared drive to share things?
-	20C probably best for testing/modelling: https://drive.google.com/drive/folders/15KfUTUK4o-9_mfXlAF1HeKQmgM5Zm7Bo & https://drive.google.com/drive/folders/13nn9-MJRJQJbd6YWNrIXZLQqjzbAK4W1 

# Ness's minutes
wrt CASING:
- electronics module casing, modular, click-on mechanism onto door design
- removable from the top for charging, without disturbing temperature sensor
- more spread out design of casing rather than deep so insulation thickness is not as affected
- depends on electronics components
- waterproofing not the most important but could consider

wrt DOOR:
- could reference previous year designs of self closing door (20C)
- advice: print and test and iterate hardware
- in final report, show how you got to a final design and describe why other designs are problematic in trials 
- investigate torsion springs and other aspects of door, especially ergonomics for finger grip
- a hole in the top for module, should not go over the door top plane, to prevent damage in case of dropping
- minimal parts, want top to be planar with the frame of the chamber
- modular door so that electronics module could be installed

integration wth ELECTRONICS:
- in case of jams, signal or alert to users?
- temperature sensor with a connector with pins (like a charging port), and an electronics module with a matching connector
- find quality off the shelf connectors, but consider strength of spring for self closing design
