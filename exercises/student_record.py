#Debemos crear un programa que registre información de un estudiante, y calcule su rendimiento académico
#Debemos pedir al usuario por teclado (Nombres, apellidos, edad, tres notas), el programa debe procesar
#esa información, debe calcular el promedio de esas 3 notas, determinar si el estudiante aprobó, o reprobó
#(se arueba con un promedio > 60), determinar el rendimiento:
#90-100: "Excelente"
#70-89:  "Bueno"
#60-69:  "Suficiente"
#0-59:   "Insuficiente"
#Debemos guardar todo en un diccionario con calves para Nombre(s), apellido(s), la edad, las 3 notas, promedio, rendimiento, recordemos que la key para notas debe guardar las 3 notas, por último debemos mostrar un reporte por pantalla

#Solicitamos datos de entrada por teclado al usuario
name = input("Nombre(s): ")
last_name = input("Apellido(s): ")
age = int(input("Edad: "))
note_1 = float(input("Ingresa la nota 1: "))
note_2 = float(input("Ingresa la nota 2: "))
note_3 = float(input("Ingresa la nota 3: "))
#Formula para calcular el promedio de las 3 notas
average = round((note_1+note_2+note_3)/3,2) #Round redondea los decimales, y 2, es la cantidad de 
#decimales a conservar

#Condicionales, para determinar si aprobo, o desaprobo, así como el rendimiento
if average >= 90:
    status = "Aprobado"
    performance = "Excelente"
elif average >=70:
    status = "Aprobado"
    performance = "Bueno"
elif average >=60:
    status = "Aprobado"
    performance = "Suficiente"
else:
    status = "Desaprobado"
    performance = "Insuficiente"
#Guardamos los datos en un diccionario por teclado
student_store = {
    "name": name,
    "last_name": last_name,
    "age": age,
    "notes": [note_1, note_2, note_3],
    "average": average,
    "performance": performance,
    "status": status
}

#Imprimimos el reporte del estudiante por pantalla
print(f"""
==============================
    REPORTE DE ESTUDIANTE        
==============================
Nombre(s)  : {name}
Apellido(s)   : {last_name}
Edad   : {age}
Notas  : {note_1, note_2, note_3}
Promedio  :  {average}
Rendimiento  : {performance}
Estado  :  {status}
=============================
""")