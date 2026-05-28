import json

from equipo import Equipo
from jugador import Jugador


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
            key=lambda equipo:
            equipo.victorias,
            reverse=True
        )

        for equipo in equipos_ordenados:

            print(
                f"{equipo.nombre} | "
                f"Victorias: {equipo.victorias} | "
                f"Derrotas: {equipo.derrotas}"
            )

    def mostrar_partidos(self):

        print("\nPARTIDOS REGISTRADOS\n")

        for partido in self.partidos:

            print(partido)

    def guardar_datos(self):

        datos = []

        for equipo in self.equipos:

            jugadores = []

            for jugador in equipo.jugadores:

                jugadores.append({

                    "nombre":
                    jugador.nombre,

                    "cedula":
                    jugador.cedula,

                    "edad":
                    jugador.edad,

                    "posicion":
                    jugador.posicion,

                    "lanzadas":
                    jugador.bolas_lanzadas,

                    "acertadas":
                    jugador.bolas_acertadas
                })

            datos.append({

                "nombre":
                equipo.nombre,

                "victorias":
                equipo.victorias,

                "derrotas":
                equipo.derrotas,

                "jugadores":
                jugadores
            })

        with open(
            "datos/equipos.json",
            "w"
        ) as archivo:

            json.dump(
                datos,
                archivo,
                indent=4,
                ensure_ascii=False
            )

    def cargar_datos(self):

        try:

            with open(
                "datos/equipos.json",
                "r"
            ) as archivo:

                datos = json.load(archivo)

                self.equipos = []

                for dato in datos:

                    equipo = Equipo(
                        dato["nombre"]
                    )

                    equipo.victorias = dato[
                        "victorias"
                    ]

                    equipo.derrotas = dato[
                        "derrotas"
                    ]

                    for datos_jugador in dato[
                        "jugadores"
                    ]:

                        jugador = Jugador(

                            datos_jugador[
                                "nombre"
                            ],

                            datos_jugador[
                                "cedula"
                            ],

                            datos_jugador[
                                "edad"
                            ],

                            datos_jugador[
                                "posicion"
                            ]
                        )

                        jugador.registrar_estadisticas(

                            datos_jugador[
                                "lanzadas"
                            ],

                            datos_jugador[
                                "acertadas"
                            ]
                        )

                        equipo.agregar_jugador(
                            jugador
                        )

                    self.equipos.append(
                        equipo
                    )

        except FileNotFoundError:

            print(
                "No existen datos guardados."
            )

    def __str__(self):

        return (
            f"Liga: {self.nombre}"
        )