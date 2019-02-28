
import pandas as pd
import numpy as np
import discriminant as dis
from numpy import mean,cov

'''importing datset'''
dataset = pd.read_csv("d3.csv")


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
One = meanOne.tolist()

meanOne = []
for i in range(3):
    meanOne.append([])
    
for i in range(3):
    for j in range(1):
        meanOne[i].append(j)
        meanOne[i][j] = One[i]
        
        
meanTwo = mean(clsTwo, axis = 0)
Two = meanTwo.tolist()

meanTwo = []
for i in range(3):
    meanTwo.append([])
    
for i in range(3):
    for j in range(1):
        meanTwo[i].append(j)
        meanTwo[i][j] = Two[i]
        

'''
covariance matrix for class one as covOne
covariance matrix for class two as covTwo
'''

x_One_Trans = np.transpose(clsOne)
x_Two_Trans = np.transpose(clsTwo)
covOne = cov(x_One_Trans)
covOne = covOne.tolist()
covTwo = cov(x_Two_Trans)
covTwo = covTwo.tolist()


#dim = int(input("enter the dimession of the sample space : "))
dim = 3
countClass = int(input("enter number of class labels : "))

prior = []
print("enter prior probability of : ")
for i in range(countClass):
    prior.append([])
    print("\nclass ", i+1, " : ")
    prior[i] = float(input())

g = []
for i in range(countClass):
    g.append([])
    g[i] = 0


print("Enter point value in space : ")
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
g[0] = dis.discFunc(x, prior[0], meanOne, covOne, dim)
g[1] = dis.discFunc(x, prior[1], meanTwo, covTwo, dim)

    
for i in range(countClass):
    print("g[", i+1, "] = ",g[i])
    
    
if(g[0] > g[1]):
    print("point belongs to class 1")
else:
    print("point belongs to class 2")






