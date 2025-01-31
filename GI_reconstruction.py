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
parser.add_argument('-i', '--input', default='', type=str, metavar='PATH', help='path to image file')


def gi1(bin_size, ghost, img_sum, img_mp):
    for i in range(ghost.shape[0]):
        for j in range(ghost.shape[1]):
            sum = 0
    
            for bin in range(bin_size):
                sum += img_sum[bin]*img_mp[bin][i][j]
                #print(type(img_sum[bin]))
                #print(type(img_mp[bin]))
    
                
            ghost[i,j]=sum/bin_size    
    

def gi2(bin_size, ghost, img_sum, img_mp):
    avg = np.mean(img_sum)
    print('avg: ', avg)
    
    for i in range(ghost.shape[0]):
        for j in range(ghost.shape[1]):
            sum = 0
    
            for bin in range(bin_size):
                sum += (img_sum[bin] - avg)*img_mp[bin][i][j]
                #print(type(img_sum[bin]))
                #print(type(img_mp[bin]))
    
                
            ghost[i,j]=sum/bin_size    

#DGI
def gi3(bin_size, ghost, img_sum, img_mp, img_int):
    avg = np.mean(img_sum)
    int_avg = np.mean(img_int)
    
    for i in range(ghost.shape[0]):
        for j in range(ghost.shape[1]):
            sum = 0
    
            for bin in range(bin_size):
                sum += (img_sum[bin] - avg*img_int[bin]/int_avg)*img_mp[bin][i][j]
    
                
            ghost[i,j]=sum/bin_size    
    
            
#NGI
def gi4(bin_size, ghost, img_sum, img_mp, img_int):
    avg = np.mean(img_sum)
    int_avg = np.mean(img_int)
    
    for i in range(ghost.shape[0]):
        for j in range(ghost.shape[1]):
            sum = 0
    
            for bin in range(bin_size):
                sum += (img_sum[bin]/img_int[bin] - avg/int_avg)*img_mp[bin][i][j]
    
                
            ghost[i,j]=sum/bin_size    
    
    
def main():
    args = parser.parse_args()	
    directory = args.input
    start_time = time.time()



    img_size_x = 256
    img_size_y = 256

    image_num = 634
    image_pair = int(image_num/2)
    
    augment = 3

    bin_size = image_pair * augment
        

    #img_bucket = np.ndarray([bin_size], dtype=np.ndarray)
    img_mp = np.ndarray([bin_size], dtype=np.ndarray)
    img_sum = np.zeros([bin_size])
    img_int = np.zeros([bin_size])

    for k in range(augment):

        for i in range(image_pair):

            filename1 = f'/image-{2*i}.npz'
            f_image1 = open(directory + filename1, "rb")
            image1 = np.load(f_image1)
            f_image1.close()

            filename2 = f'/image-{2*i+1}.npz'
            f_image2 = open(directory + filename2, "rb")
            image2 = np.load(f_image2)
            f_image2.close()

            print(filename1)
            print(filename2)


            img_mp[i + image_pair*k] = image2
            img_sum[i + image_pair*k] = np.sum(image1)
            img_int[i + image_pair*k] = np.sum(img_mp[i + image_pair*k])

            if k > 0:
                #perturbation = np.random.randint(0,1000,size=img_size_x*img_size_y).reshape(img_size_x,img_size_y)
                perturbation = np.zeros([img_size_x,img_size_y])
                sum_p = np.sum(perturbation)
                
                img_mp[i + image_pair*k] = img_mp[i + image_pair*k] + perturbation
                img_sum[i + image_pair*k] += sum_p
                img_int[i + image_pair*k] = np.sum(img_mp[i + image_pair*k])
        

        end_time = time.time()
        print(f'[{i}]: Running time: {end_time - start_time}.')
        start_time = end_time

        sys.stdout.flush()


    method = 4

    ghost = np.zeros([img_size_x,img_size_y])
    

    if method == 1:
        gi1(bin_size, ghost, img_sum, img_mp)
    elif method == 2:
        gi2(bin_size, ghost, img_sum, img_mp)
    elif method == 3:
        gi3(bin_size, ghost, img_sum, img_mp, img_int)
    elif method == 4:
        gi4(bin_size, ghost, img_sum, img_mp, img_int)
    
    #fig, ax = plt.subplots(ncols=1,nrows=1, figsize=(10, 10))
    #_=ax.imshow(ghost, norm=mpl.colors.LogNorm())
    #fig.colorbar(_)



    

    #outfile=f'GI-method{method}.png'
    #plt.savefig(outfile, format='png')
    #plt.close()


    f_image = open(f'GI-method{method}_aug{augment}.npz', "wb")
    np.save(f_image, ghost)
    f_image.close()






if __name__ == "__main__":
    main()



