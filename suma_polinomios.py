#suma de polinomios
# P(x)=2x^3-1x^2+1x-3 el termino independiente en el 1º de la lista p[-3,1,-1,2] 1º orden 0, 2º orden1, 3º orden 2 osea al cuadradi y 4º al cubo
# Q(X)=     2x^2-1x+4    Q[4,-1,+2]
#resul=2x^3+1x^2+0x+1

def suma(p,q):
    if len(p)==0:
        return q
    elif len(q)==0:
        return p
        return p
    else:
        return [p[0]+q[0]] +suma(p[1:],q[1:])
    
print(suma([-3,1,-1,2],[4,-1,+2]))