from matplotlib import pyplot as plt
from greengrapher import greengraph
from argparse import ArgumentParser



def process():
	parser = ArgumentParser(description = "Look for green pixels between two locations")
	
	parser.add_argument('city_one')
	parser.add_argument('city_two')
	parser.add_argument('steps')
	arguments= parser.parse_args()
	
	graph = greengraph(arguments.city_one,arguments.city_two)
	data = graph.green_between(arguments.steps)
	
	plt.plot(data)
	plt.show()
		
if __name__ == "__main__":
	process()