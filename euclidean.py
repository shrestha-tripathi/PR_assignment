
import math
# Example points in 3-dimensional space...
dim = 0
print("Enter the dimension of the coordinate system : ")
input(dim)

def coordinate(dim):
    temp = ()
    x = 0
    y = 0
    z = 0
    print("Enter value of : \n")
    if(dim > 0):
        print("x-coordinate : ")
        input(x)
        temp = (x)
        if(dim > 1):
            print("\ny-coordinate : ")
            input(y)
            temp = (x, y)
            if(dim > 2):
                print("\nz-coordinate : ")
                input(z)
                temp = (x, y, z)
    return temp

print("First Point : ")
x = coordinate(dim)

print("Second Point : ")
y = coordinate(dim)


distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
print("Euclidean distance from x to y: ",distance)
