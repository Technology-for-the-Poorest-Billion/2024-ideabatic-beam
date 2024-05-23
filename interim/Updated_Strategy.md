Focus on incremental improvement, building on what the previous team has done. 

# Primary goal: Make the electronics modular, minimising the compromise to insulation. 

Strategy:

1) State the design problem/constraints:
   
   (i)  why we need internal and external temperature sensors,

   (ii) why they need to be connected (why wireless connection isn't feasible),
   
   (iii) why it needs to be modular (minimise insulation - metal connections naturally oppose this objective, easy charging)

   (iv) why it needs to be thin (for usability, damage prevention - helped by ridges around module)
   
   (v) why we need an open-closed sensor in door and beep
  
2) Obtain design possibilities

- Brainstorm various ways to achieve the electrical connections required
- Eliminate some possibilities for feasability reasons (eg compromises insulaton, ergonomics, including cost, eg for wireless solution). Quantify where possible. Document this process. 
- Finalise some candidates which are worth exploring by prototpying (one, two or three designs)


3) Assemble the electronics as a stand-alone circuit. Just get it working.

4) Build prototype(s). This is the final output. 






# Secondary goals:
Only do these if primary goal is complete.

- MicroSD for datalogger added onto circuit
- Calculation for adapting thermal resistance when door is open, to inform how the temperature-sensing algorithm should be updated when the door sensor tells us the door is open

