import tricky



tablero_numeros = ['1', '2', '3',
                   '4', '5', '6',
                   '7', '8', '9']


print(
    '\n   \033[1m  ---------- BIENVENIDO - JUGUEMOS TRICKY O TIC-TAC-TOE ------ \033[0m ')
print(' \033[1m Estos son los numeros de cada posicion en el tablero, recuerdalos bien \033[0m \n')

for i in range(0, 9, 3):
    fila = tablero_numeros[i:i + 3]
    print(' | '.join(fila))
    print('----------' if i < 6 else '')

while True:
    print('Selecciona el modo de juego, escribe el numero de la opcion o ingresa 3 para salir: ')
    print('1. Jugar con la maquina')
    print('2. Jugar con otra persona ')
    print('3. Salir del juego')

    entrada_usuario = input('Ingresa el numero de la opcion aquí: ')
    print('\n')
    if entrada_usuario == '1':
        vs_maquina = tricky.tricky()
        print(vs_maquina)
    elif entrada_usuario == '3':
        break
