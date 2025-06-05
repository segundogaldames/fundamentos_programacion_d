#eliminacion de elementos de una lista
lista=[]
for x in range(10):
    valor=int(input(f"Ingrese valor {x+1}:"))
    lista.append(valor)

print(f"La lista original es {lista}")

posicion=0
while posicion<len(lista):
    if lista[posicion]==5:
        lista.pop(posicion)
    else:
        posicion=posicion+1
    
print(f"La lista sin el cinco: {lista}")  