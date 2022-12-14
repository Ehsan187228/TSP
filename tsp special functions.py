import tsplib95
import numpy as np
import sys 
import math
from array import *
problem = tsplib95.load('/Users/ehsan/Desktop/tspdata/att48.tsp.txt')
nodes = len(list(problem.get_nodes()))
np.set_printoptions(threshold=sys.maxsize)
A = []
for a in range(1, 48):
     for b in range(1, 48):
          edge = a, b
          weight = problem.get_weight(*edge)
          A.append(weight)
array = np.array(A)
n = array.size
N = round(math.sqrt(n))
Matrix = array.reshape((N,N))
print(Matrix)


    
