# 数字图像处理 实验二
***
## 04-01 Two-Dimensioal Fast Fourier Transform
### 问题内容
	(a) Multiply the input image by (-1)^(x+y) to center the transform for filtering.

	(b) Multiply the resulting (complex) array by a real function (in the sense that the real coefficients multiply both the real and imaginary parts of the transforms).

	Recall that multiplication of two images is done on pairs of corresponding elements.

	(c) Compute the inverse Fourier transform.

	(d) Multiply the result by (-1)^(x+y) and take the real part.

	(e) Compute the spectrum.

### 技术讨论
- 中心化
	经过中心化后, 图像的频谱图的直流分量值将移到中心.
- 傅里叶变换
	将图像从空间域转到频域
- 逆傅里叶变换
	将图像从频域转到空间域
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
![频谱图](report_pic/0201.png)

图像的中心点最亮, 由于傅里叶变换前进行了中心化, 频谱图的中心为直流分量的取值.

频谱图的横轴和纵轴比较亮, 在横轴上能够看到很多个亮点, 说明图像的频谱在横轴的频率比较高.  

## 04-03 Lowpass Filtering
### 问题内容
	(a) Implement the Gaussian lowpass filter in Eq. (4.3-7). You must be able to specify the size, M x N, of the resulting 2D function. In addition, you must be able to specify where the 2D location of the center of the Gaussian function.
	(b) Download Fig. 4.11(a) [this image is the same as Fig. 4.18(a)] and lowpass filter it to obtain Fig. 4.18(c).
### 技术讨论
- 高斯低通滤波器
### 结果分析
![](report_pic/0301.png)

上图中, 左图为原图, 中间图为经过高斯低通滤波器后得到的图, 右图为高斯低通滤波器.

![](report_pic/0302.png)

更改高斯低通滤波器的半径(方差, D0), 可以发现高斯低通滤波器的半径越小, 图像越模糊, 图像的细节越不清晰.

![](report_pic/0303.png)

上图显示了不同半径的高斯低通滤波器的频谱图, 白色区域为滤波器允许通过的频率, 允许通过的频率为低频率.

半径越大, 白色区域的面积越大, 通过的频率的范围就越广, 能允许更高的频率通过. 

## 04-04 Highpass Filtering Using a Lowpass Image
### 问题内容
	(a) Subtract your image in Project 04-03(b) from the original to obtain a sharpened image, as in Eq. (4.4-14). You will note that the resulting image does not resemble the Gaussian highpass results in Fig. 4.26. Explain why this is so.

	(b) Adjust the variance of your Gaussian lowpass filter until the result obtained by image subtraction looks similar to Fig. 4.26(c). Explain your result.
### 技术讨论
	- 锐化图像
	原图与其进行低通滤波得到的图像进行相减, 得到锐化图像.
	- 高斯高通滤波器
	高通滤波器在频域内的函数等于1减去其对应的低通滤波器在频域内的函数
### 结果分析
![](report_pic/0401.png)

	观看结果图像, 两张图像的底色都为黑色.
	
	锐化图像A与原图经过高斯高通滤波器后得到的图像B差异不明显.

	然而矩阵A-矩阵B的结果不是零矩阵, 说明两张图像存在差异.

	通过公式推导: 

![](report_pic/0402.png)

	随着高斯低通滤波器的方差增大, 低通滤波器允许通过更多的频率, 意味着对应的高通滤波器通过的频率范围在缩小.
	
	经过高通滤波器后, 得到的图像的细节越来越少.  

## 04-05 Correlation in the Frequency Domain 
### 问题内容
	Download Figs. 4.41(a) and (b) and duplicate Example 4.11 to obtain Fig. 4.41(e). Give the (x,y) coordinates of the location of the maximum value in the 2D correlation function. There is no need to plot the profile in Fig. 4.41(f).
### 技术讨论
	- 图像间相关性公式
	- 零延拓
### 结果分析
![](report_pic/0501.png)

* 若令f为原图(存在要查找图像的图), g为掩模(需要查找的图像), 两张图片进行零延拓后大小为MxN, 需要查找的图像在原图的左上角位置为(a,b).

  两图计算出的相关性系数的最大值的位置为(M - a, N - b) 

* 若令g为原图(存在要查找图像的图), f为掩模(需要查找的图像), 两张图片进行零延拓后大小为MxN, 需要查找的图像在原图的左上角位置为(a,b).

  两图计算出的相关性系数的最大值的位置为(a, b) 
* 无论原图和掩模是否进行中心化, 两图的相关性系数不变. 

## 检验谱平面随着图像旋转而旋转的性质
### 问题内容
	观察图像旋转时谱平面和旋转图像的关系
### 技术讨论
- 公式推导
### 结果分析
![](report_pic/r.png)

- 可以看见图像旋转时, 谱平面也旋转, 而且谱平面旋转的角度与方向与空间域中的图像的旋转的角度与方向一致.
