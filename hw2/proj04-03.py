#coding=utf-8
# 04-01 ~ 04-05
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from base import *

im = mpimg.imread("pic/Fig4.11(a).jpg")
rows, cols = im.shape

CR = 40
'''
plt.title("Gaussian Lowpass Filter")
plt.imshow(np.log(1 + gaus_lowpass),  "gray")
plt.show()
'''

def get_lowpass_pic(R):
    gaus_lowpass = get_gaussian_lowpass_filter(rows, cols, R)
# 中心化
    cim = to_center_pic(im) 
# DFT
    dim = DFT2(cim)
# 滤波
    gim = np.multiply(dim, gaus_lowpass.astype(np.complex))
# 反DFT并取实部
    rim = IDFT2(gim).astype(np.int) 
# 乘以(-1)^(x+y) shift
    result = normal_pic(to_center_pic(rim))
    return result

result = get_lowpass_pic(CR)
plt.subplot(131)
plt.title("source")
plt.imshow(im, "gray")
plt.subplot(132)
plt.title("result")
plt.imshow(result, "gray")
plt.subplot(133)
plt.title("Gaussian Lowpass Filter")
gaus_lowpass = get_gaussian_lowpass_filter(rows, cols, CR)
plt.imshow(np.log(1 + gaus_lowpass), "gray")

plt.show()

rs = [0,5,15,30,80,230]
for i in range(6):
    if i == 0:
        plt.subplot(321)
        plt.title("source")
        plt.imshow(im, "gray")
        continue
    R = rs[i]
    plt.subplot(3,2,i+1)
    plt.title("R = %d" % R)
    plt.imshow(get_lowpass_pic(R), "gray")
plt.show()

rs = [0,5,15,30,80,230]
for i in range(6):
    if i == 0:
        continue
    R = rs[i]
    plt.subplot(3,2,i+1)
    plt.title("R = %d" % R)
    gaus_lowpass = get_gaussian_lowpass_filter(rows, cols, R)
    plt.imshow(np.log(1 + gaus_lowpass), "gray")
plt.show()

