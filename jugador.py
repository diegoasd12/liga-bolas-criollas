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

        self.__posicion = posicion
        self.__puntos = 0

    @property
    def posicion(self):

        return self.__posicion

    @property
    def puntos(self):

        return self.__puntos

    def registrar_puntos(self, puntos):

        self.__puntos += puntos

    def mostrar_info(self):

        return (
            f"{super().mostrar_info()} | "
            f"Posición: {self.__posicion} | "
            f"Puntos: {self.__puntos}"
        )

    def __str__(self):

        return self.mostrar_info()