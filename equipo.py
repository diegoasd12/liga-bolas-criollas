class Equipo:

    def __init__(self, nombre):

        self.nombre = nombre
        self.jugadores = []

    def agregar_jugador(self, jugador):

        self.jugadores.append(jugador)

    def mostrar_jugadores(self):

        print(f"\nEquipo: {self.nombre}")

        for jugador in self.jugadores:

            print(jugador)

    def __str__(self):

        return (
            f"Equipo: {self.nombre} | "
            f"Jugadores: {len(self.jugadores)}"
        )