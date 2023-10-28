#Implementar una función que calcule la suma de todos los números enteros comprendidos 
# entre cero y un número entero positivo dado.

def calculo(n):
    if n==1:
        return 1
    else:
        return n+calculo(n-1)
    
print(calculo(3))