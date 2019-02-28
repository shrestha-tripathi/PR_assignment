
import pandas as pd
import numpy as np
import discriminant as dis
import mahalanobis_euclidian as dist
from numpy import mean,cov

'''importing datset'''
dataset = pd.read_csv("d3.csv")


'''
feature values for class one as clsOne and
feature values for class two as clsTwo
'''
clsOne = dataset.iloc[:10, 0:-1].values
clsTwo = dataset.iloc[10:20, 0:-1].values
clsThree = dataset.iloc[20:30, 0:-1].values

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

meanThree = mean(clsThree, axis = 0)
Three = meanThree.tolist()

meanThree = []
for i in range(3):
    meanThree.append([])
    
for i in range(3):
    for j in range(1):
        meanThree[i].append(j)
        meanThree[i][j] = Three[i]
        
        

'''
covariance matrix for class one as covOne
covariance matrix for class two as covTwo
'''

x_One_Trans = np.transpose(clsOne)
x_Two_Trans = np.transpose(clsTwo)
x_Three_Trans = np.transpose(clsThree)
covOne = cov(x_One_Trans)
covOne = covOne.tolist()
covTwo = cov(x_Two_Trans)
covTwo = covTwo.tolist()
covThree = cov(x_Three_Trans)
covThree = covThree.tolist()


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
g[0] = dist.mahalanobis_dist(x,meanOne,covOne)
g[1] = dist.mahalanobis_dist(x,meanTwo,covTwo)
g[2] = dist.mahalanobis_dist(x,meanThree,covThree)

    
for i in range(countClass):
    print("mahalanobis_distance from class " , i+1 , " = ",g[i])
    
    
if(g[0] > g[1] and g[0] > g[2]):
    print("\npoint belongs to class 1")
elif(g[1] > g[2] and g[1] > g[0]):
    print("\npoint belongs to class 2")
else:
    print("\npoint belongs to class 3")






