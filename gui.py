"""
Inicio de prueba y/o implementacion del sistema GUI
"""

# Libreria que permite la creacion de la ventana grafica
from tkinter import *
from tkinter import ttk

color = "red"

def cambioColor():
    global color
    if color == "red":
        color = "blue"
    else:
        color = "red"
    print(color)
    qsy.config(fg=color)

# La estructura de la ventana funciona de la misma manera que lo hacen las paginas HTML
root = Tk() # Ventana raiz
frm = ttk.Frame(root, padding=10) # Ventana principal que se abre primero en la raiz
frm.grid() # Esto es como configurarlo como si fuese un div, dejandolo mas abajo en la jerarquia de la estructura
ttk.Label(frm, text="Hello World!").grid(column=0, row=0) # Texto

# Boton, el command es para llamar a una funcion, 
# puede ser alguna que tenga por defecto o que hayamos creado nosotros
ttk.Button(frm, text="Quit", command=root.destroy, width=10).grid(column=1, row=0) 
qsy = Button(frm, fg=color, text="qsy", command=cambioColor).grid(column=0, row=1)



# Puede ser util llamar al objeto con el que tengamos dudas con la funcion "keys()", esto devuelve una lista de todos los parametros y
# configuraciones que tiene el objeto
""" print(ttk.Button().keys()) """ 



# Funcion que mantiene la ventana y permite que respona a la interaccion del usuario (obligatoria) 
root.mainloop()