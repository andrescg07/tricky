import random

# tablero = ['X', ' ', 'X', 'O', ' ', ' ', 'X', ' ', 'X']
# combinaciones_tricky = ['048', '246', '036', '012', '147', '345', '258', '678']


def posible_tricky(tabla, casillas, combinaciones):

    for combinacion in combinaciones:
        acumulado = 0
        marcar_casilla = 0
        for num in combinacion:
            if int(num) in casillas:
                acumulado += 1
            else:
                marcar_casilla = int(num)
        if acumulado == 2 and tabla[marcar_casilla] == ' ':
            return marcar_casilla

    return False


def escoger_movimiento(tabla: list, combinaciones: list):
    combinaciones_tricky = combinaciones
    proximo_movimiento = 0
    posiciones_ventaja = [0, 2, 4, 6, 8]
    posiciones_x = []
    posiciones_o = []

    for i in range(len(tabla)):
        if tabla[i] == 'X':
            posiciones_x.append(i)
        elif tabla[i] == 'O':
            posiciones_o.append(i)

    peligro = [
        i for i in posiciones_x for v in posiciones_ventaja if i == v]

    if len(peligro) < 2:
        while True:
            decision = random.choice(posiciones_ventaja)
            if tabla[decision] != 'X':
                proximo_movimiento = decision
                break
    if len(posiciones_x) >= 2:
        peligro_alto = posible_tricky(
            tabla, posiciones_x, combinaciones_tricky)
        if peligro_alto:
            proximo_movimiento = peligro_alto
        else:
            atacar = posible_tricky(tabla, posiciones_o, combinaciones_tricky)
            if atacar:
                proximo_movimiento = atacar

    return proximo_movimiento
