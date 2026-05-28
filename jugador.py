from persona import Persona


class Jugador(Persona):

    def __init__(self, nombre, cedula, edad, posicion):

        super().__init__(nombre, cedula, edad)

        self.__posicion = posicion
        self.__bolas_lanzadas = 0
        self.__bolas_acertadas = 0

    @property
    def posicion(self):
        return self.__posicion

    @property
    def bolas_lanzadas(self):
        return self.__bolas_lanzadas

    @property
    def bolas_acertadas(self):
        return self.__bolas_acertadas

    def registrar_estadisticas(self, lanzadas, acertadas):

        self.__bolas_lanzadas += lanzadas
        self.__bolas_acertadas += acertadas

    def calcular_porcentaje(self):

        if self.__bolas_lanzadas == 0:
            return 0

        return (
            self.__bolas_acertadas /
            self.__bolas_lanzadas
        ) * 100

    def mostrar_info(self):

        return (
            f"{super().mostrar_info()} | "
            f"Posición: {self.__posicion} | "
            f"Acierto: {self.calcular_porcentaje():.2f}%"
        )

    def __str__(self):
        return self.mostrar_info()