from PIL import Image
from numpy import *
from scipy.ndimage import filters
from pylab import *

im = array(Image.open('DSC_3655.JPG').convert('L'))
figure(1)
im1 = filters.gaussian_filter(im, 1.5)
gray()
contour(im1, origin = 'image')
imshow(im1)
axis('equal')
axis('off')

figure(2)
im2 = filters.gaussian_filter(im, 4)
gray()
contour(im2, origin = 'image')
imshow(im2)
axis('equal')
axis('off')
show()

