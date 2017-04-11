# 数字图像处理 实验二
***
## 04-01 Two-Dimensioal Fast Fourier Transform
### 问题内容
	(a) Multiply the input image by (-1)^(x+y) to center the transform for filtering.

	(b) Multiply the resulting (complex) array by a real function (in the sense that the

	the real coefficients multiply both the real and imaginary parts of the transforms).

	Recall that multiplication of two images is done on pairs of corresponding elements.

	(c) Compute the inverse Fourier transform.

	(d) Multiply the result by (-1)^(x+y) and take the real part.

	(e) Compute the spectrum.

### 技术讨论
- 中心化
- 傅里叶变换
- 逆傅里叶变换
### 结果分析
* 对图像进行傅里叶变换, 使图像从空间域转为频域.
* 假设图像在空间域的大小为MxN, 该图像经过傅里叶变换, 从空间域到频域后, 在频域中的最小大小也为MxN, 周期为MxN.
* 这里使用三个矩阵相乘的方法实现离散傅里叶变换(DFT)
* 使用了numpy自带的fft2, octave和matlab的fft2, 和自己实现的DFT函数进行比较. 发现fft2得到的结果没有乘以系数1/MN
公式推导:
## 04-02 Fourier Spectrum and Average Value
### 问题内容
	(a) Download Fig. 4.18(a) and compute its (centered) Fourier spectrum.

	(b) Display the spectrum.

	(c) Use your result in (a) to compute the average value of the image.
### 技术讨论
- 显示频谱

	由于图像矩阵经过傅里叶变换后得到的二维矩阵的元素为虚数, 并且存在负数和绝对值比较大的数. 为了得到良好的显示效果, 将傅里叶变换后得到的结果F(u, v), 转换为log2(1 + abs(F(u, v)))

- 计算均值
	- 当进行傅里叶变换前没有将图像中心化时, 当u = 0, v = 0, F(0, 0)等于图像像素取值的平均值.
	- 当进行傅里叶变换前进行了图像中心化时, 若M, N都为偶数时, u = M / 2, v = N / 2时, F(u, v)等于图像像素取值的平均值.
		- 公式推导

	 [注: 这里的矩阵下标从0开始]

### 结果分析
使用了自己编写的DFT函数和numpy自带的fft2函数, 针对中心化和非中心化分别求图像像素取值的平均值. 发现四种方法的结果一致.
```
The average value is 207.36348 (center, fft2)
The average value is 207.36348 (no center, fft2)
The average value is 207.36348 (center, dft2)
The average value is 207.36348 (no center, dft2)
```
## 04-03 Lowpass Filtering
### 问题内容
	(a) Implement the Gaussian lowpass filter in Eq. (4.3-7). You must be able to
specify the size, M x N, of the resulting 2D function. In addition, you must be able
to specify where the 2D location of the center of the Gaussian function.
	(b) Download Fig. 4.11(a) [this image is the same as Fig. 4.18(a)] and lowpass
filter it to obtain Fig. 4.18(c).
### 技术讨论
- 高斯低通滤波器
### 结果分析
## 04-04 Highpass Filtering Using a Lowpass Image
### 技术讨论
### 结果分析
## 04-05 Correlation in the Frequency Domain 
### 问题内容
### 技术讨论
### 结果分析

## 检验谱平面随着图像旋转而旋转的性质
### 问题内容
### 技术讨论
### 结果分析
