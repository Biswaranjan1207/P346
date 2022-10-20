import mylibrary.lcg as l

def ar_ell():
    seed=10
    n=125
    x=l.lcg(seed,n)
    y=l.lcg(seed,n)
    count=0
    for i,j in zip(x,y):
        if (i**2+j**2)<=1:
            count+=1
    A=4*count/n #for 4 quadrants
    #Now since the semimajor axis is 2 units the area we need is going to be multiplied by 2
    a=2*A
    print('The area of the ellipse: '+str(a)+'\n')
ar_ell()