import argparse

import numpy as np
#%matplotlib inline
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from matplotlib.ticker import NullFormatter
import glob
import time
import math
import sys

from scipy.optimize import curve_fit

parser = argparse.ArgumentParser(description='')
parser.add_argument('-i', '--input', default='', type=str, metavar='PATH', help='path to csv file')
parser.add_argument('-o', '--output', default='', type=str, metavar='PATH', help='path to npz file')


def main():
    args = parser.parse_args()	
    directory = args.input
    out_directory = args.output
    start_time = time.time()

    #x = np.empty(shape=(0), dtype=int)
    #y = np.empty(shape=(0), dtype=int)
    #toa = np.empty(shape=(0), dtype=int)
    #tot = np.empty(shape=(0), dtype=int)


    for i in range(76):
    #for i in range(72):

        filename = directory + f'/Beamline_Cycles-2hr_W0028_H07-210806-140732-{i}.csv'
        #filename = directory + f'/Beamline_Cycles-2hr_Run2_W0028_H07-210806-161604-{i}.csv'
        print(filename)

        data = np.loadtxt(filename, dtype=int, delimiter=",",usecols=(0,1,2,3))

        x = data[:,0]
        y = data[:,1]
        toa = data[:,2] / 4096*25*1e-9
        tot = data[:,3]


        f_x = open(out_directory + f'/x-{i}.npz', "wb")
        f_y = open(out_directory + f'/y-{i}.npz', "wb")
        f_toa = open(out_directory + f'/toa-{i}.npz', "wb")
        f_tot = open(out_directory + f'/tot-{i}.npz', "wb")
        np.save(f_x, x)
        np.save(f_y, y)
        np.save(f_toa, toa)
        np.save(f_tot, tot)
        f_x.close()
        f_y.close()
        f_toa.close()
        f_tot.close()

        #print(len(toa))
        #print(max(toa))
        #print(min(toa))

        end_time = time.time()
        print(f'[{i}]: Running time: {end_time - start_time}.')
        start_time = end_time

        sys.stdout.flush()





if __name__ == "__main__":
    main()
