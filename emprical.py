
import pandas as pd
import discriminant as dis
from numpy import mean, var
def toMatrix(M):
	mean = []
	for i in range(1):
		mean.append([])
	for i in range(1):
		for j in range(1):
			mean[i].append(j)
			mean[i][j] = M

	return mean

points = [[-5.01,1],[-0.91,2],[3.6,2],[-7.75,2],[-5.47,2],[7.18,2],[-2.51,1],[-2.25,1],[5.56,1],[1.03,1]]

dataset = pd.read_csv("d.csv")
correct = 0
error = 0
clsOne = dataset.iloc[:10, 0:-1].values
clsTwo = dataset.iloc[10:20, 0:-1].values

meanOne = mean(clsOne,axis = 0)
meanTwo = mean(clsTwo, axis = 0)



meanOne = toMatrix(meanOne)
meanTwo = toMatrix(meanTwo)


vOne = var(clsOne)
varOne = toMatrix(vOne)


        
vTwo = var(clsTwo) 
varTwo = toMatrix(vTwo)

dim = 1
countClass = 2

prior = []

for i in range(countClass):
    prior.append([])
    prior[i] = 0.5

for point in points:



	g = []
	for i in range(countClass):
	    g.append([])
	    g[i] = 0

	x = []
	for i in range(1):
		x.append([])
	for i in range(1):
		for j in range(1):
			x[i].append(j)
			x[i][j] = point[0]
	

	g[0] = dis.discFunc(x, prior[0], meanOne, varOne, dim)
	g[1] = dis.discFunc(x, prior[1], meanTwo, varTwo, dim)

	    	    
	if(g[0] > g[1]):
	    if(point[1] == 1):
	    	correct = correct + 1
	    else:
	    	error = error + 1
	else:
	    if(point[1] == 2):
	    	correct = correct + 1
	    else:
	    	error = error + 1

print("total misclassification %: ", (error/10)*100, "%")
