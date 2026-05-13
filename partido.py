class Partido:

    def __init__(
        self,
        equipo1,
        equipo2,
        puntos1,
        puntos2
    ):

        self.equipo1 = equipo1
        self.equipo2 = equipo2

        self.puntos1 = puntos1
        self.puntos2 = puntos2

    def determinar_ganador(self):

        if self.puntos1 > self.puntos2:

            self.equipo1.registrar_victoria()
            self.equipo2.registrar_derrota()

            return self.equipo1.nombre

        elif self.puntos2 > self.puntos1:

            self.equipo2.registrar_victoria()
            self.equipo1.registrar_derrota()

            return self.equipo2.nombre

        return "Empate"

    def __str__(self):

        return (
            f"{self.equipo1.nombre} "
            f"{self.puntos1} - "
            f"{self.puntos2} "
            f"{self.equipo2.nombre}"
        )