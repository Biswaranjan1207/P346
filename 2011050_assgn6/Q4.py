import numpy as np
import math
import mylibrary.eigen as e

A=np.matrix([[2,1,2],[2,2,-2],[3,1,1]])
x0=np.matrix([1.0,0.0,1.0])#initial guess eigenvector
xk=np.matrix([0.0,0.0,0.0])
lambda1,xk=(e.eig(A,x0,xk))
print("The dominant eigen value corresponding to the given matrix:",lambda1)
sum=0
for i in range (0,3):
    sum+=(xk[0,i]**2)
sum1=math.sqrt(sum)
for i in range (0,3):
    xk[0,i]=(xk[0,i]/sum1)
print("The normalized eigenvector corresponding to the dominant eigenvalue:\n",xk)

#OUTPUT
#The dominant eigen value corresponding to the given matrix: 4.0
#The normalized eigenvector corresponding to the dominant eigenvalue:
#[[0.70710678 0.         0.70710678]]
#So the normalized eigen vector:
#[0.70710678    0   0.70710678]
#[1/sqrt(2)     0   1/sqrt(2)]