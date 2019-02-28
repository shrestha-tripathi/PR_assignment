
import numpy as np
from numpy.linalg import inv
m = int(input("enter row : "))
n = int(input("enter col :"))
mat = []

for i in range(m):
    mat.append([])

for i in range(m):
    for j in range(n):
        mat[i].append(j)
        mat[i][j] = 0

for i in range(m):
    for j in range(n):
        print("enter value : ")
        mat[i][j] = int(input())


print(mat)

print(np.linalg.det(mat))
print(inv(mat))