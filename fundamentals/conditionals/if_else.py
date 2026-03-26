#If condicion
    #Acción


edad = 17
if edad >= 18:
    print("Eres mayor de edad")
    #El codigo escrito en este nivel de tabulación hace parte del if
else :
    print("Eres menor de edad")
    #El código escrito en este nivel de tabulación hace parte del else
#El código escrito en este nivel de tabulación no hace parte de ninguna condicional


#Comparando contraseña almacenada, con la contraseña ingresada por el usuario, si es correcta inicia sesió, si no es correcta imprime el mensaje de que debe intentar nuevamente
contraseña_almacenada = "059dt6/#aV"
contraseña_escrita = "059dt6/#aV"
if contraseña_almacenada == contraseña_escrita:
    print(".........Iniciando sesión........")
else:
    print("Contraseña incorrecta, intenta nuevamente")