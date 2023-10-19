import pygame
import sys
import tkinter as tk
import funciones
import ia_movimientos
# ---------------------------------------------------------


def empezar_juegoIa(dificultad: str, nombre: str, pantalla):  #
    pantalla.destroy()
    ANCHO = 1200
    ALTO = 680
    COLOR_FONDO = (28, 170, 156)
    ROJO = (200, 0, 0)
    COLOR_LINEAS = (23, 145, 135)
    ANCHO_LINEAS = 15
    NEGRO = (0, 0, 0)
    COLOR_BOLA = (239, 231, 200)
    COLOR_EQUIS = (52, 73, 94)
    pygame.init()
    fuente = pygame.font.Font(None, 36)
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption('VS IA - FACIL')
    ventana.fill(COLOR_FONDO)

    tablero = [' ' for _ in range(9)]
    combinaciones_tricky = [['036', '147', '258'],
                            ['012', '345', '678'], ['642'], ['048']]
    contador_t1 = 0
    contador_t2 = 0

    j1 = nombre
    j2 = 'ia'
    ronda = 0
    victorias = {j1: 0, j2: 0}

    def obtener_posicion(fila: int, columna: int) -> int:
        """convierte una fila y columna a la posicion en un tablero plano [0,1,2,3,4,5,6,7,8]

        Args: 
            fila (int): Numero de la fila 0-2 marcada
            columna (int): Numero de la columna 0-2 marcada
        Returns:
            posicion (int) : Numero Posicion 0-8 en un tablero plano
            -1 (int): en caso de que la posicion marcada no sea valida
        """

        if 0 <= fila <= 2 and 0 <= columna <= 2:
            posicion = fila * 3 + columna
            return posicion
        else:
            # Devolver un valor fuera de rango si la fila o la columna no son válidas
            return -1

    def validar_ganador(combinaciones: list, tablero: list, jugador: int):
        """ Recibir el tablero y validar si un jugador ha hecho tricky"""
        for llave in combinaciones:
            for combinacion in llave:
                if all(tablero[int(num)] == jugador for num in combinacion):
                    lineas_ganadoras()
            return True

        return False

    def dibujar_lineas():
        # Horizontales
        pygame.draw.line(ventana, COLOR_LINEAS, (100, 240),
                         (700, 240), ANCHO_LINEAS)
        pygame.draw.line(ventana, COLOR_LINEAS, (100, 440),
                         (700, 440), ANCHO_LINEAS)

        # Verticales
        pygame.draw.line(ventana, COLOR_LINEAS, (300, 40),
                         (300, 640), ANCHO_LINEAS)
        pygame.draw.line(ventana, COLOR_LINEAS, (500, 40),
                         (500, 640), ANCHO_LINEAS)
    dibujar_lineas()

    texto = fuente.render(
        f'Marcador: {nombre} "X" - SAMUEL "O"', True, NEGRO)
    ventana.blit(texto, (750, 60))

    posiciones_disponibles = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    player = 1
    ganador_ronda = 0
    fin = False
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN and not fin:
                clickX = evento.pos[0]
                clickY = evento.pos[1]

                fila_pulsada = int(clickY - 40) // 200
                columna_pulsada = int(clickX - 100) // 200
                print(fila_pulsada, columna_pulsada)

                X = int(columna_pulsada * 200 + 200)
                Y = int(fila_pulsada * 200 + 140)

                ronda += 1
                # turnos = funciones.definir_turnos(j1, j2, ronda)
                # primer_turno, primer_valor, segundo_turno, segundo_valor = turnos[0],  turnos[1], turnos[2], turnos[3]
                posicion = obtener_posicion(
                    fila_pulsada, columna_pulsada)
                if player == 1 and posicion in posiciones_disponibles:
                    tablero[posicion] = player
                    posiciones_disponibles.remove(posicion)
                    pygame.draw.circle(ventana, COLOR_BOLA, (X, Y), 60, 15)
                    player = 2
                elif player == 2 and posicion in posiciones_disponibles:
                    tablero[posicion] = player
                    posiciones_disponibles.remove(posicion)
                    pygame.draw.line(
                        ventana, COLOR_EQUIS, (X - 60, Y - 60), (X + 60, Y + 60), 25)
                    pygame.draw.line(
                        ventana, COLOR_EQUIS, (X - 60, Y + 60), (X + 60, Y - 60), 25)
                    player = 1

                while len(posiciones_disponibles) <= 6:

                    ganarJ1 = validar_ganador(combinaciones_tricky, tablero, 1)
                    ganarJ2 = validar_ganador(combinaciones_tricky, tablero, 2)
                    if ganarJ1:
                        ganador_ronda = j1
                        mensaje = f"El jugador {ganador_ronda} hizó tricky"
                        fin = True

                    elif ganarJ2:
                        ganador_ronda = j2
                        mensaje = f"El jugador {ganador_ronda} hizó tricky"
                        fin = True

                    break
                print(tablero)

            # if evento.type == pygame.KEYDOWN:
                #     if evento.key == pygame.K_KP_ENTER:
            #         ventana.fill(COLOR_FONDO)
            #         dibujar_lineas()
            #         player = 1
            #         tablero = [' ' for _ in range(9)]
            #         posiciones_disponibles = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        pygame.display.update()


# empezar_juegoIa()
