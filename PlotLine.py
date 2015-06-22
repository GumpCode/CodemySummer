from PIL import Image
from numpy import *
from pylab import *
from scipy.ndimage import filters

im = array(Image.open("image.jpg").convert('L'))
im1 = filters.gaussian_filter(im, 1.5)
gray()
subplot(131)
c = contour(im1, origin = 'image', levels=[80])
print c
subplot(132)
contour(im1, origin = 'image', levels=[120])
show()
