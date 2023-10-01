# ------------------------------- TRICKY ----------------------------------
import ia_movimientos

combinaciones_tricky = ['048', '246', '036', '012', '147', '345', '258', '678']


def actualizar_tablero(tabla, posicion, valor):

    tabla[posicion] = valor
    return tabla


def ganador(combinaciones, tablero, jugador):

    acumulado = 0

    for combinacion in combinaciones:
        for num in combinacion:
            entero = int(num)
            if tablero[entero] == jugador:
                acumulado += 1
        if acumulado == 3:
            return True
        acumulado = 0

    if acumulado != 3:
        return False


def mostrar_tablero(tablero):
    for casilla in range(0, len(tablero), 3):
        fila = tablero[casilla:casilla+3]
        print(' | '.join(fila))
        print('----------' if casilla < 6 else '')
    print('\n')


def tricky():

    jugador_O = 'O'
    jugador_X = 'X'
    posiciones_disponibles = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    tablero = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    progreso = []

    while len(posiciones_disponibles) >= 1:

        while True:
            try:
                primer_turno = int(input(
                    f'Turno de {jugador_X}, Ingresa un numero entre {[i+1 for i in posiciones_disponibles]} para la posicion donde quieres poner la X: '))
                print('\n')

                primer_turno = primer_turno - 1

                if primer_turno in posiciones_disponibles:
                    break
                else:
                    print('¡Ingresa posiciones que no esten ocupadas!')
            except ValueError:
                print('¡Valores no validos!')

        tablero = actualizar_tablero(tablero, primer_turno, jugador_X)
        posiciones_disponibles.remove(primer_turno)

        if len(posiciones_disponibles) > 0:
            segundo_turno = ia_movimientos.escoger_movimiento(
                tablero, combinaciones_tricky)
            print(f'La maquina escogió: {segundo_turno}')
            tablero = actualizar_tablero(
                tablero, segundo_turno, jugador_O)
            posiciones_disponibles.remove(segundo_turno)
            print(
                f'has puesto {jugador_X} en la posicion {primer_turno + 1} y la maquina puso {jugador_O} en la posicion {segundo_turno + 1}: \n')

        mostrar_tablero(tablero)

        while len(posiciones_disponibles) <= 6:
            gano_x = ganador(combinaciones_tricky, tablero, jugador_X)
            if gano_x is True:
                return f'El jugador {jugador_X} ha hecho tricky y ha ganado el juego'
            gano_o = ganador(combinaciones_tricky, tablero, jugador_O)
            if gano_o is True:
                return f'El jugador {jugador_O} ha hecho tricky y ha ganado el juego'
            break

    return 'Opps, has empatado con la maquina, ha estado parejo '


if __name__ == '__main__':
    jugar = tricky()
    print(jugar)
