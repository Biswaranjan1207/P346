#Non linear equations using regula falsi method
import math
def f(x):
    return math.log(x/2)-math.sin(5*x/2)
def refal(a0,b0):
    iter=0
    if f(a0)*f(b0)>0:
        print("Try another guess!!!")
    c0=b0-((b0-a0)*f(b0))/(f(b0)-f(a0))
    while abs(f(c0))>10**-6:
        c0=b0-((b0-a0)*f(b0))/(f(b0)-f(a0))
        if f(c0)*f(a0)<0:
            b0=c0
        elif f(c0)*f(b0)<0:
            a0=c0
        iter+=1
    print("No of iterations for regula falsi method:",iter)
    print("Required root using Regula falsi method:",c0)

    