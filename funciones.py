"""Modulo que contiene las funciones necesarias para el juego"""
import pygame


pygame.init()
fuente = pygame.font.Font(None, 35)
fuente_resultado = pygame.font.Font(None, 60)
ANCHO = 600
ALTO = 700
ANCHO_LINEAS = 15

COLOR_FONDO = (180, 180, 180)
ROJO = (200, 0, 0)
COLOR_LINEAS = (23, 145, 135)
NEGRO = (0, 0, 0)
COLOR_BOLA = (239, 231, 200)
COLOR_EQUIS = (52, 73, 94)
COLOR_RESULTADO = (60, 60, 60)


def obtener_posicion(tablero: list, fila: int, columna: int, jugador: int) -> bool:
    """recibe una fila y columna, valida  la posicion en el tablero y la asigna al jugador que ha marcado

    Args: 
        fila (int): Numero de la fila 0-2 marcada
        columna (int): Numero de la columna 0-2 marcada
    Returns:
        True (bool): en caso de que la posicion sea valida y sea asignada al jugador
        False (bool): en caso de que la posicion marcada no sea valida
    """
    if 0 <= fila <= 2 and 0 <= columna <= 2:
        if tablero[fila][columna] == 0:
            tablero[fila][columna] = jugador
            return True
        # Devolver False si la fila o la columna no son válidas o están ocupadas
        return False


def dibujar_lineas(ventana):
    # Horizontales
    pygame.draw.line(ventana, COLOR_LINEAS, (10, 280),
                     (600, 280), ANCHO_LINEAS)
    pygame.draw.line(ventana, COLOR_LINEAS, (10, 480),
                     (600, 480), ANCHO_LINEAS)

    # Verticales
    pygame.draw.line(ventana, COLOR_LINEAS, (200, 80),
                     (200, 680), ANCHO_LINEAS)
    pygame.draw.line(ventana, COLOR_LINEAS, (400, 80),
                     (400, 680), ANCHO_LINEAS)


def lineas_ganadoras(ventana, sentido: str, colfil: int, jug: int):

    color_linea = (COLOR_BOLA if jug == 1 else COLOR_EQUIS)

    if sentido == 'vertical':
        posX = int(colfil * 200 + 100)
        pygame.draw.line(ventana, color_linea, (posX, 80),
                         (posX, 680), ANCHO_LINEAS)

    elif sentido == 'horizontal':
        posY = int(colfil*200 + 180)
        pygame.draw.line(ventana, color_linea, (10, posY),
                         (590, posY), ANCHO_LINEAS)

    elif sentido == 'ascendente':
        pygame.draw.line(ventana, color_linea, (10, 680),
                         (590, 80), ANCHO_LINEAS)

    elif sentido == 'descendente':
        pygame.draw.line(ventana, color_linea, (10, 80),
                         (590, 680), ANCHO_LINEAS)


def marcador(ventana, nombre1: str, victorias: list, ronda: int, nombre2="IA"):
    texto = fuente.render(
        f'MARCADOR:  {nombre1.upper()} ({victorias[0]}) || {nombre2.upper()} ({victorias[1]}) || RONDA: {ronda}', True, NEGRO, COLOR_BOLA)
    ventana.blit(texto, (16, 10))


def juego_terminado(ventana, result: str, nombre=""):

    if result == "Empate":
        empate = fuente_resultado.render(
            f'EMPATE', True, COLOR_BOLA, COLOR_RESULTADO)
        ventana.blit(empate, (180, 275))

    elif result == "j1":
        j1victoria = fuente_resultado.render(
            f'{nombre.upper()} HIZO TRICKY', True, COLOR_BOLA, COLOR_RESULTADO)
        ventana.blit(j1victoria, (50, 275))

    elif result == "j2":
        j2victoria = fuente_resultado.render(
            f'{nombre.upper()} HIZO TRICKY', True, COLOR_BOLA, COLOR_RESULTADO)
        ventana.blit(j2victoria, (50, 275))

    elif result == "ia":
        iavictoria = fuente_resultado.render(
            f'LA IA GANÓ EL JUEGO', True, COLOR_BOLA, COLOR_RESULTADO)
        ventana.blit(iavictoria, (50, 275))


def validar_ganador(ventana, tablero: list, playerI: int):
    """ Recibir el tablero y validar si un jugador ha hecho tricky"""
    aux = 0
    # vertical
    for col in range(3):
        if tablero[0][col] == playerI and (tablero[1][col] == playerI and tablero[2][col] == playerI):
            lineas_ganadoras(ventana, 'vertical', col, playerI)
            return True

    # horizontal win check
    for filaa in range(3):
        if tablero[filaa][0] == playerI and (tablero[filaa][1] == playerI and tablero[filaa][2] == playerI):
            lineas_ganadoras(ventana, 'horizontal', filaa, playerI)
            return True

    # asc diagonal win check
    if tablero[2][0] == playerI and tablero[1][1] == playerI and tablero[0][2] == playerI:
        lineas_ganadoras(ventana, 'ascendente', aux, playerI)
        return True

    # desc diagonal win chek
    if tablero[0][0] == playerI and tablero[1][1] == playerI and tablero[2][2] == playerI:
        lineas_ganadoras(ventana, 'descendente', aux, playerI)
        return True

    return False
