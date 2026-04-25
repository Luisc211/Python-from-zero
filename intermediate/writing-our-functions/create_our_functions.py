#Creando una función simple
# def saludar():
#     print("Hola, Luis")
# saludar


#Función con parámetro
#La función recibe como parámetro el valor del nombre que el usuario ingrese
name = input("What's your name:")
def saludar(name):
    print(f"Hola {name}")

def sumar(a,b):
    return a+b


a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
result = sumar(a,b)
print(f"{a} + {b} = {result}")


