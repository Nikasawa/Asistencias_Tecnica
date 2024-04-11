#crear una gui en la que se muestre las faltas de un alumno, dando la opcion de editar la misma.
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def search_NA():
    #Abrir una ventana emergente con la informacion que se busco del alumno
    asistencias = customtkinter.CTk()
    asistencias.title("Asistencias")
    asistencias.geometry("850x500")
    asistencias.grid_columnconfigure((0), weight=1)

    asistencias.mainloop()
    print("test")

def search_DNI():
    asistencias = customtkinter.CTk()
    asistencias.title("Asistencias")
    asistencias.geometry("850x500")
    asistencias.grid_columnconfigure((0), weight=1)

    asistencias.mainloop()
    print("test")

#Caracteristicas principales de la ventana
app = customtkinter.CTk()
app.title("Busqueda")
app.geometry("550x400")
app.grid_columnconfigure((0), weight=1)

#Cuadro donde se encuentran los datos de busqueda por nombre y apellido
searchFrameNA = customtkinter.CTkFrame(app)
searchFrameNA.grid(row=0, column=0, padx=20, pady=10, sticky="we")

#Texto arriba de las cajas de texto
labelNombre = customtkinter.CTkLabel(searchFrameNA, text="Nombre")
labelNombre.grid(row=0, column=0, padx=20, pady=10, sticky="w")
labelApellido = customtkinter.CTkLabel(searchFrameNA, text="Apellido")
labelApellido.grid(row=0, column=1, padx=20, pady=10, sticky="w")

#Cajas de texto donde se ingresa el nombre y apellido del alumno
nombre = customtkinter.CTkTextbox(searchFrameNA)
nombre.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")
nombre.configure(height=15)
apellido = customtkinter.CTkTextbox(searchFrameNA)
apellido.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w")
apellido.configure(height=15)

#Boton para accionar la busqueda de datos por nombre y apellido
botonNA = customtkinter.CTkButton(searchFrameNA, text="Buscar", command=search_NA)
botonNA.grid(row=2, column=0, padx=20, pady=20, columnspan=2)

#Cuadro donde se encuentran los datos de busqueda por DNI
searchFrameDNI = customtkinter.CTkFrame(app)
searchFrameDNI.grid(row=1, column=0, padx=20, pady=10, sticky="w")

#Texto arriba de las cajas de texto
labelDNI = customtkinter.CTkLabel(searchFrameDNI, text="DNI")
labelDNI.grid(row=0, column=0, padx=20, pady=10, sticky="w")

#Cajas de texto donde se ingresa el DNI del alumno
DNI = customtkinter.CTkTextbox(searchFrameDNI)
DNI.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")
DNI.configure(height=15)

#Boton para accionar la busqueda de datos por DNI
botonDNI = customtkinter.CTkButton(searchFrameDNI, text="Buscar", command=search_NA)
botonDNI.grid(row=2, column=0, padx=20, pady=20, columnspan=2)

app.mainloop()