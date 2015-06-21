from numpy import *
from scipy.ndimage import measurements, morphology
from pylab import *
from PIL import Image

im = array(Image.open('test.jpg').convert('L'))

figure(1)
hist(im.flatten(), 128)

figure(2)
im = 1*(im < 64)
labels, nbr_objects = measurements.label(im)
print "Number of objects:", nbr_objects
imshow(labels)
show()
