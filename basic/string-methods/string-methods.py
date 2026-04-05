string1 = "Hello, I'm Luis"
string2 = "Welcome to Canada"

#Metodos de cadena: 
#Metodo que convierte todo un texto a mayuscula
mayusc = string1.upper()
#Metodo que convierte todo un texto a minuscula
minusc = string2.lower()
#Metodo que convierte la primer letra  en mayuscula
primer_letra_mayusc = string1.capitalize()

#Metodo para buscar cadena dentro de cadena, debemos darle el parámetro que necesitamos buscar,
#devuelve la posición en la que se ubica, arrancando desde cero, si no hay resultados devuelve -1
busqueda_find = string1.find("Hello")
#Busqueda index: Funciona igual que find, solo que si no encuentra resultados nos muestra una excepción
busqueda_index = string2.index("u")

#Consulta si el dato es númerico, de serlo lanza True, de no serlo lanza False
es_numerico = string1.isnumeric()
#Consulta si el dato es alfa númerico, si tienes espacios lanzara Flase, ya que solo admite caracteres de la A a la Z
es_alfanumerico = string1.isalpha()

#Metodo para buscar cuantas veces se repite, o se encuentra por ejemplo la letra a dentro de la cadena 1, si no encuentra resultados, mostrara 0
contar_coincidencia = string2.count("a")
#Cuenta la cantidad de caracteres de una cadena
contar_caracteres = len(string1)

#Metodo para buscar si una cadena empieza con otra cadena o parametro dado, si empieza
#con el parametro dado muestra True, si no es asi, muestra false
empieza_con = string1.startswith("H")
#Metodo para buscar si una cadena termina con otra cadena o parametro dado, si termina
#con el parametro dado muestra True, si no es asi, muestra false
empieza_con = string1.endswith("k")


#Reemplaza, debemos darle como parámetros lo que deseamos reemplazar, y el nuevo valor, en caso de 
#no encontrar devolvera el valor antiguo
new_string = string1.replace("Hello", "Hi")

#Separara cada cadena cada vez que haya una coma, y la convertira en una lista
cadena_separada = string1.split(",")