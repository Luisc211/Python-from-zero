igual_que = 5 == 6         #Devuelve False, ya que 5 no es igual a 6
distinto_de = 5 != 6       #Devuelve True, ya que es verdadero que 5 es diferente a 6
mayor_que = 5 > 6          #Devuelve False: Ya que 5 no es mayor que 6
menor_que = 5 < 6          #Devuelve True: Ya que 5 si es menor que 6
mayor_o_igual_que = 5 >= 6 #Devuelve False: Ya que ninguna de las condiciones se cumple         
menor_o_igual_que = 5 <= 6 #Devuelve True: Porque basta con que una de las condiciones se cumpla (OR), menor o igual
print(igual_que)
print(distinto_de)
print(mayor_que)
print(menor_que)
print(mayor_o_igual_que)
print(menor_o_igual_que)

#Comparaciones combinadas
a = 5
b = 10
c = 20
print(a+b == c) #Debe imprimir false, ya que a+b=15 y c es 20, 15 y 20 no son iguales

#Comparando datos escritos en campos de texto con datos almacenados en base de datos
usuario_de_base_de_datos = "Luis Carlos"
usuario_escrito = "Luis Carlos"
print(usuario_de_base_de_datos == usuario_escrito) #Imprime false: Los dos usuarios no son iguales
contraseña_almacenada = "587963adwef"
contraseña_escrita = "587963adwef" 
print(contraseña_almacenada == contraseña_escrita)#Imprime True: No importa el tipo de comillas, siempre que sea string