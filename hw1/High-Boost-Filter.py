#coding=utf-8

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from base import *

m4 = np.matrix([[0,1,0],[1,-4,1],[0,1,0]])
m8 = np.matrix([[1,1,1],[1,-8,1],[1,1,1]])

im = mpimg.imread("pic/Fig3.43(a).jpg")

def High_Boost_filter(im, A, c):
    fhb = A * im.astype(np.double) - conv2(im, c)
    return normal_pic(fhb)

fhb0 = High_Boost_filter(im, 0, m4)
fhb1 = High_Boost_filter(im, 1, m4)
fhb1_7 = High_Boost_filter(im, 1.7, m4)

fhb80 = High_Boost_filter(im, 0, m8)
fhb81 = High_Boost_filter(im, 1, m8)
fhb81_7 = High_Boost_filter(im, 1.7, m8)

plt.subplot(2, 4, 1)
plt.title("source")
plt.imshow(im, "gray")

plt.subplot(2, 4, 2)
plt.title("A = 0 (m4)")
plt.imshow(fhb0, "gray")

plt.subplot(2, 4, 3)
plt.title("A = 1 (m4)")
plt.imshow(fhb1, "gray")

plt.subplot(2, 4, 4)
plt.title("A = 1.7 (m4)")
plt.imshow(fhb1_7, "gray")

plt.subplot(2, 4, 6)
plt.title("A = 0 (m8)")
plt.imshow(fhb80, "gray")

plt.subplot(2, 4, 7)
plt.title("A = 1 (m8)")
plt.imshow(fhb81, "gray")

plt.subplot(2, 4, 8)
plt.title("A = 1.7 (m8)")
plt.imshow(fhb81_7, "gray")

plt.show()
