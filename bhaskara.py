import math

def calcular_bhaskara(a, b, c):
    delta = b**2 - 4*a*c
    
    match delta:
        case d if d < 0:
            return None
        case 0:
            x = -b / (2*a)
            return (x,)
        case d if d > 0:
            x1 = (-b + math.sqrt(d)) / (2*a)
            x2 = (-b - math.sqrt(d)) / (2*a)
            return (x1, x2)

def main():
    print("Cálculo das raízes da equação do segundo grau (ax² + bx + c = 0)")
    
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    
    resultado = calcular_bhaskara(a, b, c)
    
    match resultado:
        case None:
            print("A equação não possui raízes reais.")
        case (x,):
            print(f"A equação possui uma raiz: x = {x}")
        case (x1, x2):
            print(f"As raízes da equação são: x1 = {x1} e x2 = {x2}")

if __name__ == "__main__":
    main()