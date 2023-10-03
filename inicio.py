# Importamos los modulos '.py' (contienen y ejecutan el juego) para ser llamados luego:
import jcj
import jvs_ia


def mostrar_menu():
    # representacion de las posiciones del juego y sus respectivos numeros:
    tablero_numeros = ['1', '2', '3',
                       '4', '5', '6',
                       '7', '8', '9']

    # Mensaje inicial de bienvenida:
    print(
        '\n   \033[1m  ---------- BIENVENIDO - JUGUEMOS TRICKY O TIC-TAC-TOE ------ \033[0m ')
    print(
        ' \033[1m Estos son los numeros de cada posicion en el tablero, recuerdalos bien \033[0m \n')

    # Imprimir el tablero representativo con los numeros de las posiciones y el menu de opciones del juego:
    for i in range(0, 9, 3):
        fila = tablero_numeros[i:i + 3]
        print(' | '.join(fila))
        print('----------' if i < 6 else '')

    print('MENÚ DE OPCIONES')
    print('1. Jugar con la maquina')
    print('2. Jugar con otra persona ')
    print('3. Salir del juego \n')


# Pedir al usuario ingresar una opcion del menu anterior, validar cada caso y pasarlo a la funcion main():
while True:
    try:
        mostrar_menu()
        entrada_usuario = input('Ingresa el numero de la opcion aquí: ')
        print('\n')
        if entrada_usuario in ['1', '2', '3']:
            if entrada_usuario == '1':
                vs_maquina = jvs_ia
            elif entrada_usuario == '2':
                uno_vs_uno = jcj.juego_JCJ()
            else:
                break
        else:
            print('¡Ingrese una opcion valida!')
    except ValueError:
        print('Ingrese valores validos')
