import tkinter as tk
from tkinter import messagebox

from liga import Liga
from equipo import Equipo
from jugador import Jugador


liga = Liga("Club Demócrata")


def registrar_equipo():

    nombre = entry_equipo.get()

    if nombre == "":

        messagebox.showerror(
            "Error",
            "Ingrese un nombre."
        )

        return

    equipo = Equipo(nombre)

    liga.registrar_equipo(equipo)

    messagebox.showinfo(
        "Éxito",
        "Equipo registrado correctamente."
    )

    entry_equipo.delete(0, tk.END)


def ver_equipos():

    ventana = tk.Toplevel(root)

    ventana.title("Equipos")

    texto = tk.Text(
        ventana,
        width=60,
        height=20
    )

    texto.pack()

    for equipo in liga.equipos:

        texto.insert(
            tk.END,
            f"{equipo}\n"
        )

        for jugador in equipo.jugadores:

            texto.insert(
                tk.END,
                f"   - {jugador}\n"
            )

        texto.insert(tk.END, "\n")


root = tk.Tk()

root.title("Liga de Bolas Criollas")

root.geometry("500x400")


titulo = tk.Label(
    root,
    text="SISTEMA BOLAS CRIOLLAS",
    font=("Arial", 18, "bold")
)

titulo.pack(pady=20)


label_equipo = tk.Label(
    root,
    text="Nombre del equipo"
)

label_equipo.pack()

entry_equipo = tk.Entry(
    root,
    width=30
)

entry_equipo.pack(pady=5)


boton_equipo = tk.Button(
    root,
    text="Registrar Equipo",
    command=registrar_equipo
)

boton_equipo.pack(pady=10)

boton_ver = tk.Button(
    root,
    text="Ver Equipos",
    command=ver_equipos
)

boton_ver.pack(pady=10)

boton_salir = tk.Button(
    root,
    text="Salir",
    command=root.quit
)

boton_salir.pack(pady=20)


root.mainloop()