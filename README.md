# Mips32-lite-simulator
Mips32-lite-simulator In this project, I designed a MIPS 32 lite simulator with two modes- Forwarding and Non-Forwarding. The project simulates a 5-stage pipeline programmed in Python programming language. The simulator takes an instruction trace as input and outputs different statistics as shown below:
1) Program counter, Memory and Register states: All the memory states that changed during the run of instruction trace
2) Instruction Stats- i) No. of instructions ii) No. of Arithmetic instructions iii) No. of Logic instructions iv) No. of Memory instructions v) No. of Control instructions
3) Timing Stats - i) Number of cycles required ii) Number of average stalls required iii) Total stalls iv) Number of hazards occurred

The program has a "Debug" mode which allows the user to visualize the instructions moving through the pipeline. Since the program is object oriented it can be used to simulate a multi-processor system.
