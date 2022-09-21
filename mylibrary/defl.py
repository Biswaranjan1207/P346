import math
def p(x):
    return x**4-x**3-7*x**2+x+6

def deflat(coeff):
    x0=int(input("Enter x0:"))
    for i in range(0,len(coeff)-1):
        coeff[i+1]+=x0*coeff[i]
    coeff.pop()
    print(coeff, end='\t')
    
deflat([1,-1,-7,1,6])

