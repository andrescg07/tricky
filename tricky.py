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


def main(mdj: str, dificultad='ninguna'):
    modo_juego = mdj
    jugador_O = 'O'
    jugador_X = 'X'
    posiciones_disponibles = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    tablero = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    primer_turno = 0
    segundo_turno = 0

    print('\033[1m JUEGO 1 vs 1 \033[0m \n' if mdj ==
          'JCJ' else ' \033[1m JUEGO CONTRA LA IA \033[0m \n')
    mostrar_tablero(tablero)
    while len(posiciones_disponibles) >= 1:
        mostrar_posiciones = f'Posiciones disponibles en el tablero: {[i+1 for i in posiciones_disponibles]}'

        while True:
            try:
                print(mostrar_posiciones)
                primer_turno = int(input(
                    f' Jugador {jugador_X} ingrese la  posicion para marcar: '))
                print('\n')
                primer_turno = primer_turno - 1

                if primer_turno in posiciones_disponibles:
                    tablero = actualizar_tablero(
                        tablero, primer_turno, jugador_X)
                    posiciones_disponibles.remove(primer_turno)
                    mostrar_tablero(tablero)
                    break
                else:
                    print('¡Ingresa posiciones que no esten ocupadas!')
            except ValueError:
                print('¡Valores no validos!')

        if len(posiciones_disponibles) > 0:
            if modo_juego == 'JCJ':
                while True:
                    print(mostrar_posiciones)
                    segundo_turno = int(
                        input(f'jugador {jugador_O} ingrese una posicion para marcar: '))
                    if segundo_turno in posiciones_disponibles:
                        tablero = actualizar_tablero(
                            tablero, segundo_turno, jugador_O)
                        posiciones_disponibles.remove(segundo_turno)
                        break
                    else:
                        print('Ingrese una posicion valida o que no esté ocupada')
            else:
                segundo_turno = ia_movimientos.escoger_movimiento(
                    tablero, combinaciones_tricky, posiciones_disponibles)
                print(f'ia movimiento: {segundo_turno}')
                tablero = actualizar_tablero(tablero, segundo_turno, jugador_O)
                posiciones_disponibles.remove(segundo_turno)

            mostrar_tablero(tablero)
            print(
                f'Jugador {jugador_X} marcó  la posicion {primer_turno + 1} y el jugador {jugador_O} marcó la posicion {segundo_turno + 1}: \n')

        while len(posiciones_disponibles) <= 6:
            gano_x = ganador(combinaciones_tricky, tablero, jugador_X)
            if gano_x is True:
                print('JUEGO TERMINADO')
                return f'El jugador {jugador_X} ha hecho tricky y ha ganado el juego \n '
            gano_o = ganador(combinaciones_tricky, tablero, jugador_O)
            if gano_o is True:
                print('JUEGO TERMINADO')
                return f'El jugador {jugador_O} ha hecho tricky y ha ganado el juego \n '
            break

    print('JUEGO TERMINADO')
    return 'Opps, has empatado con la maquina, ha estado parejo \n'
