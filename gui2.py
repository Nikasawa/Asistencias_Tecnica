# Este es un ejemplo que tome que muestra como se establecen los valores dentro del modulo
# Esta traducida mas o menos asi que es mas que nada a la interpretacion
# Tiene otras formas de establecer los tipos de variables ya que en realidad esta biblioteca funciona como
# un puente entre python y el Tcl/Tk
import tkinter as tk
from tkinter import *

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("this is a variable")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<Key-Return>', self.print_contents)
        boton = Button(self, fg="red")

    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())

root = tk.Tk()
myapp = App(root)
myapp.mainloop()