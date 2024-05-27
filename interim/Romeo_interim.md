# Romeo's role:
Predominantly focussed on the physical aspect of the electronics module. This includes interfacing the electronics with each other, along with finding the best way to implement the electronics module that best preserves insulation. Will also be dealing with the software implementation.


# Personal and technical development





# Tasks completed
- Sent order for the electronic components required; ETA Tuesday 28/05.
  - This included the following: Raspberry Pi Pico, DHT22 temperature sensor, an OLED screen, buttons, and an AA battery holder, among other components for testing.
- Brainstormed different ideas with Benjamin to narrow down different designs to detect the door being open/closed.
- Rough software draft made, but will require testing to determine hurdles.

# Main tasks remaining:
- Combine the electronics into an "electronics module", working with Ness to build a case via 3D printing. 
- Designing a way to interface the electronics module with the internal temperature sensor. Current method is to use a pair of male/female headers to connect the module to the internal temperature sensor.
  - Using a bluetooth temperature sensor that is embedded among the vials is a possible solution, albeit expensive and possibly complicated.
- Trialling methods of detecting the door state.
- Decide the best cable routing method.
- Reconciling the code the team last year had with our prototype
  - Converting the code to python for better function with Pico.

# Issues
All work done has been theoretical, so the main issues that have arisen have been compatibility issues. 
<br> The main problem we are currently facing is deciding which paths we wish to explore and which aren't worth exploring, especially considering the limited time we have left. To best tackle this, we have looked at each and explored them as best we can to see which will be most fruitful in our case.

## Methods of detecting the door state
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


## Methods of internal cable routing for the internal temperature sensor/other internal components
- Wire that leads from the module connector to the temperature sensor, see Benjamin's work.
- Route wiring through the surface of the door, using the hinge as an electrical connection, as it is accessible from the outer and inner surfaces.

# Project Timeline
Our project is mostly on track, though we have required the extra time originally scheduled. From the electronics side, it has taken longer than we expected to get an order in and receive the parts. 


Notes to tackle:
<br> Water resistance: Electronics module prototype likely won't be water resistant, which could be especially different noting that the module would involve a screen, buttons, a USB port for charging, and potentially a micro SD card slot, though for this we consider having this only accessible inside the casing. 
<br> This is a conceptual prototype, and the external case is highly water resistant.


