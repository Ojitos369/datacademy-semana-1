import random
import os

opciones = {
    0: 'Piedra',
    1: 'Papel',
    2: 'Tijera'
}

resultados = {
    'P1': 'Gana Maquina',
    'P2': 'Gana Jugador',
    'E': 'Empate'
}

def tiro():
    return random.randrange(0, 3)

def verificar(player_1, player_2):
    if player_1 == 0:
        if player_2 == 1:
            return 'P2'
        elif player_2 == 2:
            return 'P1'
        elif player_2 == 0:
            return 'E'
    if player_1 == 1:
        if player_2 == 1:
            return 'E'
        elif player_2 == 2:
            return 'P2'
        elif player_2 == 0:
            return 'P1'
    if player_1 == 2:
        if player_2 == 1:
            return 'P1'
        elif player_2 == 2:
            return 'E'
        elif player_2 == 0:
            return 'P2'

def recibir_jugada():
    return int(input("""1.- Piedra
2.- Papel
3.- Tijera
Elige tu jugada: """)) - 1

def juego(jugadas):
    player_win = 0
    machine_win = 0
    empate = 0

    for i in range(jugadas):
        os.system('clear')
        print(f'Jugada {i + 1} / {jugadas}')
        jugador = recibir_jugada()
        maquina = tiro()
        print(f'Jugador - {opciones[jugador]}')
        print(f'Maquina - {opciones[maquina]}')
        resultado = verificar(maquina, jugador)
        print(f'{resultados[resultado]}')
        if resultado == 'P1':
            machine_win += 1
        elif resultado == 'P2':
            player_win += 1
        elif resultado == 'E':
            empate += 1
        input('Presiona Enter para continuar')
    os.system('clear')
    print(f'Numero de Jugadas: {jugadas}')
    print(f'Ganadas de jugador: {player_win}')
    print(f'Ganadas de la maquina: {machine_win}')
    print(f'Empates: {empate}')
    if player_win > machine_win:
        print('Gano el jugador')
    elif machine_win > player_win:
        print('Gano la maquina')
    else:
        print('Empate')

def main():
    os.system('clear')
    jugadas = int(input('Ingresa el numero de jugadas: '))
    juego(jugadas)

if __name__ == '__main__':
    main()