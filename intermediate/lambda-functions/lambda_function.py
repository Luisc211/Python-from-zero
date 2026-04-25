# Las funciones lambda son funciones anonimas de una sola expresión, se usan cuando necesitamos una función pequeña y temporal sin necesidad de definirla formalmente con def, y estar a todo momento con return
# Sintaxis
# lambda argumentos: expresión

#Nombre Palabra clave lambda  parámetros operación o función
suma = lambda a, b: a + b
print(suma(3, 7))

#Comparación con def
def sumar (a, b):
    return a+b
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
#Invocamos a la función sumar
result = sumar(a,b)
#Imprimimos resultado
print(f"{a} + {b} = {result}")