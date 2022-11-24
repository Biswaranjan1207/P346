import math
def p(x):
    return x**4-x**3-7*x**2+x+6
def deriv():
    coeff=[1,-1,-7,1,6]
    for i in range(len(coeff)):
        coeff[i]= (len(coeff)-1-i)*coeff[i]
    print(coeff,end='\t')
deriv()
def sderiv():
    coeff=[1,-1,-7,1,6]
    for i in range(len(coeff)):
        coeff[i]= (len(coeff)-1-i)*(len(coeff)-2-i)*coeff[i]
    print(coeff,end='\t')
sderiv()