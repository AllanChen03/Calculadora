
def Suma(Num1,Num2):
    return Num1 + Num2

def Resta(Num1,Num2):
    return Num1-Num2

def Sumatoria(Num):
    if Num < 0:
        return 0
    else:
        return Num + Sumatoria(Num-1)

def  Multi(A,B):
    return A*B

def Divi(A,B):
    return A/B

def fact(N):
    if N==1 or N==0:
        return 1
    else:
        return N*fact(N-1)

