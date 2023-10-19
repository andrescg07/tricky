""" importar modulo necesaio para la toma de decisiones aleatoria"""
import random

# validar la dificultad del juego deseada


def validar_nivel_ia() -> str:
    """ Pedir al usuario que escoja la dificultad del juego vs La maquina, validarlo y retornarlo"""
    while True:
        nivel = input(
            "Ingrese el nivel de dificultad de la IA, 'facil'/ 'dificil': ")
        if nivel.lower() == 'dificil' or nivel.lower() == 'facil':
            return nivel
        else:
            print('¡Opcion no valida, ese nivel no existe!')

# Funcion para pasar al frente e intentar ganar el juego sólo si la dificultad es 'dificil'


def propuesta_ataque(tabla: list, posiciones: list):
    """Iniciar y marcar una posible jugada de ataque para ganar el juego"""
    while True:
        decision = random.choice(posiciones)
        if tabla[decision] == ' ':
            return decision


def posible_tricky(tabla, valor_jugador, combinaciones_ganadoras):
    """Validar si hay algun jugador proximo a hacer un tricky o ganar el juego"""
    for combinacion in combinaciones_ganadoras:
        acumulado = 0
        marcar_casilla = 0
        for num in combinacion:
            num = int(num)
            if tabla[num] == valor_jugador:
                acumulado += 1
            else:
                marcar_casilla = int(num)
        if acumulado == 2 and tabla[marcar_casilla] == ' ':
            return True, marcar_casilla

    return False, ' '


def escoger_movimiento(tabla: list, combinaciones: list, disponibles: list, nivel: str, jugador: str, ia: str):
    """Analizar el estado del juego y posiciones para tomar una decision basado en el nivel de dificultad"""
    while True:
        p_disponibles = [i-1 for i in disponibles]
        proximo_movimiento = 0
        posiciones_ventaja = [0, 2, 4, 6, 8]

        if nivel == 'facil':
            defender, marcar_posicion = posible_tricky(
                tabla, jugador, combinaciones)

            if len(p_disponibles) >= 7:
                proximo_movimiento = random.choice([1, 3, 5, 7])
            elif defender:
                proximo_movimiento = marcar_posicion
            else:
                proximo_movimiento = random.choice(p_disponibles)

        elif nivel == 'dificil':
            ataque, marcar = posible_tricky(tabla, ia, combinaciones)
            if ataque:
                proximo_movimiento = marcar

            else:
                defensa, marcar_defensa = posible_tricky(
                    tabla, jugador, combinaciones)
                if defensa:
                    proximo_movimiento = marcar_defensa

                else:
                    proponer = propuesta_ataque(tabla, posiciones_ventaja)
                    proximo_movimiento = proponer
        break
    return proximo_movimiento
