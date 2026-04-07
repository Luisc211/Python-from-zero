#Pedirle un dato por teclado al usuario
name = input("What's your name: ")
#Imprimimos el dato por pantalla
print(name)
print(f"The name is:  {name}")

#Pidiendo datos númericos
#Enteros o int
age = input("How old are you: ")
age = int(age) * 2 #Convertimos el dato a un número entero, ya que por defecto es string
print(age)

#Flotantes o float
stature = input("What's your stature: ")
stature = float(stature) * 2
print(stature)