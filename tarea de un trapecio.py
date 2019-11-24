import numpy as np

def funcion(x):
    y=pow(x,2)
    return y
b=float(input("Introduce el limite superior "))
a=float(input("Introduce el limite inferior "))
n=int(input("Introduce el numero de trapecio"))
x=np.zero([n+1])
h=(b-a)/n
x[0]=a
x[n]=b
suma=0

for i in np.arange(1,n):
    x[i]=x[i-1]+h
    suma=suma+funcion(x[i])

integral=(h/2)*(funcion(x[0])+2*suma+funcion(x[n]))
print("El resultado de la integral es: ",integral)