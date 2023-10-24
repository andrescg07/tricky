import pygame
import sys
import ia_movimientos
import funciones
# ---------------------------------------------------------


def empezar_juegoIa(dificultad: str, nombre: str, pantalla):

    # Constantes par ausar en el tablero
    pantalla.destroy()
    ANCHO = 600
    ALTO = 700
    ANCHO_LINEAS = 15

    COLOR_FONDO = (180, 180, 180)
    COLOR_BOLA = (239, 231, 200)
    COLOR_EQUIS = (52, 73, 94)

    # Pygame pantalla del juego
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption('VS IA - FACIL')
    ventana.fill(COLOR_FONDO)
    funciones.dibujar_lineas(ventana)
    tablero = [[0 for _ in range(3)] for _ in range(3)]
    victorias = [0, 0]
    ronda = 0
    player = 1
    funciones.marcador(ventana, nombre, victorias, ronda)
    fin = False
    p_disponibles = [9]
    resultado = ""
    try:
        while True:
            p_disponibles = []
            for fila in range(3):
                for col in range(3):
                    if tablero[fila][col] == 0:
                        p_disponibles.append([fila, col])
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    sys.exit()

                if (evento.type == pygame.MOUSEBUTTONDOWN and p_disponibles) and not fin:

                    clickX = evento.pos[0]
                    clickY = evento.pos[1]

                    fila_pulsada = int(clickY - 80) // 200
                    columna_pulsada = int(clickX // 200)

                    X = int(columna_pulsada * 200 + 100)
                    Y = int(fila_pulsada * 200 + 180)

                    # turnos = funciones.definir_turnos(j1, j2, ronda)
                    # primer_turno, primer_valor, segundo_turno, segundo_valor = turnos[0],  turnos[1], turnos[2], turnos[3]

                    if player == 1:
                        posicion = funciones.obtener_posicion(tablero,
                                                              fila_pulsada, columna_pulsada, player)
                        if posicion:
                            pygame.draw.circle(
                                ventana, COLOR_BOLA, (X, Y), 60, 15)
                            player = 2

                    ganarJ1 = funciones.validar_ganador(ventana, tablero, 1)
                    ganarJ2 = funciones.validar_ganador(ventana, tablero, 2)
                    if ganarJ1:
                        victorias[0] += 1
                        resultado = 'j1'
                        funciones.juego_terminado(ventana, nombre, resultado)
                        fin = True

                if (player == 2 and p_disponibles) and not fin:
                    ia = ia_movimientos.escoger_movimiento(
                        tablero, dificultad, 1)
                    if ia is not None:
                        fila_sel = ia[0]
                        col_sel = ia[1]
                        posicion = funciones.obtener_posicion(tablero,
                                                              fila_sel, col_sel, player)
                        if posicion:
                            X = int(col_sel * 200 + 100)
                            Y = int(fila_sel * 200 + 180)
                            pygame.draw.line(
                                ventana, COLOR_EQUIS, (X - 60, Y - 60), (X + 60, Y + 60), 25)
                            pygame.draw.line(
                                ventana, COLOR_EQUIS, (X - 60, Y + 60), (X + 60, Y - 60), 25)
                            player = 1

                        ganarJ2 = funciones.validar_ganador(
                            ventana, tablero, 2)
                        if ganarJ2:
                            victorias[1] += 1
                            resultado = 'ia'
                            funciones.juego_terminado(
                                ventana, nombre, resultado)
                            fin = True

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE:
                        tablero = [[0 for _ in range(3)] for _ in range(3)]
                        ronda += 1
                        ventana.fill(COLOR_FONDO)
                        funciones.dibujar_lineas(ventana)
                        funciones.marcador(ventana, nombre, victorias, ronda)
                        player = 1
                        fin = False

                if len(p_disponibles) == 0 and resultado == "":
                    resultado = 'Empate'
                    funciones.juego_terminado(ventana, nombre, resultado)

            pygame.display.update()
    except Exception as e:
        print('Errror en el funcionamiento de ia.py')
        print(e)
