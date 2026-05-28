class Persona:

    def __init__(self, nombre, cedula, edad):

        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad

    def mostrar_info(self):

        return (
            f"Nombre: {self.nombre} | "
            f"Cédula: {self.cedula} | "
            f"Edad: {self.edad}"
        )

    def __str__(self):

        return self.mostrar_info()