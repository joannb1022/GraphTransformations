from gui import *
from parsing import *
import sys

# Get name of input file
# filename = str(sys.argv[1])
filename = "tiag.txt"

# Initialize global variables
globals.N, globals.G, globals.productions, globals.rules = prepare_data(filename)

# Display GUI
window()
