ingreso_mensual = 10000
gastos_mensuales =8000


if ingreso_mensual >= 10000: #Si se cumple una condición
    print("Estas excelente economicamente")
elif ingreso_mensual > 5000: #Si no se cumplio la primera, pero le damos otra oportunidad o condición
    print("Estas bien economicamente")
else: #Si no se cumplio ni la primera, ni la segunda condición
    print("Eres pobre") 


#if anidados
#Si dos condiciones se cumplen
if ingreso_mensual>=10000:
    if gastos_mensuales <8000:
        print("-----Estas excelente economicamente, muy bien------")
    #Si se cumple otra condición
    elif ingreso_mensual-gastos_mensuales <= 1000:
        print("-----Cuidado te estas gastando casi to tu ingreso mensual, depronto no te alcanza----")
    #si ninguna de las condiciones anteriores se cumplio
    else:
        print("-------Uy :( -------estas en deficit-------)")