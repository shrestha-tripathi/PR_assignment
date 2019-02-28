# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 21:32:16 2019

@author: Shresth_Tripathi
"""
import pandas as pd
import discriminant as dis
from numpy import mean, var

dataset = pd.read_csv("d.csv")


'''
feature values for class one as clsOne and
feature values for class two as clsTwo
'''
clsOne = dataset.iloc[:10, 0:-1].values
clsTwo = dataset.iloc[10:20, 0:-1].values

'''
mean value matrix for class one as meanOne and
mean value matrix for class two as meanTwo
'''
meanOne = mean(clsOne,axis = 0)


meanTwo = mean(clsTwo, axis = 0)


def toMatrix(M):
	
	mean = []
	for i in range(1):
		mean.append([])
	for i in range(1):
		for j in range(1):
			mean[i].append(j)
			mean[i][j] = M

	return mean
meanOne = toMatrix(meanOne)
meanTwo = toMatrix(meanTwo)
# meanOne = []
# for i in range(1):
#     meanOne.append([])
    
# for i in range(1):
#     for j in range(1):
#         meanOne[i].append(j)
#         meanOne[i][j] = One[i]
        
        
# meanTwo = []
# for i in range(1):
#     meanTwo.append([])
    
# for i in range(1):
#     for j in range(1):
#         meanTwo[i].append(j)
#         meanTwo[i][j] = Two[i] 
        

'''
covariance matrix for class one as covOne
covariance matrix for class two as covTwo
'''

vOne = var(clsOne)


varOne = toMatrix(vOne)

# varOne = []
# for i in range(1):
#     varOne.append([])
    
# for i in range(1):
#     for j in range(1):
#         varOne[i].append(j)
#         varOne[i][j] = vOne
        
vTwo = var(clsTwo) 


varTwo = toMatrix(vTwo)
# varTwo = []
# for i in range(1):
#     varTwo.append([])
    
# for i in range(1):
#     for j in range(1):
#         varTwo[i].append(j)
#         varTwo[i][j] = vTwo 
        


#dim = int(input("enter the dimession of the sample space : "))
dim = 1
countClass = int(input("enter number of class labels : "))

prior = []
print("Enter Priors Of: ")
for i in range(countClass):
    prior.append([])
    print("\nclass ", i+1, ": ")
    prior[i] = float(input())

g = []
for i in range(countClass):
    g.append([])
    g[i] = 0


print("Enter Point value in space : ")
x = dis.inputMat(dim,1)
'''
print("Enter the parameters of normal distribution :\n")
for i in range(countClass):
    print("for class", i+1)
    print("Mean : ")
    mean = dis.inputMat(dim, 1)
    
    print("Covariance Matrix :")
    cov = dis.inputMat(dim, dim)
'''    
g[0] = dis.discFunc(x, prior[0], meanOne, varOne, dim)
g[1] = dis.discFunc(x, prior[1], meanTwo, varTwo, dim)

    
for i in range(countClass):
    print("g[", i+1, "] = ",g[i])
    
    
if(g[0] > g[1]):
    print("\npoint belongs to class 1")
else:
    print("\npoint belongs to class 2")






