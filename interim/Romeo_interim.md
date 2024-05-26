# Romeo's role:
Predominantly focussed on the physical aspect of the electronics module, along with dealing with the implementation of the software.

## Tasks completed (?)
- Sent order for the electronic components required; ETA Tuesday 28/05.
- Brainstormed different ideas with Benjamin to narrow down different designs to detect the door being open/closed that least compromises the insulation.
  - Button switch that is pressed when the door is closed, as the last years team. (CAN INCLUDE PICTURE?)
    - Will need to be mounted at the edge of the door.
    - Faces issues with cable routing.
  - An open circuit that is shut when the door closes, likely done through two open contacts that conduct via a plate when the door is shut (CAN INCLUDE PICTURE?)
    - Will potentially have issues with corrosion/lifetime as exposed with the door.
    - Faces issues with cable routing.
  - Software based method: If we do use two temperature sensors, we can measure the internal temperature sensor, comparing this with the external temperature sensor to detect whether the door is open
    - Doesn't require further cable routing.
    - Based on two temperature sensors, which may not be included in the final design.
    - Will face issues with the door being partially open, for example being propped open by a pen, though if there isn't significant heat loss transfer from internal temperature sensor this may not be an issue.
    - Accuracy will likely face issues when it comes to the end of the cooling time. 
  - Distance/proximity sensors, such as the ultrasonic sensors used in the IDP project in IB.
    - Can be found for cheap (£2)
    - Often have minimum ranges of 2cm+ which will compromise insulation, but this could possibly be leveraged to our advantage.
    - Can be bulky
    - Issue with cable routing
  - Photo Interrupter Sensor, which detects when an infrared beam between a transmitter and receiver is blocked
    - Relatively cheap (£3.90)
    - Would need to be mounted onto the edge of the door, with a corresponding part required to block the beam.
    - Issue with cable routing

## Main tasks remaining:
- Combine the electronics into an "electronics module", working with Ness to build a case via 3D printing. 

- Designing a way to interface the electronics module with the internal temperature sensor. Current method is to use a pair of male/female headers to connect the module to the internal temperature sensor, with the following routing ideas:
  - Wire that leads from the module connector to the temperature sensor, see Benjamin's work.
  - Route wiring through the surface of the door, using the hinge as an electrical connection.
- Trialling methods of detecting the door state.
- Reconciling the code the team last year had with our prototype
  - Converting the code to python for better function with Pico.
- 



Notes to tackle:
<br> Water resistance: Electronics module prototype likely won't be water resistant, which could be especially different noting that the module would involve a screen, buttons, a USB port for charging, and potentially a micro SD card slot, though for this we consider having this only accessible inside the casing. 
<br> This is a conceptual prototype, and the external case is highly water resistant.
