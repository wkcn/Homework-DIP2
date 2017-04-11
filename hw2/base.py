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

def get_gray(im):
    dim = im.astype(np.int) 
    return ((dim[:,:,0] * 299 + dim[:,:,1] * 587 + dim[:,:,2] * 114 + 500) / 1000).astype(np.uint8)

# 卷积结果不对图像进行标准化, 返回值可以存在负数
def conv2(im, mask):
    dim = im.astype(np.double)
    row, col = im.shape
    mrow, mcol = mask.shape
    hr = mrow // 2
    hc = mcol // 2
    res = np.zeros((row, col))
    ms = {}
    res = np.zeros((row, col))
    for r in range(mrow):
        for c in range(mcol):
            z = mask[r, c]
            if z == 0:
                continue
            if z not in ms:
                ms[z] = dim * z 
            m = ms[z]
            dr = r - hr
            dc = c - hc
            res[max(0, dr):min(row, dr + row), max(0, dc):min(col, dc + col)] += m[max(0, -dr):min(row, row - dr), max(0, -dc):min(col, col - dc)]
    return res

# 标准化为uint8类型
def normal_pic(im):
    tim = np.clip(im, 0, 255)
    return tim.astype(np.uint8)

def dec_pic(a, b):
    return np.clip((a.astype(np.int) - b.astype(np.int)), 0, 255).astype(np.uint8)

def add_pic(a, b):
    return np.clip((a.astype(np.int) + b.astype(np.int)), 0, 255).astype(np.uint8)

def mul_pic(a,b):
    return normal_pic(np.multiply(a.astype(np.int), b.astype(np.int)))

def get_bilinear_value(im, pos):
    # pos = (r,c)
    # 使用双线性插值
    r,c = im.shape
    pos = np.array(pos)
    ipos = pos.astype(np.int) 
    ir, ic = ipos
    d = pos - ipos 
    if ir + 1 >= r:
        d[0] = 0
    if ic + 1 >= c:
        d[1] = 0
    if d[0] == 0 and d[1] == 0:
        return im[ir, ic]
    if d[0] == 0:
        #d[1] != 0
        return im[ir, ic] * (1 - d[1]) + im[ir, ic + 1] * d[1]
    if d[1] == 0:
        #d[0] != 0
        return im[ir, ic] * (1 - d[0]) + im[ir + 1, ic] * d[0]
    # d[0] != 0 and d[1] != 0
    up = im[ir, ic] * (1 - d[1]) + im[ir, ic + 1] * d[1]
    down = im[ir + 1, ic] * (1 - d[1]) + im[ir + 1, ic + 1] * d[1]
    return up * (1 - d[0]) + down * d[0]


def zoom_matrix(im, siz):
    # im.shape -> siz
    row, col = im.shape
    siz = (int(siz[0]), int(siz[1]))
    tr = row * 1.0 / siz[0]
    tc = col * 1.0 / siz[1]
    newim = np.zeros(siz)
    for r in range(siz[0]):
        for c in range(siz[1]):
            hr = r * tr
            hc = c * tc
            newim[r, c] = get_bilinear_value(im, (hr,hc))
    return newim 

def shrink_matrix(im, siz):
    row, col = im.shape
    siz = (int(round(siz[0])), int(round(siz[1]))) # small
    tr = row * 1.0 / siz[0]
    tc = col * 1.0 / siz[1]
    itr = int(tr)
    itc = int(tc)
    newim = np.zeros(siz)
    for r in range(siz[0]):
        for c in range(siz[1]):
            newim[r,c] = im[r*itr,c*itc]#np.mean(im[r*itr:(r+1)*itr, c*itc:(c+1)*itc])
    return newim


def zoom_pic(im, siz):
    newim = zoom_matrix(im.astype(np.int), siz)
    return normal_pic(newim)
def shrink_pic(im, siz):
    newim = shrink_matrix(im.astype(np.int), siz)
    return normal_pic(newim)

def resize_pic(im, siz):
    # TODO
    row,col = im.shape
    return zoom_pic(im, siz)
    if row < siz[0] or col < siz[1]:
        # 放大
        #r1 = siz[0] * 1.0 / row
        #r2 = siz[1] * 1.0 / col
        #r = max(r1, r2)
        #return zoom_pic(im, (row * r, col * r))
        return zoom_pic(im, siz)
    # 缩小
    return shrink_matrix(im, siz)

def DFT2(im):
    row, col = im.shape
    # 由于周期性
    rs = np.matrix(np.arange(row))
    ur = np.multiply(rs.T, rs)
    cs = np.matrix(np.arange(col))
    uc = np.multiply(cs.T, cs)

    left = np.exp(-2j * np.pi * ur / row)
    right = np.exp(-2j * np.pi * uc / col)

    return left * im.astype(np.complex) * right / (row * col)

def IDFT2(im):
    row, col = im.shape
    # 由于周期性
    rs = np.matrix(np.arange(row))
    ur = np.multiply(rs.T, rs)
    cs = np.matrix(np.arange(col))
    uc = np.multiply(cs.T, cs)
    left = np.exp(2j * np.pi * ur / row)
    right = np.exp(2j * np.pi * uc / col)

    return left * im.astype(np.complex) * right

if __name__ == "__main__":
    '''
    b = np.array([[1,4,7], [2,5,8], [3,6,9]])
    c = zoom_matrix(b, (4,7))
    print c.astype(np.int)
    d = zoom_matrix(c, (3,3))
    print d.astype(np.int)
    print (b)
    c = (zoom_matrix(b, (10,10)))
    print (c)
    d = shrink_matrix(c, (3,3))
    print (d)
    '''
    '''
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    im = mpimg.imread("../hw1/pic/Fig3.40(a).jpg")
    s = im.shape
    plt.imshow(im, "gray")
    plt.show()
    laim = resize_pic(im, (100,100))
    plt.imshow(laim, "gray")
    plt.show()
    laim = resize_pic(laim, s)
    plt.imshow(laim, "gray")
    plt.show()
    '''

    a = np.matrix("1,2,3;3,4,5;3,2,1")
    b = DFT2(a)
    c = IDFT2(b)
    print (a)
    print (b)
    print (c)
