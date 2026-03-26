#Operador AND (&):
#El operador logico and compara dos resultados, para que devuelva True deben cumplirse ambas condiciones, si se
#cumple uno, pero otro no devolvera falso, y si ninguna se cumple claramente devolvera falso también.
resultado1_and = True & True       #Devuelve True ya que ambas son True
resultado2_and = True & False     #Devuelve False, ya que una de las condiciones no se cumple
resultado3_and = False & True     #Devuelve False, ya que una de las condiciones no se cumple
resultado4_and = False & False    #Devuelve False, ya que ambas opciones son falsas

#Operador OR (|):
#El operador logico OR compara dos opciones, y basta con que una de las dos opciones se cumpla para que nos de como resultado TRUE, es decir si opcion1 o opcion2 = True, si ninguna se cumple entonces si nos dara resultado false
resultado1_or = True | True     #Devuelve True ya que ambas opciones son verdaderas
resultado2_or = True | False   #Devuelve True ya que basta con que na de las opciones sea verdadera
resultado3_or = False | True   #Devuelve True ya que basta con que na de las opciones sea verdadera
resultado4_or = False | False  #Devuelve False ya que ahora si ambas opciones son falsas

#Operador NOT:
#Si no es verdadero es falso, y si no es falso es verdadero
resultado1_not = not True  #Devuelve Falso, ya que no es verdadero
resultado2_not = not False #Devuelve Verdadero ya que no es falso

#Imprimimos resultados por pantalla
print("---Operador AND---")
print(resultado1_and)
print(resultado2_and)
print(resultado3_and)
print(resultado4_and)
print("---Operador OR---")
print(resultado1_or)
print(resultado2_or)
print(resultado3_or)
print(resultado4_or)
print("---Operador NOT---")
print(resultado1_not)
print(resultado2_not)
#Nota: Todas las variables deben tener un nombre distinto, ya que se sobreescriben, y tuve ese error