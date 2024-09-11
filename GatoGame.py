from tkinter import *
from tkinter import messagebox, ttk

class Gato:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Juego del Gato")
        self.tablero, self.jugador_actual = [' '] * 9, 'X'
        self.botones = [ttk.Button(raiz, text=' ', command=lambda i=i: self.jugar(i), width=10) for i in range(9)]
        for i, boton in enumerate(self.botones): boton.grid(row=i // 3, column=i % 3)

    def jugar(self, pos):
        if self.tablero[pos] == ' ':
            self.tablero[pos] = self.jugador_actual
            self.botones[pos].config(text=self.jugador_actual)
            if (ganador := self.verificar_ganador()) or ' ' not in self.tablero:
                messagebox.showinfo("Fin", f"¡El jugador {ganador} ha ganado!" if ganador else "¡Es un empate!")
                self.reiniciar()
            self.jugador_actual = 'X' if self.jugador_actual == 'O' else 'O'

    def verificar_ganador(self):
        return next((self.tablero[a] for a, b, c in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)] if self.tablero[a] == self.tablero[b] == self.tablero[c] != ' '), None)

    def reiniciar(self):
        self.tablero, self.jugador_actual = [' '] * 9, 'O'
        for boton in self.botones: boton.config(text=' ')

raiz = Tk()
juego = Gato(raiz)
raiz.mainloop()