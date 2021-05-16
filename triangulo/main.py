import os

def calcular_area(base, altura):
    return base * altura / 2

def comparacion(lado_a, lado_b, lado_c):
    if lado_a == lado_b and lado_b == lado_c:
        print('Triangulo Equilatero')
    elif lado_a != lado_b and lado_b != lado_c and lado_a != lado_c:
        print('Triangulo Escaleno')
    else:
        print('Triangulo Isoseles')

def main():
    os.system('clear')
    base = float(input('Ingresa la base: '))
    altura = float(input('Ingresa la altura: '))
    lado_a = float(input('Ingresa la lado A: '))
    lado_b = float(input('Ingresa la lado B: '))
    lado_c = float(input('Ingresa la lado C: '))
    os.system('clear')
    area = calcular_area(base, altura)
    print(f'El area es: {area}')
    comparacion(lado_a, lado_b, lado_c)

if __name__ == '__main__':
    main()
