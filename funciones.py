# ------------------------------- TRICKY ----------------------------------
# import ia_movimientos

def definir_turnos(primero, segundo, ronda) -> list:
    turno1, turno2, valor1, valor2 = "", "", "", ""
    if ronda % 2 == 0:
        turno1 = segundo
        turno2 = primero
        valor1 = 'O'
        valor2 = 'X'
    else:
        turno1 = primero
        turno2 = segundo
        valor1 = 'X'
        valor2 = 'O'
    turnos_asignados = [turno1, valor1, turno2, valor2]
    return turnos_asignados


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
