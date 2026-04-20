#?Iterando una lista con for
animals_list = ["Cat", "Dog", "Crocodile", "Bird"]
# Recorriendo la lista animales
# for animal in animals_list:
#     print(f"En esta vuelta la variable es igual a: {animal}")

# Creamos una lista de números
numbers_list = [52, 40, 67, 20]
# Recorriendo la lista de números y multiplicando cada valor por 10
# for number in numbers_list:
#     result = number * 10
#     print(f"{number} multiplicado por 10 es igual a {result}")


for animal, number in zip(animals_list, numbers_list):
    print(f"Recorriendo la lista número 1: {animal}")
    print(f"Recorriendo la lista número 2: {number}")

# For in range con dos parámetros: El primer parámetro indica donde arranca, el segundo indica donde termina
for num in range(1, 20):
    print(
        f"""
        =====Lista in rango con dos parámetros=====
        {num}"""
    )
#For in range con un solo parámetro: Ese unico parámetro indica la cantidad de veces que se ejecutara el bucle for, arrancando de 0 a......
for num in range(15):
    print(
        f"""
    =====Lista in rango con un solo parámetro=====
    {num}
"""
    )
