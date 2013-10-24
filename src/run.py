import sys
import getopt
from subprocess import call
from Simulation import Simulation
from Visualizer import Visualizer

def usage():
	print """
Usage:
-s - calculates and simulates simultaneously
-c - calculates simulation results and saves output to file
-v <data_file> - visualization from the output file
-h - this message

Parameters of the system may be adjusted in parameters.ini
for -s paramaters n <= 5 is advised.
For pure computing it is more convenient to use pypy instead of python.
	"""

try:
	opts, args = getopt.getopt(sys.argv[1:], "hcsv", \
                 ["help", "calculate", "simulate", "visualize"])
except getopt.GetoptError:
	usage()
	sys.exit(2)

if len(sys.argv) == 1:
	usage()
	sys.exit()

for opt, arg in opts:
	if opt in ("-h", "--help"):
		usage()
		sys.exit()
	elif opt in("-c", "--calculate"):
		try:
			call("pypy Simulation.py", shell = True)
		except: #pypy not found I guess
			Simulate().start_calculation()
	elif opt in("-s", "--simulate"):
		vis = Visualizer()
		vis.show_real_time()
	elif opt in("-v", "--visualize"):
		vis = Visualizer()
		vis.show_from_file()
	else:
		usage()
		sys.exit()
