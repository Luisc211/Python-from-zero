#Listas
        #Elemeto 1     Elemento 2           Elemento 3    Elemento 4
list = ["Luis Carlos", "Carrillo Tovar",    True,         1.69]
        #Indice 0        Indice 1           Indice 2      Indice 3
#Imprimimos por pantalla la lista 
print(list)
#Imprimimos el elemento 1 alojado en el índice 0 de la lista anterior
print(list[0])
#Modificando la lista, sí es valido
list[3] = False
print(list)

#Tuplas
#La tuplas alojan datos que no se podran modificar, son los que alojemos, mientras que las listas
#si son modificables
tuple = ("Luis Carlos", "Carrillo Tovar",    True,         1.69)
#Imprimos por pantalla la tupla
#Esto no es valido
#tuple[3] = False
print(tuple)

#Set o conjunto de datos: Podemos reconstruirlos, pero los datos no se pueden alterar, no permite repetir valores
#no nos deja acceder a un indice
set = {"Luis Carlos", "Carrillo Tovar",    True,         1.69}

#Los diccionarios, son como los JSON, y en vez de mostrar los elementos por número como llo hacen las listas
#lo muestran por el nombre asociado, no se ordena automatico como en las listas que se ordenan 0, 1, 2, 3....
dict = {
    #Key     #Value
    'name': 'Luis Carlos',
    'last name': 'Carrillo Tovar',
    'Work': True,
    'stature': 1.68,
    'duplicate data': 'Carrillo Tovar'
}
#Imprimimos lo que el diccionario tiene alojado en name
print(dict['name'])