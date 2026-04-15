#Los sets son mutables(se pueden modificar), desorganizados, y sin elementos duplicados
conjunto = set(['Dato 01', 'Dato 02'])
conjunto.add('Dato 03')
print(conjunto)

#Los frozensets no se pueden modificar, son sets congelados
conjunto_congelado = frozenset(['Dato 01', 'Dato 02'])
#!Nos muestra un error de atributo al ejecutarlo
conjunto_congelado.add('Dato 03')
