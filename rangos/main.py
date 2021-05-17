import os

estados = {
    0: 'en rango',
    1: 'debajo del rango',
    2: 'por encima del rango'
}

def calcular(rango_menor, rango_mayor, n):
    if n >= rango_menor and n <= rango_mayor:
        return 0
    elif n < rango_menor:
        return 1
    elif n > rango_mayor:
        return 2

def ingresar_rangos():
    menor = input('Ingresa el rango menor: ')
    mayor = input('Ingresa el rango mayor: ')
    return menor, mayor

def main():
    os.system('clear')
    menor, mayor = ingresar_rangos()
    try:
        menor = float(menor)
        mayor = float(mayor)
        incorrecto = True
        while incorrecto:
            print()
            n = input('Ingresa un numero: ')
            try:
                n = float(n)
                resultado = calcular(menor, mayor, n)
                print(f'El numero {n} esta {estados[resultado]} de {menor} - {mayor}')
                if resultado == 0:
                    incorrecto = False
                else:
                    print('Intenta con otro numero')
            except:
                incorrecto = True
                print('Ingresa un numero valido')
                input('Presiona una tecla para continuar')
    except:
        print('Ingresa Rangos correctos')

if __name__ == '__main__':
    main()