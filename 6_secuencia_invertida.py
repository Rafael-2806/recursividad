#Dada una secuencia de caracteres, obtener dicha secuencia invertida.

def invertir(secuencia):
    if len(secuencia)==0:
        return secuencia
    else:
        return secuencia[-1]+invertir(secuencia[:-1])

print(invertir('hola'))
    
    