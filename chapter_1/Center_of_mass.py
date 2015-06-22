from numpy import *
from scipy.ndimage import measurements, morphology
from pylab import *
from PIL import Image
import sys

im = array(Image.open('image.jpg').convert('L'))

figure(1)
im = 1*(im < 96)
im_open = morphology.binary_opening(im, ones((9,5)),iterations = 2)

labels, nbr_objects = measurements.label(im_open)
print "Number of objects:", nbr_objects
center = measurements.center_of_mass(labels,labels,range(1, nbr_objects+1))


imshow(labels)
print center
for item in center:
    plot(item[1], item[0], "o", color="white")
show()
