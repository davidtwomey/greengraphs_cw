from matplotlib import pyplot as plt
from greengrapher import Greengraph
from argparse import ArgumentParser



def process():
	parser = ArgumentParser(description = "Evaluate green pixels between two locations")
	
	parser.add_argument('--from', '-f', help = 'Start location', dest='startLoc')
	parser.add_argument('--to','-t', help = 'End location', dest='endLoc')
	parser.add_argument('--steps','-s', type= int, help = 'How many steps between locations to evaluate',default = 20)
	parser.add_argument('--out','-o',help= 'Define output filename. Default: PNG',default = 'output.png')
	arguments= parser.parse_args()
	
	graph = Greengraph(arguments.startLoc,arguments.endLoc)
	data = graph.green_between(arguments.steps)
	
	plt.plot(data)
	plt.savefig(arguments.out)
	plt.show()
		
if __name__ == "__main__":
	process()