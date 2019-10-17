def Suma(Num1,Num2):
    return Num1 + Num2

def Resta(Num1,Num2):
    return Num1-Num2

def Sumatoria(Num,i):
    if i > Num:
        return 0
    else:
        return i+3 + Sumatoria(Num,i+1)
