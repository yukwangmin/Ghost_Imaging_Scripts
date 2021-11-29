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

from scipy.optimize import curve_fit

parser = argparse.ArgumentParser(description='')
parser.add_argument('-i', '--input', default='', type=str, metavar='PATH', help='path to csv file')


def main():
    args = parser.parse_args()	
    directory = args.input
    start_time = time.time()

    for i in range(72):
    #for i in range(41,76):

        #filename = directory + f'/Beamline_Cycles-2hr_W0028_H07-210806-140732-{i}.csv'	
        filename = directory + f'/toa-{i}.npz'	
        print(filename)

        #data = np.loadtxt(filename, dtype=int, delimiter=",",usecols=(0,1,2,3))

        #x  = data[:, 0]
        #y  = data[:, 1]
        #toa   = data[:, 2]
        #tot   = data[:, 3]
        #toa = toa / 4096*25*1e-9

        f_toa = open(filename, "rb")
        toa = np.load(f_toa)
        f_toa.close()

        print(f'TOA length: {len(toa)}, MIN TOA: {min(toa)}, MAX TOA: {max(toa)}')




        fig, ax0 = plt.subplots(ncols=1, figsize=(20, 4))
        plt.hist(toa, bins = 400, color = 'r', ec = 'k')
        plt.title("TOA", fontsize = 12) # change the title
        plt.xlabel('TOA, second',fontsize = 12)
        plt.yscale('log')

        outfile=f'toa_{i}.png'    
        #plt.show(i)
        plt.savefig(outfile, format='png')
        plt.close()

        end_time = time.time()
        print(f'[{i}]: Running time: {end_time - start_time}.')
        start_time = end_time



if __name__ == "__main__":
    main()
