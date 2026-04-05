#Crear una nueva lista con list, poco usado.
lista = list(['Hello', 'Luis', 31])

#Devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)


#Agregando nuevo elemento a la lista
lista.append("Colombian")
#Agregando nuevo elemento a la lista en un indice especifico
lista.insert(2, "Carlos")
#Agregando varios elementos nuevos a la lista
lista.extend(["Bogotá", 1.69])
#Eliminando un elemento de la lista por su indice, para eliminar el ultimo damos -1, -2 el anteultimo
#y así sucesivamente
lista.pop(0)
#Removiendo un elemento de la lista por su valor, si no encuentra el parámetro que le pasamos, no va a eliminar nada, y aparte nos lanzara una excepción
lista.remove("Luis")

#Ordena los elementos de forma ascendente, pero si hay cadenas de texto lanzara una expeción, primero los false, true, y los números, si usamos reverse= true, invierte el orden
lista.sort()
#Odena invertidamente la lista
lista.reverse()

#En las tuplas solo podemos buscar elementos y usar el index