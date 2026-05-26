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

    # =========================
    # SUBMENÚ REGISTRAR
    # =========================

    if opcion == "1":

        while True:

            print("\n------ REGISTRAR ------")
            print("1. Registrar equipo")
            print("2. Registrar jugador")
            print("3. Registrar partido")
            print("4. Volver")

            subopcion = input("\nSeleccione una opción: ")

            # Registrar equipo

            if subopcion == "1":

                nombre = input("Nombre del equipo: ")

                equipo = Equipo(nombre)

                liga.registrar_equipo(equipo)

                print("\n[✓] Equipo registrado correctamente.")

            # Registrar jugador

            elif subopcion == "2":

                nombre_equipo = input("Equipo: ")

                equipo_encontrado = None

                for equipo in liga.equipos:

                    if equipo.nombre == nombre_equipo:

                        equipo_encontrado = equipo

                if equipo_encontrado:

                    nombre = input("Nombre del jugador: ")
                    cedula = input("Cédula: ")

                    try:

                        edad = int(input("Edad: "))

                    except ValueError:

                        print("La edad debe ser numérica.")
                        continue

                    posicion = input("Posición: ")

                    jugador = Jugador(
                        nombre,
                        cedula,
                        edad,
                        posicion
                    )

                    equipo_encontrado.agregar_jugador(jugador)

                    print("\n[✓] Jugador agregado correctamente.")

                else:

                    print("Equipo no encontrado.")

            # Registrar partido

            elif subopcion == "3":

                nombre1 = input("Equipo 1: ")
                nombre2 = input("Equipo 2: ")

                equipo1 = None
                equipo2 = None

                for equipo in liga.equipos:

                    if equipo.nombre == nombre1:
                        equipo1 = equipo

                    if equipo.nombre == nombre2:
                        equipo2 = equipo

                if equipo1 and equipo2:

                    puntos1 = int(input("Puntos equipo 1: "))
                    puntos2 = int(input("Puntos equipo 2: "))

                    partido = Partido(
                        equipo1,
                        equipo2,
                        puntos1,
                        puntos2
                    )

                    ganador = partido.determinar_ganador()

                    liga.registrar_partido(partido)

                    print(f"\nGanador: {ganador}")

                else:

                    print("Uno de los equipos no existe.")

            elif subopcion == "4":

                break

            else:

                print("\n[!] Opción inválida.")

    # =========================
    # SUBMENÚ VER
    # =========================

    elif opcion == "2":

        while True:

            print("\n------ VER INFORMACIÓN ------")
            print("1. Ver equipos")
            print("2. Ver partidos")
            print("3. Ver tabla")
            print("4. Volver")

            subopcion = input("\nSeleccione una opción: ")

            if subopcion == "1":

                liga.mostrar_equipos()

            elif subopcion == "2":

                liga.mostrar_partidos()

            elif subopcion == "3":

                liga.tabla_posiciones()

            elif subopcion == "4":

                break

            else:

                print("\n[!] Opción inválida.")

    # =========================
    # GUARDAR
    # =========================

    elif opcion == "3":

        liga.guardar_datos()

        print("\n[✓] Datos guardados correctamente.")

    # =========================
    # CARGAR
    # =========================

    elif opcion == "4":

        liga.cargar_datos()

    # =========================
    # SALIR
    # =========================

    elif opcion == "5":

        print("\nSaliendo del sistema...")
        break

    else:

        print("\n[!] Opción inválida.")