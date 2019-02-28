# -*- coding: utf-8 -*-
"""
@author: Shresth_Tripathi
"""
import numpy as np
import math
import matplotlib.pyplot as plt

def get_gaussian_random():
    m = 0
    while m == 0:
        m = round(np.random.random() * 100)
    numbers = np.random.random(int(m))
    summation = float(np.sum(numbers))
    gaussian = (summation - m/2) / math.sqrt(m/12.0)

    return gaussian


def generate_known_gaussian(dimensions):
    count = 100
    
    ret = []
    for i in range(count):
        current_vector = []
        for j in range(dimensions):
            g = get_gaussian_random()
            current_vector.append(g)

        ret.append( tuple(current_vector) )

    return ret

def main():
    known = generate_known_gaussian(3)
    target_mean = np.matrix([ [1.0], [5.0], [2.0]])
    target_cov  = np.matrix([[  1.0, 0.0, 0.0], 
                             [  0.0, 1.0, 0.0],
                             [  0.0, 0.0, 1.0]])

    [eigenvalues, eigenvectors] = np.linalg.eig(target_cov)
    l = np.matrix(np.diag(np.sqrt(eigenvalues)))
    Q = np.matrix(eigenvectors) * l
    x1_tweaked = []
    x2_tweaked = []
    x3_tweaked = []
    tweaked_all = []
    for i, j, k in known:
        original = np.matrix( [[i], [j], [k]]).copy()
        tweaked = (Q * original) + target_mean
        x1_tweaked.append(float(tweaked[0]))
        x2_tweaked.append(float(tweaked[1]))
        x3_tweaked.append(float(tweaked[2]))
        tweaked_all.append( tweaked )
    #plt.scatter(x1_tweaked, x2_tweaked, x3_tweaked)
    #plt.axis([-6, 10, -6, 10, -6, 10])
   # plt.hlines(0, -6, 10)
   # plt.vlines(0, -6, 10)
    #plt.show()
    ax = plt.axes(projection='3d')
    ax.scatter3D(x1_tweaked, x2_tweaked, x3_tweaked, c = x3_tweaked, cmap = 'Greens')
    
if __name__ == "__main__":
    main()
