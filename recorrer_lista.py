
def mostrarlista(lista,index):
    if index !=len(lista):
        print(lista[index])
        mostrarlista(lista,index+1)
        
lista=[1,2,3,4,5]
print(mostrarlista(lista,0))