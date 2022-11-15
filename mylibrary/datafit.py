
import mylibrary.gajoel as gje
import numpy as np
import csv
import matplotlib.pyplot as plt
def polyfit(M,p):
  n=len(M)
  N=[]
  for i in range (0,p):
      r=[]
      for j in range (0,p):
          sum2=0.0
          for k in range(0,n):
              sum2+= (M[k,0]**(i+j))
          r.append(sum2)
      sum1=0.0
      for l in range (0,n):
          sum1+=((M[l,0]**i)*M[l,1])
      r.append(sum1)
      N.append(r)
  N=np.matrix(N)
  return N

def input(path):
  M=[]
  with open(path) as x:
    cr=csv.reader(x)
    next(cr)
    for line in cr:
      row=[]
      for n in line:
        row.append(float(n))
      M.append(row)
  return (np.matrix(M))

      
def main():
  p= "C://Users//91891//OneDrive//Desktop//Codes//q4inp.csv"
  A = input(p)
  n=4
  B=polyfit(A,n)
  C=gje.main(B)
  print("The equation corresponding to the data:\n")
  print("y = ", C[0,n], end='')
  D=[C[0,n]]
  for i in range (1,n):
    print(" + "+str(C[i,n])+" x^"+str(i),end='')
    D.append(C[i,n])
  print("\n")

