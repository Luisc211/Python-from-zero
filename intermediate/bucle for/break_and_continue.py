fruits = ["Manzana", "Banana", "Naranja", "Pera", "Guayaba", "Uva", "Fresa"]


#La sentencia continue interrumpe la iteración del bucle, omite el elemento, y salta directamente al siguiente
for fruit in fruits:
    if fruit in "Naranja":
        continue
    print(
        f"""
        ---------SENTENCIA CONTINUE---------
        Me voy a comer una {fruit}"""
    )

#La sentencia break interrume el codigo en su totalidad
for fruit in fruits:
    if fruit in "Pera":
        break
    print(
        f"""
        ----------SENTENCIA BREAK----------
        Me voy a comer una {fruit}"""
    )
