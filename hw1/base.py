#coding=utf-8
import numpy as np

def get_cnts(im, L):
    # 对灰度值进行计数
    row, col = im.shape
    cnts = np.zeros(L)
    for c in range(col):
        for r in range(row):
            gray = im[r, c]
            cnts[gray] += 1
    return cnts
