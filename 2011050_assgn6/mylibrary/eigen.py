import math
import numpy as np

def eig(A,x0,xk):
    k=500
    y=np.matrix(x0)
    for i in range (0,k):
        sum=0
        for j in range (0,3):
            sum+=y[0,j]*x0[0,j]
        xky=(sum)
        for l in range (0,3):
            sum=0
            for j in range (0,3):
                sum+=A[l,j]*x0[0,j]
            xk[0,l]=(sum)
        x0=np.matrix(xk)
        sum=0
        for j in range (0,3):
            sum+=y[0,j]*xk[0,j]
        xk1y=(sum)
        if i==0:
            lambda0=(sum)
        if i>0 :
            if xky==0:
                break
            lambdak=xk1y/xky
            if abs(lambdak-lambda0)<10**-3:
                break
            lambda0=lambdak
    return lambdak,xk