from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class Gato:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Juego del Gato")
        self.tablero = [' ' for _ in range(9)]
        self.jugador_actual = 'X'
        self.botones = [None] * 9
        self.crear_botones()

    def crear_botones(self):
        for i in range(9):
            boton = ttk.Button(self.raiz, text=' ', command=lambda i=i: self.realizar_jugada(i), width=10)
            boton.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.botones[i] = boton

    def realizar_jugada(self, posicion):
        if self.tablero[posicion] == ' ':
            self.tablero[posicion] = self.jugador_actual
            self.botones[posicion].config(text=self.jugador_actual)
            ganador = self.verificar_ganador()
            if ganador:
                messagebox.showinfo("Fin del juego", f"¡El jugador {ganador} ha ganado!")
                self.reiniciar_juego()
            elif ' ' not in self.tablero:
                messagebox.showinfo("Fin del juego", "¡Es un empate!")
                self.reiniciar_juego()
            else:
                self.jugador_actual = 'O' if self.jugador_actual == 'X' else 'X'

    def verificar_ganador(self):
        combinaciones = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for a, b, c in combinaciones:
            if self.tablero[a] == self.tablero[b] == self.tablero[c] != ' ':
                return self.tablero[a]
        return None

    def reiniciar_juego(self):
        self.tablero = [' ' for _ in range(9)]
        self.jugador_actual = 'X'
        for boton in self.botones:
            boton.config(text=' ')

raiz = Tk()
juego = Gato(raiz)
raiz.mainloop()