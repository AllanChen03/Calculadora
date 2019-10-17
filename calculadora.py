def Resta(Num1,Num2):
    return Num1 - Num2

def Suma(Num1,Num2):
    return Num1 + Num2

def Sumatoria(Num):
    if isinstance(Num,int):
        return Sumatoria_aux(Num)
    else:
        return "No es un numero entero"

def Sumatoria_aux(Num):
    if Num == 0:
        return 0
    else: Num+Sumatoria_aux(Num-1)
