from tkinter import *
from tkinter import ttk

def Mensaje_jiji():
    etiqueta_text.set("La posicion esta en 1")

root = Tk()
root.title("nose")

mainframe = ttk.Frame(root, padding="10 10 10 10")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

etiqueta_text = StringVar()
etiqueta_text.set("")

ttk.Label(mainframe, textvariable=etiqueta_text).grid(column=2, row=1, sticky=(W, E))

ttk.Button(mainframe, text="Presiona bb", command=Mensaje_jiji).grid(column=1, row=1, sticky=W)
ttk.Button(mainframe, text="Presiona bb", command=Mensaje_jiji).grid(column=1, row=2, sticky=W)
ttk.Button(mainframe, text="Presiona bb", command=Mensaje_jiji).grid(column=1, row=3, sticky=W)
ttk.Button(mainframe, text="Presiona bb", command=Mensaje_jiji).grid(column=2, row=1, sticky=W)
ttk.Button(mainframe, text="Presiona bb", command=Mensaje_jiji).grid(column=2, row=2, sticky=W)
ttk.Button(mainframe, text="Presiona bb", command=Mensaje_jiji).grid(column=2, row=3, sticky=W)
ttk.Button(mainframe, text="Presiona bb", command=Mensaje_jiji).grid(column=3, row=1, sticky=W)
ttk.Button(mainframe, text="Presiona bb", command=Mensaje_jiji).grid(column=3, row=2, sticky=W)
ttk.Button(mainframe, text="Presiona bb", command=Mensaje_jiji).grid(column=3, row=3, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.mainloop()
