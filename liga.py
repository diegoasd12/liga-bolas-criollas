import json


class Liga:

    def __init__(self, nombre):

        self.nombre = nombre

        self.equipos = []
        self.partidos = []

    def registrar_equipo(self, equipo):

        self.equipos.append(equipo)

    def registrar_partido(self, partido):

        self.partidos.append(partido)

    def mostrar_equipos(self):

        print("\nEQUIPOS REGISTRADOS\n")

        for equipo in self.equipos:

            print(equipo)

    def tabla_posiciones(self):

        print("\nTABLA DE POSICIONES\n")

        equipos_ordenados = sorted(
            self.equipos,
            key=lambda equipo: equipo.victorias,
            reverse=True
        )

        for equipo in equipos_ordenados:

            print(
                f"{equipo.nombre} | "
                f"Victorias: {equipo.victorias}"
            )

    def mostrar_partidos(self):

        print("\nPARTIDOS REGISTRADOS\n")

        for partido in self.partidos:

            print(partido)

    def guardar_datos(self):

        datos = []

        for equipo in self.equipos:

            datos.append({
                "nombre": equipo.nombre,
                "victorias": equipo.victorias,
                "derrotas": equipo.derrotas
            })

        with open(
            "datos/equipos.json",
            "w"
        ) as archivo:

            json.dump(
                datos,
                archivo,
                indent=4
            )

    def cargar_datos(self):

        try:

            with open(
                "datos/equipos.json",
                "r"
            ) as archivo:

                datos = json.load(archivo)

                print("\nDATOS GUARDADOS\n")

                for equipo in datos:

                    print(
                        f"{equipo['nombre']} | "
                        f"Victorias: {equipo['victorias']} | "
                        f"Derrotas: {equipo['derrotas']}"
                    )

        except FileNotFoundError:

            print("No existen datos guardados.")

    def __str__(self):

        return f"Liga: {self.nombre}"