#Las funciones built-in son funciones integradas que ya vienen configuradas de manera abstracta con python, y trabajand de manera interna: print, type, round, all, sum, min, max son funciones integradas

# La función integrada max encuentra el número mayor de un grupo de números, en arrays, list, dict, set
numbers = [55, 68, 1, 35]
max_number = max(numbers)
min_number = min(numbers)

float_number = round(12.954814, 2)

# La función bool nos devuleve false, si le damos elementos vacios, none, el número 0, y devuelve True si le damos numeros distintos a 0, true, o elementos no vacios
bool_result = bool({})
# La función all devuelve false, si un solo elemento de un iterable, esta vacio, oes falso, es decir todos deben ser verdaderos
all_result = all([0, True])
#La función sum suma todos los números de un iterable
sum_list = sum(numbers)
print(
    f"""
        El número mayor del grupo es: {max_number}
        El número menor del grupo es: {min_number}
        El número redondeado es, con dos decimales es: {float_number}
        El resultado de bool es: {bool_result}
        El resultado de all es: {all_result}
        El resultado de la función sum es: {sum_list}
"""
)
