#crear una gui en la que se muestre las faltas de un alumno, dando la opcion de editar la misma.
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

paso = False

def login():
    global paso
    if paso == True :
        print("si")
        paso = False
    else:
        print("no")
        paso = True

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me", command=login)
checkbox.pack(pady=12, padx=10)

root.mainloop()