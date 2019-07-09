class Instruction(object):
	'''
	This class defines an instruction. It stores different attributes of instructions
	It has a decode function which can be used to decode different registers in the hex input.
	Input:
		hex_instr: hex code of the instruction.
	'''
	def __init__(self,hex_instr):
		'''
		Instantiates a new instruction.
		'''
		self.opcode_dict = {'000000':'Add','000001':'Addi','000010':'Sub','000011':'Subi','000100':'Mul','000101':'Muli',
							'000110':'Or','000111':'Ori','001000':'And','001001':'Andi','001010':'Xor','001011':'Xori',
							'001100':'Ldw','001101':'Stw','001110':'Bz','001111':'Beq','010000':'Jr','010001':'Halt'}
		self.r_type = ['Add','Sub','Mul','Or','And','Xor']
		self.hex = hex_instr
		self.opcode = None
		self.type = None
		self.rs = 0
		self.reg_rs = None
		self.rt = 0
		self.reg_rt = None
		self.rd = 0
		self.reg_rd = None
		self.imm = None
		self.x_addr = None
		self.frwd_rs = False
		self.frwd_rt = False
    
	def __repr__(self,):
		return f'Instr({self.hex},{self.opcode},R{self.reg_rs}:{self.rs},R{self.reg_rt}:{self.rt},R{self.reg_rd}:{self.rd},imm:{self.imm},addr:{self.x_addr},rs_f:{self.frwd_rs},rt_f:{self.frwd_rt})'   
    
	def decode(self,):
		'''
		Decodes the instruction hex string.
		'''
		if self.hex==None:
			return
		bin_inst = '{0:032b}'.format(int.from_bytes(bytes.fromhex(self.hex),byteorder='big',signed=True))
		opcode = bin_inst[:6]
		if opcode in self.opcode_dict:
			self.opcode = self.opcode_dict[opcode]
			if self.opcode in self.r_type:
				self.reg_rs = int(bin_inst[6:11],2)
				self.reg_rt = int(bin_inst[11:16],2)
				self.reg_rd = int(bin_inst[16:21],2)
				self.type = 'R'
			else:
				self.type = 'I'
				if self.opcode=='Halt':
					return
				self.reg_rs = int(bin_inst[6:11],2)
				if self.opcode=='Jr':
					return
				if self.opcode=='Bz':
					self.x_addr = int('{0:016b}'.format(int.from_bytes(bytes.fromhex(self.hex[-4:]),byteorder='big',signed=True)),2)
					return
				self.reg_rt = int(bin_inst[11:16],2)
				self.imm = int('{0:016b}'.format(int.from_bytes(bytes.fromhex(self.hex[-4:]),byteorder='big',signed=True)),2)
		return