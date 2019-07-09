# Mips32-lite-simulator
Mips32-lite-simulator In this project, I designed a MIPS 32 lite simulator with two modes- Forwarding and Non-Forwarding. The project simulates a 5-stage pipeline programmed in Python programming language. The simulator takes an instruction trace as input and outputs different statistics as shown below:
1) Program counter, Memory and Register states: All the memory states that changed during the run of instruction trace
2) Instruction Stats- i) No. of instructions ii) No. of Arithmetic instructions iii) No. of Logic instructions iv) No. of Memory instructions v) No. of Control instructions
3) Timing Stats - i) Number of cycles required ii) Number of average stalls required iii) Total stalls iv) Number of hazards occurred

The program has a "Debug" mode which allows the user to visualize the instructions moving through the pipeline. Since the program is object oriented it can be used to simulate a multi-processor system.
<br>
The details required for generating the trace memory file:<br>
Instruction Set: The simulator is capable of simulating the following instructions:<br>
a. Arithmetic Instructions:<br>
i. ADD Rd Rs Rt (Add the contents of registers Rs and Rt, transfer the result to register
Rd). Opcode: 000000 <br>
ii. ADDI Rt Rs Imm (Add the contents of register Rs to the immediate value “Imm”,
transfer the result to register Rt). Opcode: 000001 <br>
iii. SUB Rd Rs Rt (Subtract the contents of register Rt from Rs, transfer the result to
register Rd). Opcode: 000010 <br>
iv. SUBI Rt Rs Imm (Subtract the immediate value “Imm” from the contents of register Rs,
transfer the result to register Rt). Opcode: 000011 <br>
v. MUL Rd Rs Rt (Multiply the contents of registers Rs and Rt, transfer the result to
register Rd). Opcode: 000100 <br>
vi. MULI Rt Rs Imm (Multiply the contents of registers Rs with the immediate value
“Imm”, transfer the result to register Rt). Opcode: 000101 <br>
b. Logical Instructions <br>
i. OR Rd Rs Rt (Take a bitwise OR of the contents of registers Rs and Rt, transfer the
result to register Rd). Opcode: 000110 <br>
ii. ORI Rt Rs Imm (Take a bitwise OR of the contents of registers Rs and the immediate
value “Imm”, transfer the result to register Rt). Opcode: 000111 <br>
iii. AND Rd Rs Rt (Take a bitwise AND of the contents of registers Rs and Rt, transfer the
result to register Rd). Opcode: 001000 <br>
iv. ANDI Rt Rs Imm (Take a bitwise AND of the contents of registers Rs and the
immediate value “Imm”, transfer the result to register Rt). Opcode: 001001 <br>
v. XOR Rd Rs Rt (Take a bitwise XOR of the contents of registers Rs and Rt, transfer the
result to register Rd). Opcode: 001010 <br>
vi. XORI Rt Rs Imm (Take a bitwise XOR of the contents of registers Rs and the
immediate value “Imm”, transfer the result to register Rt). Opcode: 001011 <br>
c. Memory Access Instructions <br>
i. LDW Rt Rs Imm (Add the contents of Rs and the immediate value “Imm” to generate
the effective address “A”, load the contents (32-bits) of the memory location at address
“A” into register Rt). Opcode: 001100 <br>
ii. STW Rt Rs Imm (Add the contents of Rs and the immediate value “Imm” to generate
the effective address “A”, store the contents of register Rt (32-bits) at the memory
address “A”). Opcode: 001101 <br>
d. Control Flow Instructions <br>
i. BZ Rs x (If the contents of register Rs are zero, then branch to the “x”th instruction from
the current instruction). Opcode: 001110 <br>
ii. BEQ Rs Rt x (Compare the contents of registers Rs and Rt. If they are equal, then
branch to the “x”th instruction from the current instruction). Opcode: 001111 <br>
iii. JR Rs (Load the PC [program counter] with the contents of register Rs. Jump to the new
PC). Opcode: 010000 <br>
iv. HALT (Stop executing the program). Opcode: 010001 <br>
<br>
The data should be in "Big Endian" format and signed for all arithmetic and address calculation operations.
