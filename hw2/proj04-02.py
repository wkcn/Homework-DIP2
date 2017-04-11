#coding=utf-8
# 04-01 ~ 04-05
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from base import *

im = mpimg.imread("pic/Fig4.11(a).jpg")
cim = im.astype(np.complex)
row, col = cim.shape
print ("Shape: %d x %d" % (row, col))
mesh = np.meshgrid(np.arange(col), np.arange(row))
xplusy = mesh[0] + mesh[1]
k = np.power(-1, xplusy)
ci = np.multiply(cim, k)

fft2 = np.fft.fft2(ci)

print ("The average value is " + str(fft2[row / 2, col / 2]) + " (center)")
print ("The average value is " + str(np.fft.fft2(cim)[0,0]) + " (no center)")


lgfft2 = np.log(1 + np.abs(fft2))
plt.imshow(normal_pic(lgfft2), "gray")
plt.show()
