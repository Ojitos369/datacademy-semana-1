import os
PI = 3.1416
def ingresar_datos():
    radio = input('Ingresa el radio del circulo base: ')
    altura = input('Ingresa la altura del cilindro: ')
    return radio, altura

def calcular_volumen(radio, altura):
    base = PI * (radio ** 2)
    return base * altura

def main():
    os.system('clear')
    radio, altura = ingresar_datos()
    try:
        radio = float(radio)
        altura = float(altura)
        os.system('clear')
        volumen = calcular_volumen(radio, altura)
        print(f'El volumen del cilindo con {radio} de radio y {altura} de altura es:')
        print(volumen)
    except:
        print('Ingresa datos validos')

if __name__ == '__main__':
    main()