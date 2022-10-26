#interpolation by lagrange method
def inter(x,y,a):
    n=len(x)
    p=1
    r=0
    for i in range(n):
        for j in range(n):
            if j!=i:
                p*=(a-x[j])/(x[i]-x[j])
        r+=p*y[i]
        p=1
    print("The value of f(x) at x=",a,"is:",r)
inter([2,3,5,8,12],[10,15,25,40,60],4)
inter([1951,1961,1971],[2.8,3.2,4.5],1969)
            
