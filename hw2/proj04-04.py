#coding=utf-8
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from base import *
im = mpimg.imread("pic/Fig4.11(a).jpg")
rows, cols = im.shape

CR = 15

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

sharp_pic = dec_pic(im, get_lowpass_pic(CR))
ghpf_pic = filter_in_freq_domain(im, get_gaussian_highpass_filter(rows, rows, CR)) 

d = sharp_pic.astype(np.int) - ghpf_pic.astype(np.int)
print (np.sum(np.abs(d)))

plt.subplot(121)
plt.title("Sharped Pic")
plt.imshow(sharp_pic, "gray")

plt.subplot(122)
plt.title("GHPF Pic")
plt.imshow(ghpf_pic, "gray")

plt.show()

D = 30
for i in range(9):
    u = i * D + 1
    print ("R = %d, %d / 9 wait..." % (u, i + 1))
    plt.subplot(3,3,i+1)
    plt.title("R = %d" % u)
    sharp_pic = dec_pic(im, get_lowpass_pic(u))
    plt.imshow(sharp_pic, "gray")

plt.show()
