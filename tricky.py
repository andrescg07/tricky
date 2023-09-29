# ------------------------------- TRICKY ----------------------------------
import random

combinaciones_tricky = ['159', '357', '147', '123', '258', '456', '369', '789']
primer_lista = ['1', '2', '3']
segunda_lista = ['4', '5', '6']
tercer_lista = ['7', '8', '9']


def actualizar_tablero(tabla, posicion, valor):

    c = 0
    indice = 0

    for fila in tabla:
        if c == 0 and posicion in primer_lista:
            indice = primer_lista.index(posicion)
            tabla[c][indice] = valor
        elif c == 1 and posicion in segunda_lista:
            indice = segunda_lista.index(posicion)
            tabla[c][indice] = valor
        elif c == 2 and posicion in tercer_lista:
            indice = tercer_lista.index(posicion)
            tabla[c][indice] = valor
        c += 1
    return tabla


def ganador(combinaciones, tablero, jugador):

    acumulado = 0
    indice = 0

    for combinacion in combinaciones:
        for num in combinacion:
            if num in primer_lista:
                indice = primer_lista.index(num)
                if tablero[0][indice] == jugador:
                    acumulado += 1
            elif num in segunda_lista:
                indice = segunda_lista.index(num)
                if tablero[1][indice] == jugador:
                    acumulado += 1
            elif num in tercer_lista:
                indice = tercer_lista.index(num)
                if tablero[2][indice] == jugador:
                    acumulado += 1
        if acumulado == 3:
            return True
        acumulado = 0

    if acumulado != 3:
        return False


def mostrar_tablero(tablero):
    c = 0
    for fila in tablero:
        print(' | '.join(fila))
        print('----------' if c != 2 else '')
        c += 1
    print('\n')


def tricky():

    jugador_O = 'O'
    jugador_X = 'X'
    posiciones_disponibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    tablero = [[' ', ' ', ' '],
               [' ', ' ', ' '],
               [' ', ' ', ' ']]
    progreso = []

    print(
        '\n   \033[1m  ---------- BIENVENIDO - JUGUEMOS TRICKY O TIC-TAC-TOE ------ \033[0m ')
    print(
        ' \033[1m Estos son los numeros de cada posicion en el tablero, recuerdalos bien \033[0m \n')
    tablero_numeros = [['1', '2', '3'],
                       ['4', '5', '6'],
                       ['7', '8', '9']]
    i = 0
    for fila in tablero_numeros:
        print(' | '.join(fila))
        i += 3
        print('----------'if i != 9 else '')

    while len(posiciones_disponibles) >= 1:

        while True:
            try:
                primer_turno = input(
                    f'Turno de {jugador_X}, Ingresa un numero entre {posiciones_disponibles} para la posicion donde quieres poner la X: ')
                print('\n')

                if int(primer_turno) in posiciones_disponibles:
                    break
                else:
                    print('¡Ingresa posiciones que no esten ocupadas!')
            except ValueError:
                print('¡Valores no validos!')

        progreso = actualizar_tablero(tablero, primer_turno, jugador_X)
        posiciones_disponibles.remove(int(primer_turno))

        if len(posiciones_disponibles) > 0:
            segundo_turno = random.choice(posiciones_disponibles)
            progreso = actualizar_tablero(
                progreso, str(segundo_turno), jugador_O)
            posiciones_disponibles.remove(segundo_turno)
            print(
                f'has puesto {jugador_X} en la posicion {primer_turno} y la maquina puso {jugador_O} en la posicion {segundo_turno}: \n')

        mostrar_tablero(progreso)

        while len(posiciones_disponibles) <= 6:
            gano_x = ganador(combinaciones_tricky, progreso, jugador_X)
            if gano_x is True:
                return f'El jugador {jugador_X} ha hecho tricky y ha ganado el juego'
            gano_o = ganador(combinaciones_tricky, progreso, jugador_O)
            if gano_o is True:
                return f'El jugador {jugador_O} ha hecho tricky y ha ganado el juego'
            break

    return 'Opps, has empatado con la maquina, ha estado parejo '


if __name__ == '__main__':
    jugar = tricky()
    print(jugar)
