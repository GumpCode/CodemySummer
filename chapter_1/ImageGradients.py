from PIL import Image
from numpy import *
from scipy.ndimage import filters
from pylab import *

im = array(Image.open('test.jpg').convert('L'))

imx = zeros(im.shape)
filters.sobel(im, 1, imx)

imy = zeros(im.shape)
filters.sobel(im, 0, imy)

magnitude = sqrt(imx**2+imy**2)

figure(1)
imshow(magnitude)
axis('equal')
axis('off')
show()
