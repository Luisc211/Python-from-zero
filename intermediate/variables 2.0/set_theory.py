#A es super conjunto de b, o b es sub conjunto de a
conjunto_a = {1,3,5,7}
conjunto_b = {1,3,7}

resultado = conjunto_b.issubset(conjunto_a)
resultadob = conjunto_a.issuperset(conjunto_b)
diferente = conjunto_a.isdisjoint(conjunto_b) #Basta con que uno de los elementos se repita para que de falso que es diferente, solo si no hay un solo elemento igual dara True
print(resultado)
print(resultadob)
print(diferente)