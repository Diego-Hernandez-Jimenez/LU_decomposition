# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 23:17:31 2021

@author: Diego
"""

import numpy as np

A = np.array([[1,2,3,4],[17,22,27,8],[77,44,47,-494],[-10,1,7,63]])
b = np.array([-10,22,2106,-243])

# A = np.random.randint(0,100,9).reshape([3,3])
# b = np.random.randint(0,100,3)
A = np.array([[1,2,2],
              [3,-3,-2],
              [4,-1,-5]])
b = np.array([5,0,-10])

# A = np.array([[2,1,3],
#               [4,-1,0],
#               [10,12,34]])
# b = np.array([5,-11,84])
sol = np.linalg.solve(A,b)

#%%
startentry = 0
neg_multip = []
U = A.copy()
L = np.identity(A.shape[0])

for col in range(U.shape[1] - 1):
    startentry += 1 
    for row in range(startentry,U.shape[0]):
        multiplier = -U[row,col]/U[col,col]
        U[row] = U[row] + multiplier * U[col]
        L[row,col] = -multiplier

#%%

y = np.zeros(L.shape[0])
Lcols = L.shape[1]

for i in range(len(y)):
    y[i] = (b[i] - np.sum([L[i,j]*y[j] for j in range(Lcols)]))/L[i,i]
    
    
x = np.zeros(U.shape[0])
Ucols = U.shape[1]

for i in range(len(x)-1,-1,-1):
    x[i] = (y[i] - np.sum([U[i,j]*x[j] for j in range(Ucols)]))/U[i,i]
    
print(sol)
print(x)