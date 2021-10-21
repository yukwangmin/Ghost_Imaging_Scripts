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
parser.add_argument('-i', '--input', default='', type=str, metavar='PATH', help='path to image file')



def main():
    args = parser.parse_args()	
    directory = args.input
    start_time = time.time()



    for i in range(634):

        filename = f'/image-{i}.npz'
        f_image = open(directory + filename, "rb")
        print(filename)

        image = np.load(f_image)
        f_image.close()




        fig, ax = plt.subplots(ncols=1,nrows=1, figsize=(10, 10))
        _=ax.imshow(image, norm=mpl.colors.LogNorm())
        fig.colorbar(_)


        outfile=f'image-{i}.png'
        plt.savefig(outfile, format='png')
        plt.close()

        

        end_time = time.time()
        print(f'[{i}]: Running time: {end_time - start_time}.')
        start_time = end_time






if __name__ == "__main__":
    main()



