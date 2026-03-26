#Las variables se declaran y se definen, son espacios de memoria en los que almacenamos datos de diferentes tipos
nombre = "Luis Carlos"
edad = 31
profesion = "programador"

#Concatenación: Agregamos f por delante
saludo = f"Hola, {nombre} tienes {edad}  "  
print (saludo)

#Operadores de pertenencia (in/ not in)
#Como resultado obtenemos true, ya que Luis si esta en saludo
print("Luis" in saludo)
#Como resultado obtenemos false, ya que profesion no lo ibncluimos en el saludo
print(profesion in saludo)
#Obtenemos False, ya que no es cierto que Luis no este en saludo
print("Luis" not in saludo)
#Obtenemos True, ya que es verdadero que profesion no esta en saludo
print(profesion not in saludo)

#snake_case recomendado