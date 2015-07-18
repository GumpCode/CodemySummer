from PIL import Image
from numpy import *
from pylab import *
from scipy import ndimage
import warp

im1 = array(Image.open('test.jpg').convert('L'))
im2 = array(Image.open('june1.jpg').convert('L'))

tp = array([[264,200,200,264],[40,36,300,300],[1,1,1,1]])
im3 = warp.image_in_image(im1, im2, tp)

figure()
gray()
imshow(im3)
axis('equal')
axis('off')
show()
