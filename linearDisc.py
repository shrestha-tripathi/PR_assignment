import numpy as np
from numpy.linalg import inv

def inputMat(row, col): 
    mat = []
    
    for i in range(row):
        mat.append([])
        for j in range(col):
            mat[i].append(j)
            print("element[", i+1,"][", j+1, "]")
            mat[i][j] = float(input())
            
    return mat

def matrixMul(A, B):
    res = []
        
    for i in range(len(A)):
        res.append([])
        for j in range(len(B[0])):
            res[i].append(j)
            for k in range(len(B)):
                res[i][j] += A[i][k] * B[k][j]  
    return res


'''
linearDisc() computes the linear discriminant function value
for a given data point in d-dimension denoted by 'dim'

'''
def linearDisc(x, prior, mean, cov):
    XminusM = []    #to store the matrix of (x-mean)
    XminusM_ = []   #to store the matrix of (x-mean)'
    dim = len(x)
    
    for i in range(dim):
        XminusM.append([])
        for j in range(1):
            XminusM[i].append(j)
            XminusM[i][0] = x[i][0] - mean[i][0]    
    
    XminusM_ = np.transpose(XminusM)    #transpose of (x-mean) matrix
    inv_cov = inv(cov)                  #inv_cov holds inverse of covariance matrix
    
    #temp stores the multiplication matrix of (x-mean)' and inverse of covariance
    temp = matrixMul(XminusM_, inv_cov)
    #tempTwo stores the multiplication result of temp and (x-mean) matrix
    tempTwo = matrixMul(temp, XminusM)
    
    value = ((-1/2) * tempTwo[0][0]) + np.log(prior)
    
    return value


def quadDisc(x, prior, mean, cov):
    XminusM = []    #to store the matrix of (x-mean)
    XminusM_ = []   #to store the matrix of (x-mean)'
    dim = len(x)
    
    for i in range(dim):
        XminusM.append([])
        for j in range(1):
            XminusM[i].append(j)
            XminusM[i][0] = x[i][0] - mean[i][0]    
    
    XminusM_ = np.transpose(XminusM)    #transpose of (x-mean) matrix
    inv_cov = inv(cov)                  #inv_cov holds inverse of covariance matrix
    
    #temp stores the multiplication matrix of (x-mean)' and inverse of covariance
    temp = matrixMul(XminusM_, inv_cov)
    #tempTwo stores the multiplication result of temp and (x-mean) matrix
    tempTwo = matrixMul(temp, XminusM)
    
    value = ((-1/2) * tempTwo[0][0]) - ((1/2)*np.log(np.linalg.det(cov))) + np.log(prior)
    
    return value
