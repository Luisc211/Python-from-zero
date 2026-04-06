dictionary = {
    'name': 'Luis Carlos',
    'last name': 'Carrillo',
    'subs': 10000000
}
keys = dictionary.keys()
print(keys) #Imprime las claves o llaves, más no el valor alojado, dict_item
keys = dictionary.get("name") #Obtener el valor alojado en las llaves que le pidamos
print(keys)
#dictionary.clear()                                #Elimina todos los elementos del diccionario
#dictionary.pop('name', 'last name')               #Eliminando un objeto del diccionario

iterable_dictionary = dictionary.items()
print(dictionary)  #No se puede iterar
print(iterable_dictionary) #Se puede iterar, o recorrer el elemento