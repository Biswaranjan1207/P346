import numpy as np
import math
import mylibrary.eigen as e

A=np.matrix([[1,-2,0,5],[0,7,1,5],[0,4,4,0],[0,0,0,2]])
x0=np.matrix([1.0,0.0,1.0,1.0])#initial guess eigenvector
xk=np.matrix([0.0,0.0,0.0,0.0])
lambda1,xk=(e.eig(A,x0,xk))
print("The dominant eigen value corresponding to the given matrix:",round(lambda1,3))
sum=0
for i in range (0,3):
    sum+=(xk[0,i]**2)
sum1=math.sqrt(sum)
for i in range (0,3):
    xk[0,i]=(xk[0,i]/sum1)
print("The normalized eigenvector corresponding to the dominant eigenvalue:\n",xk)

##OUTPUT
#The dominant eigen value corresponding to the given matrix: 8.0
#The normalized eigenvector corresponding to the dominant eigenvalue:
#[[-0.19802675  0.69309865  0.6931087   0.        ]]