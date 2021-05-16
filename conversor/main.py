import os

def convertir_km_a_millas(km):
    return km * 1.609344

def convertir_millas_a_km(millas):
    return millas / 1.609344

def opciones():
    return input("""1.- Convertir de millas a kilometros
2.- Convertir de kilometros a millas
Elige una opcion: """)

def main():
    os.system('clear')
    opcion = opciones()
    if opcion == '1':
        os.system('clear')
        millas = input('Ingresa las millas: ')
        try:
            millas = float(millas)
            kilometros = convertir_millas_a_km(millas)
            print(f'millas: {millas}')
            print(f'kilometros: {kilometros}')
        except:
            print('Debes ingresar un numero')
    elif opcion == '2':
        os.system('clear')
        kilometros = input('Ingresa los kilometros: ')
        try:
            kilometros = float(kilometros)
            millas = convertir_km_a_millas(kilometros)
            print(f'kilometros: {kilometros}')
            print(f'millas: {millas}')
        except:
            print('Debes ingresar un numero')
    else:
        print('Por favor ingresa una opcion valida')

if __name__ == '__main__':
    main()