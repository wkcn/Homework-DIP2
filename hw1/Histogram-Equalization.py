#coding=utf-8

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from base import *

im = mpimg.imread("Fig3.08(a).jpg")
row, col = im.shape

L = 256 # 灰度级

# 统计灰度级
cnts = get_cnts(im, L)

# 计算出各个灰度值的频率
p = cnts / np.sum(cnts)

# 累计分布
cp = np.cumsum(p)
#cp[0] = 0.0
s = np.around(cp * (L - 1))

f = np.frompyfunc(lambda x : s[x], 1, 1)
new_im = f(im).astype(np.uint8)

# 统计灰度级
new_cnts = get_cnts(new_im, L)

# 绘制原图
plt.subplot(2,2,1)
plt.title("Before")
plt.imshow(im, "gray")
# 绘制直方图均衡后的图像
plt.subplot(2,2,2)
plt.title("After")
plt.imshow(new_im, "gray")

# 原图绘制直方图
plt.subplot(2,2,3)
plt.bar(range(L), cnts)

# 绘制均衡后的直方图
plt.subplot(2,2,4)
plt.bar(range(L), new_cnts)
plt.show()
