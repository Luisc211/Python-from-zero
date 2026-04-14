# Para ver los conceptos que hemos visto hasta este momento en nuestro curso. Variables, tipos de datos, operadores logicos, de comparación, operadores aritmeticos, condicionales, inputs, metodos de strings, de listas, inputs, el promedio es de 2.5h como mínimo, 7 horas como máximo, y promedio de 4 horas, en nuestro curso lo logramos en 1.5h, debemos crear un programa que porcese los datos y nos muestre
# A
# Diferencia en porcentaje entre el curso actual y
# El más rapido de los otros cursos (2.5h)
# El más lento de los otros cursos (7.0h)
# El promedio de los cursos (4h)
# B
# Teniendo en cuenta que la cantidad de crudo es de 5h en el promedio, y con edición se convierte en 4h,
# y el crudo del video de nuestro curso es de 3.5h y con edición se convierte a 1.5h, necesitamos saber que
# porcentaje de material inservible se remueve en ambos casos
# C
# Ver 10 horas de este curso a cuantas de otros cursos equivale, y ver 10 horas de otros cursos a cuantas de este curso equivale

min_time = 2.5
max_time = 7.0
average = 4
our_course = 1.5
# Tiempo total sin edición
raw_average = 5.0
raw_our = 3.5

#Formula: Restar la cantidad de tiempo de nuestro curso a la cantidad de tiempo de los demás cursos, luego dividir ese resultado entre la cantidad respectiva de los tiempos de los otros cursos, y multiplicarlo por 100
# Diferencia en porcentaje entre el curso actual y el más rapido de los cursos
min_time_our_course = round(((min_time - our_course) / min_time) * 100, 1)
# Diferencia en porcentaje entre el curso actual, y el más lento de los cursos
max_time_our_course = round(((max_time - our_course) / max_time) * 100, 1)
# Diferencia en porcentaje, entre nuestro curso, y el promedio de duración
average_our_course = round(((average - our_course) / average) * 100, 1)

# Material inservible removido
average_removal_of_unusable_material = round(
    ((raw_average - average) / raw_average) * 100, 1
)
our_course_removal_of_unusable_material = round(
    ((raw_our - our_course) / raw_our) * 100, 1
)

#Multiplicamos 10 * la cantidad respectiva que necesitamos comprar, luego dividimos entre la duración de nuestro curso.
ten_hours_this_course_min_time = round(((10 * 2.5) / 1.5), 1)
ten_hours_this_course_average = round(((10 * 4) / 1.5), 1)
ten_hours_this_course_max_time = round(((10 * 7) / 1.5), 1)

ten_hours_min_time_this_course = round(((10 * 1.5) / 2.5), 1)
ten_hours_average_this_course = round(((10 * 1.5) / 4.0), 1)
ten_hours_max_time_this_course = round(((10 * 1.5) / 7.0), 1)

print(
    f"""
    ================================
        DIFERENCIAS DE DURACIONES
    ================================
    Nuestro curso es: {min_time_our_course}% más corto que el más rapido de los cursos.
    Nuestro curso es: {max_time_our_course}% más corto que el más largo de los cursos.
    Nuestro curso es: {average_our_course}% más corto que el promedio de los cursos
    ===================================
        MATERIAL INSERVIBLE REMOVIDO
    ===================================
    El porcentaje de material inservible que se remueve en el promedio de los cursos es de: {average_removal_of_unusable_material}%
    El porcentaje de material inservible que se remueve en nuestro curso es de: {our_course_removal_of_unusable_material}%
    =======================
        EQUIVALENCIAS
    =======================
    Ver 10 horas de nuestro curso equivalen a tener que ver {ten_hours_this_course_min_time} horas del más rapido de otros cursos
    Ver 10 horas de nuestro curso equivalen a tener que ver {ten_hours_this_course_average} horas del promedio de otros cursos
    Ver 10 horas de nuestro curso equivalen a tener que ver {ten_hours_this_course_max_time} horas del más largo de los cursos
    =============================
        EQUIVALENCIA INVERSA
    =============================
    Ver 10 horas del más rapido de los otros cursos equivalen a ver {ten_hours_min_time_this_course} horas de nuestro curso
    Ver 10 horas del promedio de los otros cursos equivalen a ver {ten_hours_average_this_course} horas de nuestro curso
    Ver 10 horas del más largo de los otros cursos equivalen a ver {ten_hours_max_time_this_course} horas de nuestro curso
    """
)
