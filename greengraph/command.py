from matplotlib import pyplot as plt
from greengraph import Greengraph
from argparse import ArgumentParser


parser = ArgumentParser(description = "Evaluate green pixels between two locations")
	
parser.add_argument('--from', '-f', help = 'Start location, default: London', dest='startLoc', default='London')
parser.add_argument('--to','-t', help = 'End location, default: Paris', dest='endLoc',default = 'Paris')
parser.add_argument('--steps','-s', type= int, help = 'How many steps between locations to evaluate, default:20',default = 20,dest='steps')
parser.add_argument('--out','-o',help= 'Define output filename. Type: PNG',default = 'output', dest='out')

def build_greengraph(args):
    graph = Greengraph(args.startLoc,args.endLoc)
    data = graph.green_between(args.steps)
    plt.plot(data)
    
    # Labelling of plot 
    plt.xlabel("Step")
    plt.ylabel("Number of green pixels (Max 160000)")
    plt.title("Green pixels in geographical images between "+
              "".join(args.startLoc)+ " and " + "".join(args.endLoc))
    plt.savefig(args.out+'.png')
    plt.show()

def process():
    args= parser.parse_args()
    build_greengraph(args)
    
		
if __name__ == "__main__":
	process()