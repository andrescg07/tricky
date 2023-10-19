"""Importar librerias tkinter, PIL, pygame,sys 
para diseñar las iterfaces graficas y ejecutable del juego"""

import tkinter as tk
from PIL import Image, ImageTk
import ia


# ---------------------------------------------------

cascadia_titulos = ("Cascadia Code", 29, "bold")
cascadia_botones = ("Cascadia Code", 12, "bold")

# --------------------------------------------------------
FACIL = 'facil'
DIFICIL = 'dificil'


def obtener_nombre(dificultad, ventana):
    ventana.destroy()
    nombre = tk.Tk()
    nombre.title("Nombres de Jugadores")
    nombre.iconbitmap("logo.ico")
    nombre.config(bg="#66CDAA")
    nombre.geometry("500x300")
    nombre.resizable(False, False)

    etiqueta_jugador = tk.Label(
        nombre, text="Nombre del Jugador:", bg="#66CDAA", font=cascadia_botones)
    etiqueta_jugador.place(x=150, y=25)

    entrada_jugador = tk.Entry(nombre)
    entrada_jugador.place(x=170, y=60)

    boton_comenzar = tk.Button(nombre, text="Comenzar Juego",
                               command=lambda: ia.empezar_juegoIa(dificultad, entrada_jugador.get(), nombre), font=cascadia_botones, activebackground="#66CDAA", cursor="hand2")
    boton_comenzar.place(x=160, y=110)


def abrir_vs_ia(home):
    home.destroy()
    ventana_vs_ia = tk.Tk()
    ventana_vs_ia.title("JUEGO CONTRA LA IA")
    ventana_vs_ia.iconbitmap("logo.ico")
    ventana_vs_ia.config(bg="#66CDAA")
    ventana_vs_ia.geometry("500x300")
    ventana_vs_ia.resizable(False, False)
    dificultad_tx = tk.Label(
        ventana_vs_ia, text="NIVEL DE DIFICULTAD", fg="black", bg="#66CDAA", font=cascadia_titulos)
    dificultad_tx.place(x=40, y=25)

    facil_boton = tk.Button(
        ventana_vs_ia, text="Facil", command=lambda: obtener_nombre(FACIL, ventana_vs_ia), font=cascadia_botones, activebackground="#66CDAA", cursor="hand2", padx=32, pady=10)
    facil_boton.place(x=110, y=130)

    dificil_boton = tk.Button(
        ventana_vs_ia, text="Dificil", font=cascadia_botones, activebackground="#66CDAA", cursor="hand2", padx=20, pady=10)
    dificil_boton.place(x=250, y=130)

    ventana_vs_ia.mainloop()


# --------------------------------------------------
# crear la raiz o interfaz principal del juego
raiz = tk.Tk()
raiz.geometry("800x800")
raiz.iconbitmap("logo.ico")
raiz.title("Tricky")
raiz.config(bg="#66CDAA")


# FRAME PARA MOSTRAR TITULO E IMAGEN DEL JUEGO
frame_inicio = tk.Frame(raiz)
frame_inicio.pack(fill="y", expand=True)
frame_inicio.config(width=850, height=300, bg="#F0F8FF")


# cargar, procesar el texto e imagen principal
abrir_img = Image.open("home.png")
ancho = 250
alto = 250
redimensionar = abrir_img.resize((ancho, alto), Image.LANCZOS)
home_img = ImageTk.PhotoImage(redimensionar)

# Crear fuente en negrita para el título

tk.Label(frame_inicio, text="TRICKY", bg="#F0F8FF", fg="green",
         font=cascadia_titulos).place(x=315, y=12)
tk.Label(frame_inicio, image=home_img, bg="#F0F8FF").place(
    x=270, y=90)


# GRID PARA MOSTRAR BOTONES DE LAS OPCIONES DE JUEGO

ia_boton = tk.Button(
    frame_inicio, command=lambda: abrir_vs_ia(raiz), text="Jugar contra la IA", font=cascadia_botones, activebackground="#66CDAA", cursor="hand2", padx=32, pady=10)
ia_boton.place(x=280, y=410)

jcj_boton = tk.Button(
    frame_inicio, text="Jugar contra otra persona", font=cascadia_botones, activebackground="#66CDAA", cursor="hand2", pady=10)
jcj_boton.place(x=280, y=475)

salir_boton = tk.Button(
    frame_inicio, text="Salir", font=cascadia_botones, cursor="hand2", activebackground="#66CDAA", padx=90, pady=10)
salir_boton.place(x=280, y=540)
raiz.mainloop()
