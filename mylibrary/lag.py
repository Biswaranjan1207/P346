
import math
def ff(C,x):
    n=len(C)
    sum=0.0
    for i in range (0,n):
        sum+= C[i]*(x**(n-i-1))
    return sum
def fd(C):
    n=len(C)
    R=[0]*n
    for i in range (0,n-1):
        R[i+1] = C[i]*(n-i-1)
    return R

def lagu(C,x0,n):
    G=ff(fd(C),x0)/ff(C,x0)
    H=G**2-ff(fd(fd(C)),x0)/ff(C,x0)
    L=math.sqrt((n-1)*(n*H-G**2))
    if G==0 and L==0:
        return "end"
    a1=n/(G+L)
    a2=n/(G-L)
    if abs(a1)>abs(a2):
        a=a2
    else:
        a=a1
    x0-=a
    return x0
def deflat(C,x0):
    n=len(C)
    R=[0]*n
    for i  in range(1,n):
        j=C[i-1]
        R[i]=j
        C[i-1]=0
        C[i]+=(j*x0)
    return R

def solve(C):
    x0=1.5
    x=float(x0)
    n=1
    for i in range(1,100):
        if abs(ff(C,x))<10**-6:
            n+=1
            print("Root",n-1,":",x)
            C=deflat(C,x)
            if (ff(C,x))==0:
                return
            x=lagu(C,1.5,n)
            if x=="end":
                return
        else:
            x=lagu(C,x,n)