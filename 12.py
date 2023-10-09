# Desarrollar el algoritmo de Euclides para calcular el máximo común divisor (MCD) de dos número entero.

#Imaginate N=56 M=20 calculamos el resto que es 16. hacemos 20 entre y 16 y calculamos el resto que es 4. 16 entre 4 resto 0

def mcd(n,m):
   if m==0:
       return n
   else:
       return mcd(m,n%m)
   
#Desarrollar el algoritmo de Euclides para calcular también el mínimo común múltiplo (MCM) de dos número entero.
def mcm(n,m):
    return (n*m)/mcd(m,n%m)
   
print(mcd(56,20))
print(mcm(56,20))