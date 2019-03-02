'''
@author:    VIKAS TYAGI
            17MCMC03
            
Description :   This file computes the predicted values for the sample points for iris 
                dataset and computes empirical error for all the three cases
                LDF is used for CASE I and CASE II
                QDF is used for CASE III
'''

import pandas as pd
import linearDisc as disc
import numpy as np
from numpy import mean, var, cov

dim = 4

def classLabel(p, q, r):
    if(p > q) and (p > r):
        value = "Iris-setosa"
    elif(q > p) and (q > r):
        value = "Iris-versicolor"
    else:
        value = "Iris-virginica"
    return value

def toList(mat):
    res = []
    
    for i in range(dim):
        res.append([])
        for j in range(1):
            res[i].append(j)
            res[i][j] = mat[i]
            
    return res


dataset = pd.read_csv("Iris.csv")
classNum = np.array(dataset.iloc[:150, 4:].values).tolist()

'''
feature values for class one as clsOne and
feature values for class two as clsTwo and 
feature values for class three as clsThree
'''
clsOne = dataset.iloc[:50, :-1].values
clsTwo = dataset.iloc[50:100, :-1].values
clsThree = dataset.iloc[100:150, :-1].values

'''
feature values matrix for different classes
'''
x1_clsOne = dataset.iloc[:50, 0:1].values
x2_clsOne = dataset.iloc[:50, 1:2].values
x3_clsOne = dataset.iloc[:50, 2:3].values
x4_clsOne = dataset.iloc[:50, 3:4].values

x1_clsTwo = dataset.iloc[50:100, 0:1].values
x2_clsTwo = dataset.iloc[50:100, 1:2].values
x3_clsTwo = dataset.iloc[50:100, 2:3].values
x4_clsTwo = dataset.iloc[50:100, 3:4].values

x1_clsThree = dataset.iloc[100:150, 0:1].values
x2_clsThree = dataset.iloc[100:150, 1:2].values
x3_clsThree = dataset.iloc[100:150, 2:3].values
x4_clsThree = dataset.iloc[100:150, 3:4].values

'''
mean value matrix for class one as meanOne and
mean value matrix for class two as meanTwo and
mean value matrix for class three as meanThree
'''

#mean() function of numpy computes mean along column with axis = 0
meanOne = mean(clsOne,axis = 0)     
temp = meanOne.tolist()
meanOne = toList(temp)

meanTwo = mean(clsTwo, axis = 0)
temp = meanTwo.tolist()
meanTwo = toList(temp)

meanThree = mean(clsThree, axis = 0)
temp = meanThree.tolist()
meanThree = toList(temp)

del temp    #deleting the temp variable

'''
CASE I : common variance is taken as average of variances of all 
         classes where non diagonal elements are zero
         varMat represents matrix for this case
'''
var_x1 = (var(x1_clsOne) + var(x1_clsTwo) + var(x1_clsThree))/3.0
var_x2 = (var(x2_clsOne) + var(x2_clsTwo) + var(x2_clsThree))/3.0
var_x3 = (var(x3_clsOne) + var(x3_clsTwo) + var(x3_clsThree))/3.0
var_x4 = (var(x4_clsOne) + var(x4_clsTwo) + var(x4_clsThree))/3.0

avgVar = (var_x1 + var_x2 + var_x3 + var_x4)/4.0
varMat = [[avgVar, 0, 0, 0],
          [0, avgVar, 0, 0],
          [0, 0, avgVar, 0],
          [0, 0, 0, avgVar]]

'''
CASE II : common covariance matrix is taken as average of covariance 
          matrix of all classes
          covariance represents matrix for this case
'''
cls_One_Trans = np.transpose(clsOne)
cls_Two_Trans = np.transpose(clsTwo)
cls_Three_Trans = np.transpose(clsThree)
covOne = cov(cls_One_Trans).tolist()
covTwo = cov(cls_Two_Trans).tolist()
covThree = cov(cls_Three_Trans).tolist()

covariance = ((np.array(covOne) + np.array(covTwo) + np.array(covThree))/3.0).tolist()

'''
CASE III : all covariances matrix are seperate
           covOne, covTwo, covThree represent covariance matrix for
           class One, Two, Three respectively
'''

prior = [[0.3333],
         [0.3333],
         [0.3334]]      #stores prior probability for classes

g = []      #stores discriminant function value 
for i in range(3):
    g.append([])
    g[i] = 0

predicted_caseOne = []
for i in range(150):
    predicted_caseOne.append([])
    for j in range(1):
        predicted_caseOne[i].append(j)
        predicted_caseOne[i][j] = 0

predicted_caseTwo = []
for i in range(150):
    predicted_caseTwo.append([])
    for j in range(1):
        predicted_caseTwo[i].append(j)
        predicted_caseTwo[i][j] = 0
        
predicted_caseThree = []
for i in range(150):
    predicted_caseThree.append([])
    for j in range(1):
        predicted_caseThree[i].append(j)
        predicted_caseThree[i][j] = 0

print("\n\nDecision rule is :\n if g[i] > g[j]  for all j, data point belongs to class i") 
   
print("\n\nCASE I: LDF for same covariance matrix where non diagonal elements are zero\n")
correct = 0 
error = 0
for count in range(150):
    point = dataset.iloc[count:count+1, :-1].values
    x = (np.transpose(point)).tolist()
    g[0] = disc.linearDisc(x, prior[0], meanOne, varMat)
    g[1] = disc.linearDisc(x, prior[1], meanTwo, varMat)
    g[2] = disc.linearDisc(x, prior[2], meanThree, varMat)
    
    predicted_caseOne[count][0] = classLabel(g[0], g[1], g[2]) 

    if(classNum[count][0] == predicted_caseOne[count][0]):
        correct = correct + 1
    else:
        error = error + 1
        
    count = count + 1
    
print("Number of correct predictions: ", correct, "\nNumber of false predictions: ", error)
print("Empirical error = ", round((error/150.0), 4) * 100, "%")  

print("\n\nCASE II : LDF for same covariance matrix where non diagonal elements are not zero\n")
correct = 0
error = 0
for count in range(150):
    point = dataset.iloc[count:count+1, :-1].values
    x = (np.transpose(point)).tolist()
    g[0] = disc.linearDisc(x, prior[0], meanOne, covariance)
    g[1] = disc.linearDisc(x, prior[1], meanTwo, covariance)
    g[2] = disc.linearDisc(x, prior[2], meanThree, covariance)
    
    predicted_caseTwo[count][0] = classLabel(g[0], g[1], g[2])
    
    if(classNum[count][0] == predicted_caseTwo[count][0]):
        correct = correct + 1
    else:
        error = error + 1
        
    count = count + 1
print("Number of correct predictions: ", correct, "\nNumber of false predictions: ", error)
print("Empirical error = ", round((error/150.0), 4) * 100, "%")

print("\n\nCASE III : QDF for different covariance matrix for different class\n")
correct = 0
error = 0    
for count in range(150):
    point = dataset.iloc[count:count+1, :-1].values
    x = (np.transpose(point)).tolist()
    g[0] = disc.quadDisc(x, prior[0], meanOne, covOne)
    g[1] = disc.quadDisc(x, prior[1], meanTwo, covTwo)
    g[2] = disc.quadDisc(x, prior[2], meanThree, covThree)
    
    predicted_caseThree[count][0] = classLabel(g[0], g[1], g[2])
    
    if(classNum[count][0] == predicted_caseThree[count][0]):
        correct = correct + 1
    else:
        error = error + 1
        
    count = count + 1
print("Number of correct predictions: ", correct, "\nNumber of false predictions: ", error)
print("Empirical error = ", round((error/150.0) * 100, 2), "%")


