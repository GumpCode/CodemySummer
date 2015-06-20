from PIL import Image
from numpy import *
from scipy.ndimage import filters
from pylab import *

im = array(Image.open('test.jpg').convert('L'))
im1 = filters.gaussian_filter(im, 1.5)
im1 = im/im1
figure(1)
imshow(im1)
axis('equal')
axis('off')

show()

