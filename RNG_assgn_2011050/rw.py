import math
import matplotlib.pyplot as plt
import mylibrary.lcg as l
def rwalk(s1,s2,n):
    x=l.lcg(s1,n)#random number for x coordinate
    y=l.lcg(s2,n)#random number for y coordinate
    xlist=[0.0]
    ylist=[0.0]
    rms=0.0
    d=0.0
    disp=0.0
    x2=0.0
    y2=0.0
    #Loop to find the coordinates during the random wwalk
    for i in range (0,n) :
        x1=((2*x[i])-1)+x2
        y1=((2*y[i])-1)+y2
        xlist.append(x1)
        ylist.append(y1)
        d+=((x2-x1)**2 +(y2-y1)**2)
        x2=x1
        y2=y1
    rms=math.sqrt(d/n)
    disp=math.sqrt((x1**2)+(y1**2))
    output("The RMS distance for random walk of "+str(n)+" steps is : \n")
    output(str(rms)+'\n')
    output("The net displacement for random walk of "+str(n)+" steps is : \n")
    output(str(disp)+'\n')
    #plotting the simulation
    plt.title("\nRandom walk of "+str(n)+" steps")
    plt.plot(xlist,ylist,color='blue')
    plt.show()
#to write output file
def output(s):
    with open("C:\\Users\\91891\\OneDrive\\Desktop\\Codes\\rw.txt",'a') as file:
        file.write(s)
        file.close()
    return
with open("C:\\Users\\91891\\OneDrive\\Desktop\\Codes\\rw.txt",'w') as file:
    file.write("OUTPUT : \n")
    file.close()
    
rwalk(15,10,300)
rwalk(18,13,600)
rwalk(21,16,900)