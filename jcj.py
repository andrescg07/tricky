# importamos los modulos que necesitamos:
import funciones

# Funcion principal para el modo de juego Jugador contra Jugador:


def juego_JCJ():
    """ jugar el modo Jugador contra jugador"""
    # Variables necesarias para procesar
    combinaciones_tricky = ['048', '246', '036',
                            '012', '147', '345', '258', '678']
    contador_t1 = 0
    contador_t2 = 0

    j1 = input('Nombre del primer jugador: ')
    j2 = input('Nombre del seguo u otro jugador: ')
    ronda = 0
    victorias = {j1: 0, j2: 0}

    while True:
        posiciones_disponibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        tablero = [' ' for _ in range(9)]
        ronda += 1
        turnos = funciones.definir_turnos(j1, j2, ronda)
        primer_turno, primer_valor, segundo_turno, segundo_valor = turnos[
            0],  turnos[1], turnos[2], turnos[3]

        print('\n')
        print('\033[   1m JUEGO 1 vs 1  \033[0m')
        print(
            f'En esta ronda {primer_turno} juega con {primer_valor} y {segundo_turno} juega con {segundo_valor}')
        funciones.mostrar_tablero(
            tablero, victorias, j1, j2, posiciones_disponibles)

        while posiciones_disponibles:

            t1 = funciones.validar_posicion(
                posiciones_disponibles, primer_turno)
            tablero = funciones.actualizar_tablero(
                tablero, t1, primer_valor)
            posiciones_disponibles.remove(t1)
            print(
                f'Posiciones disponibles tablero: {[i+1 for i in posiciones_disponibles]}')
            funciones.mostrar_tablero(
                tablero, victorias, j1, j2, posiciones_disponibles)

            if funciones.validar_ganador(combinaciones_tricky, tablero, primer_valor):
                contador_t1 += 1
                victorias[primer_turno] = contador_t1
                print(f'{primer_turno} ganó el juego, hizo tricky con la "{primer_valor}"')  # noqa
                break

            if not posiciones_disponibles:
                print(
                    f'{primer_turno} y {segundo_turno} han empatado, el juego estuvo parejo')
                break

            t2 = funciones.validar_posicion(
                posiciones_disponibles, segundo_turno)
            tablero = funciones.actualizar_tablero(
                tablero, t2, segundo_valor)
            posiciones_disponibles.remove(t2)
            funciones.mostrar_tablero(
                tablero, victorias, j1, j2, posiciones_disponibles)

            if funciones.validar_ganador(combinaciones_tricky, tablero, segundo_valor):
                contador_t2 += 1
                victorias[segundo_turno] = contador_t2
                print(
                    f'{segundo_turno} ganó el juego, hizo tricky con la "{segundo_valor}"')
                break

        seguir_jugando = input('¿Seguir jugando 1 vs 1 Si/No?: ')
        if seguir_jugando.lower() == 'no':
            break

    return 'Menú'
