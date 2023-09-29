import random

# tablero = [[' ', ' ', ' '],
#            [' ', ' ', ' '],
#            [' ', ' ', ' ']]
tablero = ['', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ']


def escoger_movimiento(tabla) -> str:
    posiciones_ventaja = [0, 2, 4, 6, 8]
    veces_x = tabla.count('X')
    posiciones_x = []
    for i in range(len(tabla)):
        if tabla[i] == 'X':
            posiciones_x.append(i)

    print(
        f'La X está {veces_x} veces en las posiciones {[i+1 for i in posiciones_x]}')
    proximo_movimiento = 0
    # numeros_posiciones = [i for fila in tabla for i in fila]
    if 'X' not in tabla:
        posicion_inicial = random.choice(posiciones_ventaja)
        proximo_movimiento = posicion_inicial
    return proximo_movimiento


def mostrar_tablero(tabla):

    for i in range(0, 9, 3):
        fila = tabla[i:i + 3]
        print(' | '.join(fila))
        print('----------' if i < 6 else '')


movimiento = escoger_movimiento(tablero)

tablero[movimiento if movimiento != 0 else 0] = 'O'
print(f'\n La maquina ha puesto O  en la pocicion {movimiento + 1 } \n')
mostrar_tablero(tablero)
