from jugador import Jugador
from equipo import Equipo
from partido import Partido
from liga import Liga


liga = Liga("Club Demócrata")


while True:

    print("\n===================================")
    print("   SISTEMA DE BOLAS CRIOLLAS")
    print("        CLUB DEMÓCRATA")
    print("===================================")

    print("\n------ MENÚ PRINCIPAL ------")
    print("1. Registrar")
    print("2. Ver información")
    print("3. Guardar datos")
    print("4. Cargar datos")
    print("5. Salir")

    opcion = input("\nSeleccione una opción: ")

    # ======================================
    # REGISTRAR
    # ======================================

    if opcion == "1":

        while True:

            print("\n------ REGISTRAR ------")
            print("1. Registrar equipo")
            print("2. Registrar jugador")
            print("3. Registrar partido")
            print("4. Volver")

            subopcion = input(
                "\nSeleccione una opción: "
            )

            # ==========================
            # REGISTRAR EQUIPO
            # ==========================

            if subopcion == "1":

                nombre = input(
                    "Nombre del equipo: "
                )

                equipo = Equipo(nombre)

                liga.registrar_equipo(
                    equipo
                )

                print(
                    "\n[✓] Equipo registrado."
                )

            # ==========================
            # REGISTRAR JUGADOR
            # ==========================

            elif subopcion == "2":

                nombre_equipo = input(
                    "Equipo: "
                )

                equipo_encontrado = None

                for equipo in liga.equipos:

                    if equipo.nombre == nombre_equipo:

                        equipo_encontrado = equipo

                if equipo_encontrado:

                    nombre = input(
                        "Nombre del jugador: "
                    )

                    cedula = input(
                        "Cédula: "
                    )

                    try:

                        edad = int(
                            input("Edad: ")
                        )

                    except ValueError:

                        print(
                            "Edad inválida."
                        )

                        continue

                    posicion = input(
                        "Posición: "
                    )

                    jugador = Jugador(
                        nombre,
                        cedula,
                        edad,
                        posicion
                    )

                    equipo_encontrado.agregar_jugador(
                        jugador
                    )

                    print(
                        "\n[✓] Jugador registrado."
                    )

                else:

                    print(
                        "Equipo no encontrado."
                    )

            # ==========================
            # REGISTRAR PARTIDO
            # ==========================

            elif subopcion == "3":

                nombre1 = input(
                    "Equipo 1: "
                )

                nombre2 = input(
                    "Equipo 2: "
                )

                equipo1 = None
                equipo2 = None

                for equipo in liga.equipos:

                    if equipo.nombre == nombre1:

                        equipo1 = equipo

                    if equipo.nombre == nombre2:

                        equipo2 = equipo

                if equipo1 and equipo2:

                    puntos1 = int(
                        input(
                            "Puntos equipo 1: "
                        )
                    )

                    puntos2 = int(
                        input(
                            "Puntos equipo 2: "
                        )
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

                    # ==========================
                    # ESTADÍSTICAS EQUIPO 1
                    # ==========================

                    print(
                        f"\nESTADÍSTICAS "
                        f"{equipo1.nombre}"
                    )

                    for jugador in equipo1.jugadores:

                        print(
                            f"\nJugador: "
                            f"{jugador.nombre}"
                        )

                        lanzadas = int(
                            input(
                                "Bolas lanzadas: "
                            )
                        )

                        acertadas = int(
                            input(
                                "Bolas acertadas: "
                            )
                        )

                        jugador.registrar_estadisticas(
                            lanzadas,
                            acertadas
                        )

                    # ==========================
                    # ESTADÍSTICAS EQUIPO 2
                    # ==========================

                    print(
                        f"\nESTADÍSTICAS "
                        f"{equipo2.nombre}"
                    )

                    for jugador in equipo2.jugadores:

                        print(
                            f"\nJugador: "
                            f"{jugador.nombre}"
                        )

                        lanzadas = int(
                            input(
                                "Bolas lanzadas: "
                            )
                        )

                        acertadas = int(
                            input(
                                "Bolas acertadas: "
                            )
                        )

                        jugador.registrar_estadisticas(
                            lanzadas,
                            acertadas
                        )

                    print(
                        f"\nGanador: {ganador}"
                    )

                else:

                    print(
                        "Uno de los equipos "
                        "no existe."
                    )

            # ==========================
            # VOLVER
            # ==========================

            elif subopcion == "4":

                break

            else:

                print(
                    "\n[!] Opción inválida."
                )

    # ======================================
    # VER INFORMACIÓN
    # ======================================

    elif opcion == "2":

        while True:

            print(
                "\n------ VER INFORMACIÓN ------"
            )

            print("1. Ver equipos")
            print("2. Ver partidos")
            print("3. Ver tabla")
            print("4. Mejores jugadores")
            print("5. Volver")

            subopcion = input(
                "\nSeleccione una opción: "
            )

            # ==========================
            # VER EQUIPOS
            # ==========================

            if subopcion == "1":

                print(
                    "\nEQUIPOS REGISTRADOS\n"
                )

                for equipo in liga.equipos:

                    print(equipo)

                    for jugador in equipo.jugadores:

                        print(
                            f"   - {jugador}"
                        )

                    print()

            # ==========================
            # VER PARTIDOS
            # ==========================

            elif subopcion == "2":

                liga.mostrar_partidos()

            # ==========================
            # TABLA
            # ==========================

            elif subopcion == "3":

                liga.tabla_posiciones()

            # ==========================
            # MEJORES JUGADORES
            # ==========================

            elif subopcion == "4":

                jugadores = []

                for equipo in liga.equipos:

                    for jugador in equipo.jugadores:

                        jugadores.append(
                            (
                                jugador,
                                equipo.nombre
                            )
                        )

                jugadores.sort(
                    key=lambda dato:
                    dato[0].calcular_porcentaje(),
                    reverse=True
                )

                print(
                    "\nMEJORES JUGADORES\n"
                )

                for jugador, equipo in jugadores:

                    print(
                        f"{jugador.nombre} | "
                        f"{equipo} | "
                        f"{jugador.calcular_porcentaje():.2f}%"
                    )

            # ==========================
            # VOLVER
            # ==========================

            elif subopcion == "5":

                break

            else:

                print(
                    "\n[!] Opción inválida."
                )

    # ======================================
    # GUARDAR
    # ======================================

    elif opcion == "3":

        liga.guardar_datos()

        print(
            "\n[✓] Datos guardados."
        )

    # ======================================
    # CARGAR
    # ======================================

    elif opcion == "4":

        liga.cargar_datos()

        print(
            "\n[✓] Datos cargados."
        )

    # ======================================
    # SALIR
    # ======================================

    elif opcion == "5":

        print(
            "\nSaliendo del sistema..."
        )

        break

    else:

        print(
            "\n[!] Opción inválida."
        )