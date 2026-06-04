import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from liga import Liga
from equipo import Equipo
from jugador import Jugador
from partido import Partido


liga = Liga("Club Demócrata")


def buscar_equipo(nombre):

    for equipo in liga.equipos:
        if equipo.nombre == nombre:
            return equipo

    return None


def crear_ventana(titulo, ancho, alto):

    ventana = tk.Toplevel(root)

    ventana.title(titulo)

    ventana.geometry(f"{ancho}x{alto}")

    ventana.resizable(False, False)

    return ventana


def error(texto):

    messagebox.showerror("Error", texto)


def exito(texto):

    messagebox.showinfo("Éxito", texto)


def registrar_equipo():

    nombre = entry_equipo.get()

    if nombre == "":
        error("Ingrese un nombre.")

        return

    equipo = Equipo(nombre)

    liga.registrar_equipo(equipo)

    exito("Equipo registrado correctamente.")

    entry_equipo.delete(0, tk.END)


def ventana_registrar_jugador():

    ventana = crear_ventana("Registrar Jugador", 400, 450)

    tk.Label(ventana, text="Nombre").pack(pady=5)

    entry_nombre = tk.Entry(ventana, width=30)

    entry_nombre.pack()

    tk.Label(ventana, text="Cédula").pack(pady=5)

    entry_cedula = tk.Entry(ventana, width=30)

    entry_cedula.pack()

    tk.Label(ventana, text="Edad").pack(pady=5)

    entry_edad = tk.Entry(ventana, width=30)

    entry_edad.pack()

    tk.Label(ventana, text="Posición").pack(pady=5)

    entry_posicion = tk.Entry(ventana, width=30)

    entry_posicion.pack()

    tk.Label(ventana, text="Equipo").pack(pady=5)

    combo_equipos = ttk.Combobox(
        ventana, values=[equipo.nombre for equipo in liga.equipos], width=27
    )

    combo_equipos.pack()

    def guardar_jugador():

        try:
            jugador = Jugador(
                entry_nombre.get(),
                entry_cedula.get(),
                int(entry_edad.get()),
                entry_posicion.get(),
            )

            equipo = buscar_equipo(combo_equipos.get())

            if not equipo:
                error("Equipo no encontrado.")

                return

            equipo.agregar_jugador(jugador)

            exito("Jugador registrado.")

            ventana.destroy()

        except ValueError:
            error("Datos inválidos.")

    tk.Button(ventana, text="Guardar Jugador", width=20, command=guardar_jugador).pack(
        pady=20
    )


def ventana_registrar_partido():

    ventana = crear_ventana("Registrar Partido", 500, 650)

    tk.Label(ventana, text="Equipo 1").pack(pady=5)

    combo1 = ttk.Combobox(
        ventana, values=[equipo.nombre for equipo in liga.equipos], width=30
    )

    combo1.pack()

    tk.Label(ventana, text="Equipo 2").pack(pady=5)

    combo2 = ttk.Combobox(
        ventana, values=[equipo.nombre for equipo in liga.equipos], width=30
    )

    combo2.pack()

    tk.Label(ventana, text="Puntos Equipo 1").pack(pady=5)

    entry_p1 = tk.Entry(ventana, width=30)

    entry_p1.pack()

    tk.Label(ventana, text="Puntos Equipo 2").pack(pady=5)

    entry_p2 = tk.Entry(ventana, width=30)

    entry_p2.pack()

    frame_stats = tk.Frame(ventana)

    frame_stats.pack(pady=15)

    entradas_jugadores = []

    def cargar_jugadores():

        for widget in frame_stats.winfo_children():
            widget.destroy()

        entradas_jugadores.clear()

        equipo1 = buscar_equipo(combo1.get())

        equipo2 = buscar_equipo(combo2.get())

        fila = 0

        tk.Label(frame_stats, text="Jugador").grid(row=fila, column=0)

        tk.Label(frame_stats, text="Lanzadas").grid(row=fila, column=1)

        tk.Label(frame_stats, text="Acertadas").grid(row=fila, column=2)

        fila += 1

        for equipo in [equipo1, equipo2]:
            if not equipo:
                continue

            tk.Label(frame_stats, text=f"Jugadores {equipo.nombre}").grid(
                row=fila, column=0, columnspan=3, pady=10
            )

            fila += 1

            for jugador in equipo.jugadores:
                tk.Label(frame_stats, text=jugador.nombre).grid(row=fila, column=0)

                entry_lanzadas = tk.Entry(frame_stats, width=10)

                entry_lanzadas.grid(row=fila, column=1)

                entry_acertadas = tk.Entry(frame_stats, width=10)

                entry_acertadas.grid(row=fila, column=2)

                entradas_jugadores.append((jugador, entry_lanzadas, entry_acertadas))

                fila += 1

    tk.Button(
        ventana, text="Cargar Jugadores", width=20, command=cargar_jugadores
    ).pack(pady=10)

    def guardar_partido():

        try:
            if combo1.get() == combo2.get():
                error("Seleccione equipos diferentes.")

                return

            equipo1 = buscar_equipo(combo1.get())

            equipo2 = buscar_equipo(combo2.get())

            partido = Partido(
                equipo1, equipo2, int(entry_p1.get()), int(entry_p2.get())
            )

            ganador = partido.determinar_ganador()

            liga.registrar_partido(partido)

            for jugador, lanzadas, acertadas in entradas_jugadores:
                jugador.registrar_estadisticas(
                    int(lanzadas.get()), int(acertadas.get())
                )

            messagebox.showinfo("Partido", f"Ganador: {ganador}")

            ventana.destroy()

        except ValueError:
            error("Datos inválidos.")

    tk.Button(ventana, text="Guardar Partido", width=20, command=guardar_partido).pack(
        pady=20
    )


def ver_equipos():

    ventana = crear_ventana("Equipos", 700, 500)

    texto = tk.Text(ventana, width=80, height=30)

    texto.pack(pady=10)

    for equipo in liga.equipos:
        texto.insert(tk.END, f"{equipo}\n")

        for jugador in equipo.jugadores:
            texto.insert(tk.END, f"   - {jugador}\n")

        texto.insert(tk.END, "\n")


def tabla_posiciones():

    ventana = crear_ventana("Tabla", 500, 400)

    texto = tk.Text(ventana, width=60, height=20)

    texto.pack(pady=10)

    equipos_ordenados = sorted(
        liga.equipos, key=lambda equipo: equipo.victorias, reverse=True
    )

    for equipo in equipos_ordenados:
        texto.insert(
            tk.END,
            f"{equipo.nombre} | "
            f"Victorias: {equipo.victorias} | "
            f"Derrotas: {equipo.derrotas}\n",
        )


def mejores_jugadores():

    ventana = crear_ventana("Mejores Jugadores", 500, 400)

    texto = tk.Text(ventana, width=60, height=20)

    texto.pack(pady=10)

    jugadores = []

    for equipo in liga.equipos:
        for jugador in equipo.jugadores:
            jugadores.append((jugador, equipo.nombre))

    jugadores.sort(key=lambda dato: dato[0].calcular_porcentaje(), reverse=True)

    for jugador, equipo in jugadores:
        texto.insert(
            tk.END,
            f"{jugador.nombre} | {equipo} | {jugador.calcular_porcentaje():.2f}%\n",
        )


def guardar_datos():

    liga.guardar_datos()

    messagebox.showinfo("Guardar", "Datos guardados.")


def cargar_datos():

    liga.cargar_datos()

    messagebox.showinfo("Cargar", "Datos cargados.")


root = tk.Tk()

root.title("Liga de Bolas Criollas")

root.geometry("550x700")

root.resizable(False, False)

titulo = tk.Label(root, text="CLUB DEMÓCRATA", font=("Arial", 22, "bold"))

titulo.pack(pady=20)

subtitulo = tk.Label(root, text="Sistema de Gestión", font=("Arial", 12))

subtitulo.pack(pady=5)

tk.Label(root, text="Nombre del equipo").pack(pady=5)

entry_equipo = tk.Entry(root, width=35)

entry_equipo.pack(pady=5)

tk.Button(root, text="Registrar Equipo", width=25, command=registrar_equipo).pack(
    pady=10
)

botones = [
    ("Registrar Jugador", ventana_registrar_jugador),
    ("Registrar Partido", ventana_registrar_partido),
    ("Ver Equipos", ver_equipos),
    ("Tabla de Posiciones", tabla_posiciones),
    ("Mejores Jugadores", mejores_jugadores),
    ("Guardar Datos", guardar_datos),
    ("Cargar Datos", cargar_datos),
]

for texto, comando in botones:
    tk.Button(root, text=texto, width=25, command=comando).pack(pady=10)

tk.Button(root, text="Salir", width=25, command=root.quit).pack(pady=25)

root.mainloop()
