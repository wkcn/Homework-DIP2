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

def show_max(res, im):
    row, col = im.shape
    z = np.zeros((row,col,3)).astype(np.uint8)
    z[:,:,0] = im
    z[:,:,1] = im
    z[:,:,2] = im
    ma = np.max(res)
    rows, cols = np.where(res == ma)
    print ("The maximum value in the 2D corr function is %lf" % ma)
    print ("Index: (x,y)")
    for i in range(len(rows)):
        r = rows[i]
        c = cols[i]
        print ("(%d, %d)" % (cols[i], rows[i]))
        z[r,c,0] = 255
        z[r:r+brows,c:c+bcols,0] = 255
    print ("")
    return z

# center
print ("center")
cza = to_center_pic(za)
czb = to_center_pic(zb)
afft2 = DFT2(cza)#np.fft.fft2(cza) / (mrows * mcols)
bfft2 = DFT2(czb)#np.fft.fft2(czb) / (mrows * mcols)
mab = np.multiply(afft2, np.conjugate(bfft2))
#mab = np.multiply(np.conjugate(afft2), (bfft2))
#res = (to_center_pic(np.fft.ifft2(mab) * mrows * mcols)).astype(np.int)
res = (to_center_pic(IDFT2(mab))).astype(np.int)
z = show_max(res, za)

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
plt.subplot(326)
plt.imshow(z)

plt.show()

# if no center
print ("no center")
cza = (za)
czb = (zb)
afft2 = np.fft.fft2(cza) / (mrows * mcols)
bfft2 = np.fft.fft2(czb) / (mrows * mcols)
mab = np.multiply(afft2, np.conjugate(bfft2))
#mab = np.multiply(np.conjugate(afft2), (bfft2))
res2 = ((np.fft.ifft2(mab) * mrows * mcols)).astype(np.int)
z = show_max(res2, za)

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
plt.subplot(326)
plt.imshow(z)

plt.show()

print ("diff between center and no center: %d" % np.sum(res != res2))
