# Romeo's role:
Predominantly focussed on the physical aspect of the electronics module. This includes interfacing the electronics with each other, along with finding the best way to implement the electronics module that best preserves insulation. 
<br> Will also be dealing with the software implementation.

# Personal and technical development
- Personal knowledge of all the parts and researched how best to combine them.
- Getting used to developing with the Pi Pico via Thonny.
- Improving logic and coding ability regarding software.
- Will have to learn how to appropriately deal with the button inputs, will do this via interrupts.


# Tasks completed
- Sent order for the electronic components required; ETA Tuesday 28/05.
  - This included the following: Raspberry Pi Pico, DHT22 temperature sensor, an OLED screen, buttons, and an AA battery holder, among other components for testing.
- Brainstormed different ideas with Benjamin to narrow down different designs to detect the door being open/closed.
- Very rough software draft made, but will require testing to determine and overcome hurdles.
<br>



# Main tasks remaining:
- Order any further parts required when possible.
- Combine the electronics into an "electronics module", working with Ness to build a case via 3D printing. 
- Designing a way to interface the electronics module with the internal temperature sensor. Current method is to use a pair of male/female headers to connect the module to the internal temperature sensor.
  - Using a bluetooth temperature sensor that is embedded among the vials is a possible solution, albeit expensive and possibly complicated.
- Trialling methods of detecting the door state.
- Decide the best cable routing method.
- Reconciling the code the team last year had with our prototype.
  - Converting the code to python for better function with Pico.

### Notes to tackle:
**Water resistance:** Electronics module prototype won't be water resistant, which could be especially difficult noting that the module would involve a screen, buttons, a USB port for charging, and potentially a micro SD card slot, though for this we consider having everything only accessible inside the casing. 
<br> This is a conceptual prototype, and the external case/backpack is highly water resistant, so even as a protoype we don't see this becoming an issue.

# Issues
All work done has been theoretical, so the main issues that have arisen have been compatibility issues. 
<br> The main problem we are currently facing is deciding which paths we wish to explore and which aren't worth exploring, especially considering the limited time we have left. To best tackle this, we have looked at each choice, expanded upon them in detail looking specifically at usability and cost, and explored them as best we can to see which will be most fruitful in our case.

## Methods of detecting the door state
- Button switch that is pressed when the door is closed, as the last years team. 
  - Will need to be mounted at the edge of the door.
  - Faces issues with cable routing.
<img height="250" alt="Screenshot 2024-05-27 132004" src="https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/99049952/74f72f82-4954-45d3-bcd5-5df57296b694">
<img height="250" alt="Screenshot 2024-05-27 132004" src="https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/99049952/40ec579b-b10c-4ebe-8ec4-fc389b64f768">
<br>



- An open circuit that is shut when the door closes, likely done through two open contacts that conduct via a plate when the door is shut.
  - Will potentially have issues with corrosion/lifetime as exposed with the door.
  - Faces issues with cable routing.
<img height="250" alt="image" src="https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/99049952/8752d163-084f-4c26-98f7-afc65ecb1e2b">


- Software based method: If we do use two temperature sensors, we can measure the internal temperature sensor, comparing this with the external temperature sensor to detect whether the door is open.
  - Doesn't require further cable routing.
  - Based on two temperature sensors, which may not be included in the final design.
  - Will face issues with the door being partially open, for example being propped open by a pen, though if there isn't significant heat loss transfer from internal temperature sensor this may not be an issue.
  - Accuracy will likely face issues when it comes to the end of the cooling time. 
- Distance/proximity sensors, such as the ultrasonic sensors used in the IDP project in IB.
  - Can be found for cheap (£2).
  - Often have minimum ranges of 2cm+ which will compromise insulation, but this could possibly be leveraged to our advantage.
  - Can be bulky.
- Issue with cable routing.
- Photo Interrupter Sensor, which detects when an infrared beam between a transmitter and receiver is blocked.
  - Relatively cheap (£3.90).
  - Would need to be mounted onto the edge of the door, with a corresponding part required to block the beam.
  - Issue with cable routing.
 

## Mounting the electronics module
The plan is to have these connectors, the male side attached to the module, with the female side attached to the door, allowing plug and play capability. <br>
<img height="250" alt="Screenshot 2024-05-27 132004" src="https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/99049952/6cb9c6e1-60c8-4e93-8ad9-ac7a6c964117">

## Methods of internal cable routing for the internal temperature sensor/other internal components
See Benjamin's work






