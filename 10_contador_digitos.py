#Desarrollar un algoritmo que cuente la cantidad de dígitos de un número entero.

def contador_digitos(n):
    if n<10:
        return 1
    else:
        return 1+contador_digitos(n//10)
    
print(contador_digitos(200))