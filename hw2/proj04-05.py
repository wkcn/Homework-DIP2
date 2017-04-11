#coding=utf-8
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from base import *
aim = mpimg.imread("pic/Fig4.41(a).jpg")
arows, acols = aim.shape
bim = mpimg.imread("pic/Fig4.41(b).jpg")
brows, bcols = bim.shape

mrows = max(arows, brows)
mcols = max(acols, bcols)

za = np.zeros((mrows, mcols)).astype(np.uint8)
zb = np.zeros((mcols, mcols)).astype(np.uint8)
za[:arows, :acols] = aim
zb[:brows, :bcols] = bim

def show_max(res):
    ma = np.max(res)
    rows, cols = np.where(res == ma)
    print ("The maximum value in the 2D corr function is %lf" % ma)
    print ("Index: (x,y)")
    for i in range(len(rows)):
        print ("(%d, %d)" % (cols[i], rows[i]))
    print ("")

# center
print ("center")
cza = to_center_pic(za)
czb = to_center_pic(zb)
afft2 = np.fft.fft2(cza) / (mrows * mcols)
bfft2 = np.fft.fft2(czb) / (mrows * mcols)
mab = np.multiply(afft2, np.conjugate(bfft2))
res = (to_center_pic(np.fft.ifft2(mab) * mrows * mcols)).astype(np.int)
show_max(res)

plt.subplot(321)
plt.imshow(aim, "gray")
plt.subplot(322)
plt.imshow(bim, "gray")
plt.subplot(323)
plt.imshow(za, "gray")
plt.subplot(324)
plt.imshow(zb, "gray")
plt.subplot(325)
plt.imshow(res, "gray")

plt.show()

# if no center
print ("no center")
cza = (za)
czb = (zb)
afft2 = np.fft.fft2(cza) / (mrows * mcols)
bfft2 = np.fft.fft2(czb) / (mrows * mcols)
mab = np.multiply(afft2, np.conjugate(bfft2))
res2 = ((np.fft.ifft2(mab) * mrows * mcols)).astype(np.int)
show_max(res2)

plt.subplot(321)
plt.imshow(aim, "gray")
plt.subplot(322)
plt.imshow(bim, "gray")
plt.subplot(323)
plt.imshow(za, "gray")
plt.subplot(324)
plt.imshow(zb, "gray")
plt.subplot(325)
plt.imshow(res2, "gray")

plt.show()

print ("diff between center and no center: %d" % np.sum(res != res2))
