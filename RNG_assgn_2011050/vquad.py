import mylibrary.lcg as l
def vq():
    n=1000
    count=0
    seed=10
    #random numbers for different points
    x=l.lcg(seed,n)
    y=l.lcg(seed,n)
    z=l.lcg(seed,n)
    #Loop to count the number of points inside the quadrant of sphere
    for i,j,k in zip(x,y,z):
      if (i**2 + j**2 + k**2) <= 1:
        count = count+ 1
    V = count/n
    output('The volume of a quadrant of the sphere: '+str(V)+'\n')

def output(s):
    with open("C:\\Users\\91891\\OneDrive\\Desktop\\Codes\\vquad.txt",'a') as file:
        file.write(s)
        file.close()
    return
with open("C:\\Users\\91891\\OneDrive\\Desktop\\Codes\\vquad.txt",'w') as file:
    file.write("OUTPUT : \n")
    file.close()
    
vq()