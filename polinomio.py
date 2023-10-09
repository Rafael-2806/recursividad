
# f(x)= 3x^2-x^2+2x-1= x(3x^2-2x+2)-1
#lista f [-1,2,-1,3]. El primer elemento es el termino independiente que se suma, se multiplica por x que es por el que has sacado factor comun

def calcular(f,x):
    if len(f)==0:
        return 0
    else:
        return calcular(f[1:],x)*x+f[0]
    
print(calcular([-1,2,-1,3],3))

