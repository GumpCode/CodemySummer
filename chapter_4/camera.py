from numpy import *
from PIL import Image
from scipy import linalg

class Camera(object):

    def __init__(self,P):
        self.P = P
        self.K = None
        self.R = None
        self.t = None
        self.c = None

    def project(self, X):

        x = dot(self.P, X)
        for i in range(3):
            x[i] /= x[2]
        return x


def rotation_matrix(a):
    R = eye(4)
    R[:3,:3] = linalg.expm([[0, -a[2], a[1]], [a[2], 0, -a[0]],[-a[1],a[0],0]])
    return R

def factor(self):

    K,R = linalg.rq(self.P[:,:3])
    T = diag(sign(diag(K)))
    if linalg.det(T) < 0:
        T[1,1] *= -1

    self.K = dot(K,T)
    self.R = dot(T,R)
    self.t = dot(linalg.inv(self.K), self.P[:,:3])

    return self.K, self.R, self.t

def center(self):
    if self.c is not None:
        return self.c
    else:
        self.factor()
        self.c = -dot(self.R.T, self.t)
        return self.c
