Greengraph
=====================================
### Intro
Greengraph is a set of classes which generate a graph of the proportion 
of green pixels in a series of satellite images between two points. 

### Installation instructions
The Greengraph package can be installed using the stand pip comand pip <library>.
 - Download the greengraphs package to your local machine
 - Using the command line, navigate to the package root folder
 - Now on your command line:
 - **Windows**   : `python setup.py install`
 - **Mac/Other** : `sudo python setup.py install`
 
 Alternatively, the package can be installed directly from GitHub using `pip`
 **pip install**
 `pip install git+https://github.com/davidtwomey/greengraphs_cw.git`
 

###Example Implementation
To USE this program, please follow the steps:

 1. Install
 
 2. Enter the two locations you wish to analyse (--From; --To)
 3. Select optional additional arguments (--Steps; --Out)
 Your command line input should now look similar to:
 `greengraph --from 'London' --to 'Paris' --steps 50 --out 'my_filename'`
 
 NOTE: Your --Out filename should not include an extension as this is set to .png

The output plot will be saved in the folder where the command is called
 *e.g if you call the package from the desktop, the results file will be output there for the user to view.*