import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from liga import Liga
from equipo import Equipo
from jugador import Jugador
from partido import Partido


liga = Liga("Club Demócrata")


# ==================================================
# REGISTRAR EQUIPO
# ==================================================

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


# ==================================================
# REGISTRAR JUGADOR
# ==================================================

def ventana_registrar_jugador():

    ventana = tk.Toplevel(root)

    ventana.title("Registrar Jugador")

    ventana.geometry("400x450")

    tk.Label(
        ventana,
        text="Nombre"
    ).pack(pady=5)

    entry_nombre = tk.Entry(
        ventana,
        width=30
    )

    entry_nombre.pack()

    tk.Label(
        ventana,
        text="Cédula"
    ).pack(pady=5)

    entry_cedula = tk.Entry(
        ventana,
        width=30
    )

    entry_cedula.pack()

    tk.Label(
        ventana,
        text="Edad"
    ).pack(pady=5)

    entry_edad = tk.Entry(
        ventana,
        width=30
    )

    entry_edad.pack()

    tk.Label(
        ventana,
        text="Posición"
    ).pack(pady=5)

    entry_posicion = tk.Entry(
        ventana,
        width=30
    )

    entry_posicion.pack()

    tk.Label(
        ventana,
        text="Equipo"
    ).pack(pady=5)

    combo_equipos = ttk.Combobox(
        ventana,
        values=[
            equipo.nombre
            for equipo in liga.equipos
        ],
        width=27
    )

    combo_equipos.pack()

    def guardar_jugador():

        try:

            nombre = entry_nombre.get()

            cedula = entry_cedula.get()

            edad = int(entry_edad.get())

            posicion = entry_posicion.get()

            equipo_nombre = combo_equipos.get()

            equipo_encontrado = None

            for equipo in liga.equipos:

                if equipo.nombre == equipo_nombre:

                    equipo_encontrado = equipo

            if equipo_encontrado:

                jugador = Jugador(
                    nombre,
                    cedula,
                    edad,
                    posicion
                )

                equipo_encontrado.agregar_jugador(
                    jugador
                )

                messagebox.showinfo(
                    "Éxito",
                    "Jugador registrado."
                )

                ventana.destroy()

            else:

                messagebox.showerror(
                    "Error",
                    "Equipo no encontrado."
                )

        except ValueError:

            messagebox.showerror(
                "Error",
                "Datos inválidos."
            )

    tk.Button(
        ventana,
        text="Guardar Jugador",
        width=20,
        command=guardar_jugador
    ).pack(pady=20)


# ==================================================
# REGISTRAR PARTIDO
# ==================================================

def ventana_registrar_partido():

    ventana = tk.Toplevel(root)

    ventana.title("Registrar Partido")

    ventana.geometry("500x650")

    tk.Label(
        ventana,
        text="Equipo 1"
    ).pack(pady=5)

    combo1 = ttk.Combobox(
        ventana,
        values=[
            equipo.nombre
            for equipo in liga.equipos
        ],
        width=30
    )

    combo1.pack()

    tk.Label(
        ventana,
        text="Equipo 2"
    ).pack(pady=5)

    combo2 = ttk.Combobox(
        ventana,
        values=[
            equipo.nombre
            for equipo in liga.equipos
        ],
        width=30
    )

    combo2.pack()

    tk.Label(
        ventana,
        text="Puntos Equipo 1"
    ).pack(pady=5)

    entry_p1 = tk.Entry(
        ventana,
        width=30
    )

    entry_p1.pack()

    tk.Label(
        ventana,
        text="Puntos Equipo 2"
    ).pack(pady=5)

    entry_p2 = tk.Entry(
        ventana,
        width=30
    )

    entry_p2.pack()

    frame_stats = tk.Frame(
        ventana
    )

    frame_stats.pack(pady=15)

    entradas_jugadores = []

    def cargar_jugadores():

        for widget in frame_stats.winfo_children():

            widget.destroy()

        entradas_jugadores.clear()

        equipo1 = None
        equipo2 = None

        for equipo in liga.equipos:

            if equipo.nombre == combo1.get():

                equipo1 = equipo

            if equipo.nombre == combo2.get():

                equipo2 = equipo

        fila = 0

        if equipo1:

            tk.Label(
                frame_stats,
                text=f"Jugadores {equipo1.nombre}"
            ).grid(
                row=fila,
                column=0,
                columnspan=3
            )

            fila += 1

            for jugador in equipo1.jugadores:

                tk.Label(
                    frame_stats,
                    text=jugador.nombre
                ).grid(
                    row=fila,
                    column=0
                )

                entry_lanzadas = tk.Entry(
                    frame_stats,
                    width=10
                )

                entry_lanzadas.grid(
                    row=fila,
                    column=1
                )

                entry_acertadas = tk.Entry(
                    frame_stats,
                    width=10
                )

                entry_acertadas.grid(
                    row=fila,
                    column=2
                )

                entradas_jugadores.append(
                    (
                        jugador,
                        entry_lanzadas,
                        entry_acertadas
                    )
                )

                fila += 1

        if equipo2:

            tk.Label(
                frame_stats,
                text=f"Jugadores {equipo2.nombre}"
            ).grid(
                row=fila,
                column=0,
                columnspan=3,
                pady=10
            )

            fila += 1

            for jugador in equipo2.jugadores:

                tk.Label(
                    frame_stats,
                    text=jugador.nombre
                ).grid(
                    row=fila,
                    column=0
                )

                entry_lanzadas = tk.Entry(
                    frame_stats,
                    width=10
                )

                entry_lanzadas.grid(
                    row=fila,
                    column=1
                )

                entry_acertadas = tk.Entry(
                    frame_stats,
                    width=10
                )

                entry_acertadas.grid(
                    row=fila,
                    column=2
                )

                entradas_jugadores.append(
                    (
                        jugador,
                        entry_lanzadas,
                        entry_acertadas
                    )
                )

                fila += 1

    tk.Button(
        ventana,
        text="Cargar Jugadores",
        width=20,
        command=cargar_jugadores
    ).pack(pady=10)

    def guardar_partido():

        try:

            equipo1 = None
            equipo2 = None

            for equipo in liga.equipos:

                if equipo.nombre == combo1.get():

                    equipo1 = equipo

                if equipo.nombre == combo2.get():

                    equipo2 = equipo

            puntos1 = int(
                entry_p1.get()
            )

            puntos2 = int(
                entry_p2.get()
            )

            partido = Partido(
                equipo1,
                equipo2,
                puntos1,
                puntos2
            )

            ganador = partido.determinar_ganador()

            liga.registrar_partido(
                partido
            )

            for datos in entradas_jugadores:

                jugador = datos[0]

                lanzadas = int(
                    datos[1].get()
                )

                acertadas = int(
                    datos[2].get()
                )

                jugador.registrar_estadisticas(
                    lanzadas,
                    acertadas
                )

            messagebox.showinfo(
                "Partido",
                f"Ganador: {ganador}"
            )

            ventana.destroy()

        except ValueError:

            messagebox.showerror(
                "Error",
                "Datos inválidos."
            )

    tk.Button(
        ventana,
        text="Guardar Partido",
        width=20,
        command=guardar_partido
    ).pack(pady=20)


# ==================================================
# VER EQUIPOS
# ==================================================

def ver_equipos():

    ventana = tk.Toplevel(root)

    ventana.title("Equipos")

    ventana.geometry("700x500")

    texto = tk.Text(
        ventana,
        width=80,
        height=30
    )

    texto.pack(pady=10)

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

        texto.insert(
            tk.END,
            "\n"
        )


# ==================================================
# TABLA
# ==================================================

def tabla_posiciones():

    ventana = tk.Toplevel(root)

    ventana.title("Tabla")

    ventana.geometry("500x400")

    texto = tk.Text(
        ventana,
        width=60,
        height=20
    )

    texto.pack(pady=10)

    equipos_ordenados = sorted(
        liga.equipos,
        key=lambda equipo:
        equipo.victorias,
        reverse=True
    )

    for equipo in equipos_ordenados:

        texto.insert(
            tk.END,
            f"{equipo.nombre} | "
            f"Victorias: {equipo.victorias} | "
            f"Derrotas: {equipo.derrotas}\n"
        )


# ==================================================
# MEJORES JUGADORES
# ==================================================

def mejores_jugadores():

    ventana = tk.Toplevel(root)

    ventana.title(
        "Mejores Jugadores"
    )

    ventana.geometry("500x400")

    texto = tk.Text(
        ventana,
        width=60,
        height=20
    )

    texto.pack(pady=10)

    jugadores = []

    for equipo in liga.equipos:

        for jugador in equipo.jugadores:

            jugadores.append(
                (jugador, equipo.nombre)
            )

    jugadores.sort(
        key=lambda dato:
        dato[0].calcular_porcentaje(),
        reverse=True
    )

    for jugador, equipo in jugadores:

        texto.insert(
            tk.END,
            f"{jugador.nombre} | "
            f"{equipo} | "
            f"{jugador.calcular_porcentaje():.2f}%\n"
        )


# ==================================================
# GUARDAR
# ==================================================

def guardar_datos():

    liga.guardar_datos()

    messagebox.showinfo(
        "Guardar",
        "Datos guardados."
    )


# ==================================================
# CARGAR
# ==================================================

def cargar_datos():

    liga.cargar_datos()

    messagebox.showinfo(
        "Cargar",
        "Datos cargados."
    )


# ==================================================
# VENTANA PRINCIPAL
# ==================================================

root = tk.Tk()

root.title(
    "Liga de Bolas Criollas"
)

root.geometry("550x700")

titulo = tk.Label(
    root,
    text="CLUB DEMÓCRATA",
    font=("Arial", 22, "bold")
)

titulo.pack(pady=20)

subtitulo = tk.Label(
    root,
    text="Sistema de Gestión",
    font=("Arial", 12)
)

subtitulo.pack(pady=5)

tk.Label(
    root,
    text="Nombre del equipo"
).pack(pady=5)

entry_equipo = tk.Entry(
    root,
    width=35
)

entry_equipo.pack(pady=5)

tk.Button(
    root,
    text="Registrar Equipo",
    width=25,
    command=registrar_equipo
).pack(pady=10)

tk.Button(
    root,
    text="Registrar Jugador",
    width=25,
    command=ventana_registrar_jugador
).pack(pady=10)

tk.Button(
    root,
    text="Registrar Partido",
    width=25,
    command=ventana_registrar_partido
).pack(pady=10)

tk.Button(
    root,
    text="Ver Equipos",
    width=25,
    command=ver_equipos
).pack(pady=10)

tk.Button(
    root,
    text="Tabla de Posiciones",
    width=25,
    command=tabla_posiciones
).pack(pady=10)

tk.Button(
    root,
    text="Mejores Jugadores",
    width=25,
    command=mejores_jugadores
).pack(pady=10)

tk.Button(
    root,
    text="Guardar Datos",
    width=25,
    command=guardar_datos
).pack(pady=10)

tk.Button(
    root,
    text="Cargar Datos",
    width=25,
    command=cargar_datos
).pack(pady=10)

tk.Button(
    root,
    text="Salir",
    width=25,
    command=root.quit
).pack(pady=25)

root.mainloop()