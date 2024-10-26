def suma(x,y):
    return x+y


def resta(x,y):
    return x-y

def multiplicacion(x,y):
    return x*y

def division(x,y):
    if y==0:
        raise ValueError("\n[!] No es posible dividir un número entre cero")
    else:
        return x/y

