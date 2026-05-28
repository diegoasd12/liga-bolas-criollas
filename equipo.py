class Equipo:

    def __init__(self, nombre):

        self.nombre = nombre

        self.jugadores = []

        self.victorias = 0
        self.derrotas = 0

    def agregar_jugador(self, jugador):

        self.jugadores.append(jugador)

    def registrar_victoria(self):

        self.victorias += 1

    def registrar_derrota(self):

        self.derrotas += 1

    def mostrar_jugadores(self):

        print(f"\nJugadores del equipo {self.nombre}:")

        if len(self.jugadores) == 0:

            print("No hay jugadores registrados.")
            return

        for jugador in self.jugadores:

            print(f" - {jugador}")

    def __str__(self):

        return (
            f"Equipo: {self.nombre} | "
            f"Victorias: {self.victorias} | "
            f"Derrotas: {self.derrotas}"
        )