import math
def p(x):
    return x**4-5*x**2+4

def deflat(C,x0):
    n=len(C)
    R=[0]*n
    for i  in range(1,n):
        j=C[i-1]
        R[i]=j
        C[i-1]=0
        C[i]+=(j*x0)
    print(R)
    return R
    

