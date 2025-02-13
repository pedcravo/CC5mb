from math import pi

def Soma(a, b):
    print(a + b)
    return a + b

def Operacoes(a, b):
    return a - b, a * b

def CalcularEsfera(a, b):
    return(4/3)*(a**3)*b

def CalcularEsfera2(a):
    return(4/3)*(a**3)*pi

if __name__ == "__main__":
    print("Olá Mundo")
    x = Soma(3, 8)
    print("x = ", x)
    x = Operacoes(3, 6)
    print("x = ", x)
    v_pi = 3.1415
    print(CalcularEsfera(2, v_pi))
    print(CalcularEsfera2(10))
    v = lambda a: (4/3)*(a**3)*v_pi
    print(v(13.7))
