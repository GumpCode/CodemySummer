from PIL import Image
from numpy import *
from scipy.ndimage import filters
from pylab import *

figure(1)
im = array(Image.open('test.jpg').convert('L'))
im1 = filters.gaussian_filter(im, 1.5)
gray()
im1 = im - im1
imshow(im1)
axis('equal')
axis('off')

figure(2)
im = array(Image.open('test.jpg'))
im2 = filters.gaussian_filter(im, 4)
im2 = im - im2
imshow(im2)
axis('equal')
axis('off')
show()

