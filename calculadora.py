def Suma(Num1,Num2):
    return Num1 + Num2

def Resta(Num1,Num2):
    return Num1-Num2

def Sumatoria(Num):
    if Num < 0:
        return 0
    else:
        return Num + Sumatoria(Num-1)
