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

    whole_boundary = []
        
    threshold = 1e+4
    beam_on = False

    for i in range(76):

        filename = directory + f'/toa-{i}.npz'	
        print(filename)


        f_toa = open(filename, "rb")
        toa = np.load(f_toa)
        f_toa.close()

        data_length = len(toa)



        print('data_length: ', data_length)
        boundary = []
        
        fig, ax0 = plt.subplots(ncols=1, figsize=(20, 4))
        n, bins, _ = plt.hist(toa, bins = 400, color = 'r', ec = 'k')
        plt.title("TOA", fontsize = 12) # change the title
        plt.xlabel('TOA, second',fontsize = 12)
        plt.yscale('log')



        for k in range(400):

            if beam_on:
 
                if n[k] <= threshold:
                    beam_on = not beam_on
                    boundary += [bins[k-1]]
       
            else: # beam off
                if n[k] > threshold:
                    beam_on = not beam_on
                    boundary += [bins[k+1]]
 

        whole_boundary = whole_boundary + boundary




        for b in boundary:
            plt.axvline(x=b,color='blue')

        outfile=f'toa_boundary_{i}.png'    
        #plt.show(i)
        plt.savefig(outfile, format='png')
        plt.close()

        end_time = time.time()
        print(f'[{i}]: Running time: {end_time - start_time}.')
        start_time = end_time


    print('whole_boundary = ', whole_boundary)




if __name__ == "__main__":
    main()
