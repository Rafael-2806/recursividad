#Implementar una función para calcular la potencia dado dos 
# números enteros, el primero re- presenta la base y segundo el exponente.

def potencia(base, exponente):
    
    if exponente==0:
        return 1
    else:
        return  base *potencia(base, exponente-1)
    
print(potencia(3,2))
