from processor import Processor
from memory import Memory

def main():
	mem_image = Memory('./proj_trace.txt') #Enter the path for the trace file
	p1 = Processor(mem_image,forwarding=False,)
	p1.run()
	p1.print_stats()
	p2 = Processor(mem_image,forwarding=True,)
	p2.run()
	p2.print_stats()

if __name__=="__main__":
	main()
