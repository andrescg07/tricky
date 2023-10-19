"""Modulo que contiene las funciones necesarias para el juego"""


def definir_turnos(primero: str, segundo: str, ronda: int) -> list:
    """Para cada ronda definir quien empieza el juego y con que valor X/O juega cada jugador"""
    turno1, turno2, valor1, valor2 = "", "", "", ""
    if ronda % 2 == 0:
        turno1, valor1, turno2, valor2 = segundo, 'X', primero, 'O'

    else:
        turno1, valor1, turno2, valor2 = primero, 'X', segundo, 'O'

    return [turno1, valor1, turno2, valor2]


def validar_posicion(disponibles: list, jugador: str) -> int:
    """Pedir al usuario, ingresar una posicion y retornarla para actualizar el tablero"""
    while True:
        try:
            entrada_usuario = int(
                input(f'{jugador} Ingresa una posicion 1-9 para marcar en le tablero: '))
            if entrada_usuario in disponibles:
                return entrada_usuario
            else:
                print(
                    f'la posicion {entrada_usuario} está ocupada o no es valida, pruebe nuevamente ')
        except ValueError:
            print('Error al ingresar la posicion, valor no valido')


def actualizar_tablero(tabla: list, posicion: int, valor: str) -> list:
    """reemplazar y actualizar cada posicion validada con el valor X/O por cada jugador"""
    tabla[posicion - 1] = valor
    return tabla


def validar_ganador(combinaciones: list, tablero: list, jugador: str):
    """ Recibir el tablero y validar si un jugador ha hecho tricky"""
    for combinacion in combinaciones:
        if all(tablero[int(num)] == jugador for num in combinacion):
            return True

    return False


def mostrar_tablero(tablero: list, victorias: dict, j1: str, j2: str, disponibles: list):
    """Mostrar e imprimir el marcador de victorias, el tabalero actualizado en cada ronda e iteracion"""
    print('\033[1mVICTORIAS:\033[0m ')
    print(f'{j1.lower()} == {victorias[j1]} ------- {j2.lower()} == {victorias[j2]} ')  # noqa
    print(
        f'Posiciones disponibles tablero: {[i for i in disponibles]} \n')

    for casilla in range(0, len(tablero), 3):
        fila = tablero[casilla:casilla+3]
        print(' | '.join(fila))
        print('----------' if casilla < 6 else '')
    print('\n')
