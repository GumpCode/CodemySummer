from PIL import Image
from numpy import *
from pylab import *

def imresize(im, sz):
    pil_im= Image.fromarray(unit8(im))

    return array(pil_im.resize(sz))


def histeq(im, nbr_bins=256):
    imhist,bins = histogram(im.flatten(), nbr_bins,normed=True)
    cdf = imhist.cumsum()
    cdf = 255* cdf /cdf[-1]

    im2 = interp(im.flatten(),bins[:-1], cdf)

    return im2.reshape(im.shape), cdf

def copute_average(imlist):

    averageim = array(Image.open(imlist[0],'f'))

    for imname in imlist[1:]:
        try:
            averageim += array(Image.open(imname))
        except:
            print imname + '...skipped'
    averageim /= len(imlist)

    return array(averageim, 'unit8')

def pca(X):
    num_data,dim = X.shape
    mean_X = X.mean(axis=0)
    X = X - mean_X

    if dim>num_data:
        M = dot(X,X.T)
        e,EV = linalg.eigh(M)
        tmp = dot(X.T,EV).T
        V = tmp[::-1]
        S = sqrt(e)[::-1]

        for i in range(V.shape[1]):
            V[:,i]/= S
    else:
        U,S,V = linalg.svd(X)
        V = V[:num_data]

    return V,S,mean_X
