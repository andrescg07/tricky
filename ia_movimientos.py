""" importar modulo necesaio para la toma de decisiones aleatoria"""
import random

# validar la dificultad del juego deseada
combinaciones_tricky = [
    [(0, 0), (0, 1), (0, 2)],  # Filas
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],  # Columnas
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],  # Diagonales
    [(0, 2), (1, 1), (2, 0)]
]


# Funcion para pasar al frente e intentar ganar el juego sólo si la dificultad es 'dificil'
def propuesta_ataque(tabla: list, posiciones: list):
    """Iniciar y marcar una posible jugada de ataque para ganar el juego"""
    while True:
        decision = random.choice(posiciones)
        c1 = decision[0]
        c2 = decision[1]
        if tabla[c1][c2] == 0:
            return decision


def posible_tricky(tablero: list, jugador: int, disponibles: list):
    """Validar si hay algun jugador proximo a hacer un tricky o ganar el juego"""

    for combo in combinaciones_tricky:
        acumulado = 0
        marcar = [0, 0]
        for coordenada in combo:
            f = coordenada[0]
            c = coordenada[1]
            if tablero[f][c] == jugador:
                acumulado += 1
            elif tablero[f][c] == 0:
                marcar = [f, c]
        if acumulado == 2:
            if marcar in disponibles:
                return marcar

    return False  # No se encontró ningún "tricky" para el próximo turno


def escoger_movimiento(tabla: list, nivel: str, jugador: int):
    """Analizar el estado del juego y posiciones para tomar una decision basado en el nivel de dificultad"""

    try:
        p_disponibles = []
        for fila in range(3):
            for col in range(3):
                if tabla[fila][col] == 0:
                    p_disponibles.append([fila, col])

        while p_disponibles:
            proximo_movimiento = 0
            posiciones_ventaja = [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]
            posiciones_opcionales = [[0, 1], [1, 0], [1, 2], [2, 1]]

            if nivel == 'facil':
                defender = posible_tricky(
                    tabla, jugador, p_disponibles)

                if len(p_disponibles) >= 7:
                    proximo_movimiento = random.choice(posiciones_opcionales)

                elif defender:
                    proximo_movimiento = defender

                else:
                    proximo_movimiento = random.choice(p_disponibles)

            elif nivel == 'dificil':
                ataque = posible_tricky(tabla, 2, p_disponibles)
                if ataque:
                    proximo_movimiento = ataque

                else:
                    defender = posible_tricky(
                        tabla, jugador, p_disponibles)
                    if defender:
                        proximo_movimiento = defender

                    else:
                        proponer = propuesta_ataque(tabla, posiciones_ventaja)
                        proximo_movimiento = proponer

            if proximo_movimiento in p_disponibles:
                return proximo_movimiento
    except Exception as e:
        print('Error la ia no pudo escoger un movimiento')
        print(e)
