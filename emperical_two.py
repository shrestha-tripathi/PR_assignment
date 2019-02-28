
import pandas as pd
import discriminant as dis
from numpy import mean,var,cov
import numpy as np

def toMatrix(M):
	mean = []
	for i in range(1):
		mean.append([])
	for i in range(1):
		for j in range(1):
			mean[i].append(j)
			mean[i][j] = M

	return mean

points = [[-5.01,-8.12,1],[-0.91,-0.18,2],[3.6,1.26,2],[-7.75,-4.54,2],[-5.47,0.50,2],[7.18,1.46,2],[-2.51,2.09,1],[-2.25,-2.13,1],[5.56,2.86,1],[1.03,-3.33,1]]


correct = 0
error = 0
dataset = pd.read_csv("d2.csv")


clsOne = dataset.iloc[:10, 0:-1].values
clsTwo = dataset.iloc[10:20, 0:-1].values


meanOne = mean(clsOne,axis = 0)
One = meanOne.tolist()

meanOne = []
for i in range(2):
    meanOne.append([])
    
for i in range(2):
    for j in range(1):
        meanOne[i].append(j)
        meanOne[i][j] = One[i]
        
        
meanTwo = mean(clsTwo, axis = 0)
Two = meanTwo.tolist()

meanTwo = []
for i in range(2):
    meanTwo.append([])
    
for i in range(2):
    for j in range(1):
        meanTwo[i].append(j)
        meanTwo[i][j] = Two[i]


x_One_Trans = np.transpose(clsOne)
x_Two_Trans = np.transpose(clsTwo)
covOne = cov(x_One_Trans)
covOne = covOne.tolist()
covTwo = cov(x_Two_Trans)
covTwo = covTwo.tolist()


#dim = int(input("enter the dimession of the sample space : "))
dim = 2
countClass = 2

prior = []

for i in range(countClass):
    prior.append([])
  
    prior[i] = 0.50


for point in points:



	g = []
	for i in range(countClass):
	    g.append([])
	    g[i] = 0

	x = []
	for i in range(2):
		x.append([])
	for i in range(2):
		for j in range(1):
			x[i].append(j)
			x[i][j] = point[i]
	

	g[0] = dis.discFunc(x, prior[0], meanOne, covOne, dim)
	g[1] = dis.discFunc(x, prior[1], meanTwo, covTwo, dim)

	    	    
	if(g[0] > g[1]):
	    if(point[2] == 1):
	    	correct = correct + 1
	    else:
	    	error = error + 1
	else:
	    if(point[2] == 2):
	    	correct = correct + 1
	    else:
	    	error = error + 1

print("total misclassification %: ", (error/10)*100, "%")
