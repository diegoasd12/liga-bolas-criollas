from persona import Persona


class Jugador(Persona):

    def __init__(
        self,
        nombre,
        cedula,
        edad,
        posicion
    ):

        super().__init__(
            nombre,
            cedula,
            edad
        )

        self.posicion = posicion
        self.puntos = 0

    def registrar_puntos(self, puntos):

        self.puntos += puntos

    def mostrar_info(self):

        return (
            f"{super().mostrar_info()} | "
            f"Posición: {self.posicion} | "
            f"Puntos: {self.puntos}"
        )

    def __str__(self):

        return self.mostrar_info()