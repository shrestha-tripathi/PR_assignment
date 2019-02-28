
import matplotlib.pyplot as plt
import pandas as pd

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

dataset = pd.read_csv("d3.csv")

x = dataset.iloc[:30, :1].values
y = dataset.iloc[:30, 1:2].values
#z = dataset.iloc[:30, 2:3]

ax.scatter(x, y, c = 'r', marker = 'o')
ax.set_xlabel('x1')
ax.set_ylabel('x2')
#ax.set_zlabel('x3')

plt.show()