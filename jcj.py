# importamos los modulos que necesitamos:
import tricky

# Funcion principal para el modo de juego Jugador contra Jugador:


def juego_JCJ():
    """ jugar el modo Jugador contra jugador"""
    while True:
        iniciar_juego = tricky.main('JCJ')
        print('OPCIONES')
        print('1.Continuar jugando// 2.Salir del juego// 3.Volver a Menú principal ')
        seguir_jugando = input('Ingrese el numero de la opcion (1,2,3): ')

        if seguir_jugando == '2':
            exit()
        elif seguir_jugando == '3':
            break

    return 'Menú'
