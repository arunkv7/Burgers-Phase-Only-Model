#!/usr/bin/env python    
# line above specifies which program should be called to run this script - called shebang
# the way it is called above (and not #!/user/bin/python) ensures portability amongst Unix distros

######################
##	Library Imports
######################
import matplotlib
matplotlib.use('TkAgg') # Use this backend for displaying plots in window
# matplotlib.use('Agg') # Use this backend for writing plots to file

import h5py
import sys
import os
import numpy as np
import matplotlib.pyplot as plt




######################
##	Read input file
######################
# Check if program was given directory for input file
if (len(sys.argv) == 1):
	print("No Input file specified, Error.\n")
	sys.exit()
else :
	inpt_dir_data = str(sys.argv[1])


# print directory of input file to screen
print("\n\tData Directory: %s\n" % inpt_dir_data)


# Open input file in given directory for reading in data
if (os.path.isfile(inpt_dir_data + "/Runtime_Data.h5")):
	HDFfileData = h5py.File(inpt_dir_data + "/Runtime_Data.h5", 'r')
else:
	print("Cannot open data file, Error.\n")
	sys.exit()


# print input file name to screen
print("\t     Data File: %s\n" % "/Runtime_Data.h5")





######################
##	Output Directory
######################
# Get current working directory
out_dir_data = os.getcwd()


# # create output directory if doesn't exist
# if (os.path.isdir(out_dir_data + "/TestPlots")):
# 	out_dir_data += "/TestPlots" # add new dir to path
# 	os.mkdir(out_dir_data)       # make the new dir
# 	if (os.path.isdir(out_dir_data)): 
# 		print("Output directory: %s" % out_dir_data)
# 	else:
# 		print("Failed to create output directory, Error! \n")
# 		sys.exit()
# else:
# 	out_dir_data += "/TestPlots"

# check if output directory exist
if (os.path.isdir(out_dir_data + "/TestPlots")):
	out_dir_data += "/TestPlots"
else:
	print("Failed to detect output directory, Error! \n")
	sys.exit()

print("\tOutput Directory: %s\n\n" % out_dir_data)




######################
##	Open datasets
######################
# Size parameters
num_c_modes = HDFfileData['ComplexModesFull'].shape[1]
num_r_modes = (num_c_modes-1)*2
num_tsteps  = HDFfileData['ComplexModesFull'].shape[0]


# data
u_z = HDFfileData['ComplexModesFull']



######################
##	Prelim data calc
######################
dx = 2*np.pi / num_r_modes;
x  = np.arange(0, 2*np.pi, dx)



######################
##	Plotting
######################
for t in range(num_tsteps):
	print("Snapshot Indx = %d\n" % t)
	# plt.clf()

	plt.plot(np.fft.ifft(u_z[t, :]).real)
	
	plt.title('Real Space Solution')
	plt.xlabel(r'$x$')
	plt.ylabel(r'$u$')
	plt.grid(which='major', axis='both')
	plt.savefig(out_dir_data +'/Snap_{:05d}.png'.format(t), format='png', dpi = 800)	
	plt.close()
	


