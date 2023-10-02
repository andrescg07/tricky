import random

def atacar(tabla, posiciones):
    while True:
        decision = random.choice(posiciones)
        if tabla[decision] == ' ':
            return decision
     

def posible_tricky(tabla, casillas, combinaciones, ventaja):

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
        
    if acumulado == 1 and tabla[marcar_casilla] == ' ':
        return marcar_casilla
    else:
        proponer =  atacar(tabla, ventaja)
        return proponer

    return False


def escoger_movimiento(tabla: list, combinaciones: list, disponibles:list):
    while True:
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
            proximo_movimiento = atacar(tabla, posiciones_ventaja)

        if len(posiciones_x) >= 2:
            peligro_alto = posible_tricky(
                tabla, posiciones_x, combinaciones_tricky, posiciones_ventaja)
            if peligro_alto:
                proximo_movimiento = peligro_alto
            else:
                pasar_al_ataque = posible_tricky(tabla, posiciones_o, combinaciones_tricky, posiciones_ventaja)
                if pasar_al_ataque:
                    proximo_movimiento = atacar

        if proximo_movimiento in disponibles:
            break

    return proximo_movimiento
