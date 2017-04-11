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
dft2 = DFT2(ci) 

R = lambda x : str(x.real)

print ("The average value is " + R(fft2[row / 2, col / 2] / (row * col)) + " (center, fft2)")
print ("The average value is " + R(np.fft.fft2(cim)[0,0] / (row * col)) + " (no center, fft2)")
print ("The average value is " + R(dft2[row / 2, col / 2]) + " (center, dft2)")
print ("The average value is " + R(DFT2(cim)[0,0]) + " (no center, dft2)")


lgfft2 = np.log(1 + np.abs(fft2))
plt.imshow(normal_pic(lgfft2), "gray")
plt.show()
