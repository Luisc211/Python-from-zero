#El desempaquetado (unpacking) en Python es una técnica muy útil que no permite extraer valores de estructuras como listas, tuplas o diccionarios directamente en variables de forma limpia y elegante.
# ! Regla importante: El número de variables debe coincidir con el número de elementos:
#Podemos asignar los valores de una lista o tupla a varias variables:
data_in_list = ['Luis', 'Carrillo', 30]
name, last_name, age = data_in_list

data_in_tuple = ('Bogotá','Colombia')
city, country = data_in_tuple

print(f"""
    Nombre(s): {name}
    Apellidos(s): {last_name}
    Edad: {age}
    Ciudad: {city}
    País: {country}
    """)