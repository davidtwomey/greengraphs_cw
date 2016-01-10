from matplotlib import pyplot as plt
from greengraph import Greengraph
from argparse import ArgumentParser


parser = ArgumentParser(description = "Evaluate green pixels between two locations")
	
parser.add_argument('--from', '-f', help = 'Start location, default: London', dest='startLoc', default='London')
parser.add_argument('--to','-t', help = 'End location, default: Paris', dest='endLoc',default = 'Paris')
parser.add_argument('--steps','-s', type= int, help = 'How many steps between locations to evaluate, default:20',default = 20,dest='steps')
parser.add_argument('--out','-o',help= 'Define output filename. Type: PNG',default = 'output', dest='out')



def process():
    arguments= parser.parse_args()
    graph = Greengraph(arguments.startLoc,arguments.endLoc)
    data = graph.green_between(arguments.steps)
    plt.plot(data)
    
    # Labelling of plot 
    plt.xlabel("Step")
    plt.ylabel("Number of green pixels (Max 160000)")
    plt.title("Graph of green pixels in geographical images between"+
              " ".join(arguments.startLoc)+ "and" + " ".join(arguments.endLoc))
    plt.savefig(arguments.out+'.png')
    plt.show()
		
if __name__ == "__main__":
	process()