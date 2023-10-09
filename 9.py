#Implementar una función para calcular el logaritmo entero de número n en una base b. Recuerde que:

#log b (n/b) = log b (n) - log b (b)

# n<b devuelve 0   si n>=b devuelve log(N/b,b)+1    si n=b devuelve 1

def logaritmo(n,b):
    if n < b:
        return 0

    else:
        return logaritmo(n//b,b)+1

logaritmo(16,2)

#Ponemos // para que te de un resultado entero