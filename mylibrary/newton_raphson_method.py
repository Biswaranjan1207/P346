import math
from re import A
def f(x):
    return math.cos(x)-x**3
def fd(x):
    return -math.sin(x)-3*x**2
def newraph():
    x0=1
    iter=0
    a=f(x0)/fd(x0)
    while abs(f(x0)) > 10**-6:
        a=f(x0)/fd(x0)
        x0=x0-a
        iter+=1
    print("Total no of iterations:",iter+1)
    print("Required root is:",x0)
newraph()