#non linear equations (bisection method)
import math
def f(x):
    return math.log(x/2) - math.sin(5*x/2)
def bisect(a0,b0,e):
    a0=2
    b0=3
    e=0.000001
    ct=1
    condition=True
    while condition:
        c0=(a0+b0)/2
        if f(a0)*f(c0)<0:
            b0=c0
        else:
            a0=c0
        ct+=1
        condition=abs(f(c0))>e
    if f(a0)*f(b0)>0.0:
        print("Interval doesn't bracket the root...Try again with different guess!!!")
    else:
        bisect(a0,b0,e)
    print("No. of iterations:",ct)
    print('\n Required root using bisection method is:',c0)

bisect(2,3,0.000001)