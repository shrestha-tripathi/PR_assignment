import math
import numpy as np
import mahalanobis_euclidian as dist
from numpy.linalg import inv


def matrixMul(A, B, r1, c2):
    res = []
    for i in range(r1):
        res.append([])
    for i in range(r1):
        for j in range(c2):
            res[i].append(j)
            res[i][j] = 0
    
    for p in range(len(A)):
        for q in range(len(B[0])):
            for r in range(len(B)):
                res[p][q] += A[p][r] * B[r][q]
                
    
    return res


def input_point(dim):
        temp = ()
        x = 0
        y = 0
        z = 0
        print("Enter value of : \n")
        if(dim > 0):
            print("x-coordinate : ")
            x = float(input())
            temp = (x)
            if(dim > 1):
                print("\ny-coordinate : ")
                y = float(input())
                temp = (x, y)
                if(dim > 2):
                    print("\nz-coordinate : ")
                    z = float(input())
                    temp = (x, y, z)
        return temp

def euclidian_dist(dim,X,Y):

    distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
    return distance

def mahalanobis_dist(X,Mean,Cov):
    XminusM = []
    XminusM_ = []
    dim = len(Mean)
    
    for i in range(dim):
        XminusM.append([])
    
    for i in range(dim):
        for j in range(1):
            XminusM[i].append(j)
            XminusM[i][j] = 0
    
    for i in range(dim):
        XminusM[i][0] = X[i][0] - Mean[i][0]
    
    XminusM_ = np.transpose(XminusM)
    inv_cov = inv(Cov)
    
    temp = matrixMul(XminusM_, inv_cov, len(XminusM_), len(inv_cov[0]))
    distance = matrixMul(temp, XminusM, len(temp), len(XminusM[0]))
    value = (abs(distance[0][0]))**0.5
    return value


