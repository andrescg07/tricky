# importamos los modulos que necesitamos:


# validar la dificultad del juego deseada
def validar_nivel() -> str:
    """Pedir al usuario que escoja la dificultad del juego vs La maquina, validarlo y retornarlo"""
    while True:
        nivel = input(
            "Ingrese el nivel de dificultad de la IA, 'facil'/ 'dificil': ")
        if nivel.lower() == 'dificil' or nivel.lower() == 'dificil':
            return nivel
        else:
            print('¡Opcion no valida, ese nivel no existe!')

# Funcion principal para el modo de juego Jugador contra IA:


def juego_JvsIA():
    """ jugar el modo contra la IA """
