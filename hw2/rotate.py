#coding=utf-8
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import scipy as sp
from scipy import misc, ndimage
from base import *

im = misc.imread("pic/Fig4.04(a).jpg")
while 1:
    for i in range(0, 360):
        nim = ndimage.rotate(im, i)
        cim = to_center_pic(nim)
        dft2 = np.fft.fft2(cim)#DFT2(cim)
        plt.subplot(121)
        plt.imshow(nim, "gray")
        plt.subplot(122)
        plt.imshow(np.log(1 + np.abs(dft2)), "gray")

        plt.pause(0.1)
