import math

def calcular_area_retangulo(base, altura):
    return base * altura

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_area_circulo(raio):
    return math.pi * (raio ** 2)

def main():
    while True:
        print("\nCalculadora de Áreas de Formas Geométricas")
        print("1. Retângulo")
        print("2. Triângulo")
        print("3. Círculo")
        print("4. Sair")

        escolha = input("Escolha uma forma (1/2/3/4): ")

        match escolha:
            case '1':
                base = float(input("Digite a base do retângulo: "))
                altura = float(input("Digite a altura do retângulo: "))
                area = calcular_area_retangulo(base, altura)
                print(f"A área do retângulo é: {area}")

            case '2':
                base = float(input("Digite a base do triângulo: "))
                altura = float(input("Digite a altura do triângulo: "))
                area = calcular_area_triangulo(base, altura)
                print(f"A área do triângulo é: {area}")

            case '3':
                raio = float(input("Digite o raio do círculo: "))
                area = calcular_area_circulo(raio)
                print(f"A área do círculo é: {area:.2f}")

            case '4':
                print("Saindo da calculadora...")
                break

            case _:
                print("Escolha inválida!")

if __name__ == "__main__":
    main()