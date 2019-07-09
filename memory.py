import os

class Memory(object):
	'''
	Class to read and store a trace file of Instructions.
	'''
	def __init__(self,path):
		self.mem_trace=dict()
		if os.path.exists(path):
			index = 0
			with open(path,'r+') as trace:
				lines = trace.readlines()
				for line in lines:
					self.mem_trace[index] = line.strip('\n')
					index += 4
    
	def read_word(self,index):
		'''
		Reads data from a memory location
		'''
		return self.mem_trace[index]
    
	def read_byte(self,index):
		offset = index%4
		word = self.mem_trace[index+offset]
		byte = int('{0:032b}'.format(int.from_bytes(bytes.fromhex(word),byteorder='big',signed=True))[offset*8:offset*8+8])
		return byte
    
	def write_byte(self,index,word):
		offset = index%4
		word1 = self.mem_trace[index+offset]
		word1 = '{0:032b}'.format(int.from_bytes(bytes.fromhex(word1),byteorder='big',signed=True))
		word = '{0:08b}'.format(int.from_bytes(bytes.fromhex(word),byteorder='big',signed=True))
		word_write = word1[:offset*8] + word + word1[offset*8+8:]
		self.mem_trace[index] = hex(int(word_write,2))[2:]
		return
        
	def write_word(self,index,word):
		'''
		Writes data to a memory location
		'''
		self.mem_trace[index] = word
		return

class registers(object):
	'''
	Defines 0-32 registers for a processor
	'''
	def __init__(self):
		self.regs=dict()
		for index in range(32):
			self.regs[index] = 0
    
	def read_reg(self,index):
		'''
		Returns the register value
		'''
		return self.regs[index]
    
	def write_reg(self,index,word):
		'''
		Writes data to particular register
		'''
		self.regs[index] = word
		return