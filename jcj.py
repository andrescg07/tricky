# importamos los modulos que necesitamos:
import funciones

# Funcion principal para el modo de juego Jugador contra Jugador:


def juego_JCJ():
    """ jugar el modo Jugador contra jugador"""
    # Variables necesarias para procesar
    combinaciones_tricky = ['048', '246', '036',
                            '012', '147', '345', '258', '678']

    terminar_juego = False

    j1 = input('Nombre del primer jugador: ')
    j2 = input('Nombre del seguo u otro jugador: ')
    ronda = 0
    victorias = {j1: 0, j2: 0}

    while not terminar_juego:
        posiciones_disponibles = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        tablero = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ronda_terminada = False
        ronda += 1
        turnos = funciones.definir_turnos(j1, j2, ronda)
        primer_turno = turnos[0]
        primer_valor = turnos[1]
        segundo_turno = turnos[2]
        segundo_valor = turnos[3]

        print('\n')
        print('\033[1m JUEGO 1 vs 1 \033[0m')

        while not ronda_terminada:
            print('\033[1mVICTORIAS:\033[0m ')
            print(f'{j1.lower()} {(primer_valor)} = {victorias[j1]} ------- {j2.lower()} {(segundo_valor)} = {victorias[j2]} \n')  # noqa
            print(
                f'Posiciones disponibles tablero: {[i+1 for i in posiciones_disponibles]}')
            funciones.mostrar_tablero(tablero)

            while True:
                try:
                    t1 = int(
                        input(f'{primer_turno} ingresa una posicion para marcar: '))
                    t1 -= 1
                    if t1 in posiciones_disponibles:
                        tablero = funciones.actualizar_tablero(
                            tablero, t1, primer_valor)
                        posiciones_disponibles.remove(t1)
                        print(
                            f'Posiciones disponibles tablero: {[i+1 for i in posiciones_disponibles]}')
                        funciones.mostrar_tablero(tablero)
                        break
                    else:
                        print(
                            'Posicion ocupada o valor no valido, intente nuevamente')
                except ValueError:
                    print('Error, ingrese un valor valido')

            if len(posiciones_disponibles) > 0:
                while True:
                    try:
                        t2 = int(
                            input(f'{segundo_turno} ingresa una posicion para marcar: '))
                        t2 -= 1
                        if t2 in posiciones_disponibles:
                            tablero = funciones.actualizar_tablero(
                                tablero, t2, segundo_valor)
                            posiciones_disponibles.remove(t2)
                            print(
                                f'Posiciones disponibles tablero: {[i+1 for i in posiciones_disponibles]}')
                            funciones.mostrar_tablero(tablero)
                            break
                        else:
                            print(
                                'Posicion ocupada o valor no valido, intente nuevamente')
                    except ValueError:
                        print('Error, ingrese un valor valido')

            while len(posiciones_disponibles) <= 6:
                gano_primer_jugador = funciones.ganador(
                    combinaciones_tricky, tablero, primer_valor)
                if gano_primer_jugador:
                    print('JUEGO TERMINADO')
                    print(
                        f'{primer_turno} ha hecho tricky y ha ganado el juego \n ')
                    if primer_turno == j1:
                        victorias[j1] = victorias[j1] + 1
                    elif primer_turno == j2:
                        victorias[j2] = victorias[j2] + 1
                    ronda_terminada = True
                gano_segundo_jugador = funciones.ganador(
                    combinaciones_tricky, tablero, primer_valor)
                if gano_segundo_jugador:
                    print('JUEGO TERMINADO')
                    print(
                        f'{segundo_turno} ha hecho tricky y ha ganado el juego \n ')
                    if primer_turno == j1:
                        victorias[j1] = victorias[j1] + 1
                    elif primer_turno == j2:
                        victorias[j2] = victorias[j2] + 1
                    ronda_terminada = True

                break

            if len(posiciones_disponibles) == 0:
                print(
                    f'{primer_turno} y {segundo_turno} han empatado, el juego estuvo parejo')
                ronda_terminada = True

        print('OPCIONES')
        print('1.Continuar jugando// 2.Salir del juego// 3.Volver a Menú principal ')
        seguir_jugando = input('Ingrese el numero de la opcion (1,2,3): ')

        if seguir_jugando == '2':
            exit()
        elif seguir_jugando == '3':
            terminar_juego = True

    return 'Menú'
