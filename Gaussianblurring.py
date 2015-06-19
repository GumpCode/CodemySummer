from PIL import Image
from numpy import *
from scipy.ndimage import filters
from pylab import *

gaussian_list = [1, 4, 6, 8, 10]
number = 1

for value in gaussian_list:
    im = array(Image.open('test.jpg').convert('L'))
    im2 = filters.gaussian_filter(im, value)
    figure(number)
    imshow(im2)
    show()
    number = number + 1

#高斯模糊也就是对一副图像进行正态分布的卷积运算。由分布不为零的像素组成卷积矩阵，从而余原始图像做变换。换句话说，也就是高斯模糊时每个像素的值都是周围相邻像素值的加权平均。当我们采用不同的标准差时，图像会越来越模糊，这是因为当标准差越大，我们的加权矩阵半径越大，整个图像的模糊效果也就越大。
