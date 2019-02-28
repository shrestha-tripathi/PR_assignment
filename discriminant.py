# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 09:22:59 2019

@author: Shresth_Tripathi
"""
import numpy as np
from numpy.linalg import inv

def inputMat(row, col): 
    mat = []
    for i in range(row):
        mat.append([])
    
    for i in range(row):
        for j in range(col):
            mat[i].append(j)
            mat[i][j] = 0
            
    for i in range(row):
        for j in range(col):
            print("element[", i+1,"][", j+1, "]: ")
            mat[i][j] = float(input())
            
    return mat

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

def discFunc(X, Prior, Mean, Cov, dim):
    XminusM = []

    for i in range(dim):
        XminusM.append([])
    
    for i in range(dim):
        for j in range(1):
            XminusM[i].append(j)
            XminusM[i][j] = X[i][0] - Mean[i][0]
    
    XminusM_ = np.transpose(XminusM)
    inv_cov = inv(Cov)
    
    temp = matrixMul(XminusM_, inv_cov, len(XminusM_), len(inv_cov[0]))
    temp2 = matrixMul(temp, XminusM, len(temp), len(XminusM[0]))
    
    value = ((-1/2) * temp2[0][0]) - ((dim/2)*np.log(2*3.14159)) - ((1/2)*np.log(np.linalg.det(Cov))) + np.log(Prior)
    
    return value
        