import mylibrary.integration as inte
import math
def f(x):
    thetam=math.pi/4
    a=math.sin(thetam/2)
    return 4*math.sqrt(1/9.8)*(1/(math.sqrt(1-((a)**2)*(math.sin(x))**2)))
def output():
    print("The value of T using Simpson method:",inte.simp(f,0,math.pi/2,10))
output()

##OUTPUT
#The value of T using Simpson method: 2.0873200174795916