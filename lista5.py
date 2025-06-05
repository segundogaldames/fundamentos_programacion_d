#Ejemplo de listas dentro de listas
lista=[[1,2,3], [4,5,6], [7,8,9], [10,11,12]]

# imprimimos la lista completa
print("Lista completa sin for")
print(lista)
print("Inprime el primer componente de la lista padre")
# imprimimos la primer componente
print(lista[0])
print("Imprime primer elemento de la sublista")
# imprimimos la primer componente de la lista contenida
# en la primer componente de la lista principal
print(lista[0][0])
print("Mostramos los componentes de la primera sublista con un for")
# imprimimos con un for la lista contenida en la primer componente
for x in range(len(lista[0])):
    print(lista[0][x])
print("Mostramos toda la lista con sus sublistas con for")               
# imprimimos cada elemento entero de cada lista contenida en la lista
for k in range(len(lista)):
    for x in range(len(lista[k])):
        print(lista[k][x])