from jugador import Jugador
from equipo import Equipo
from partido import Partido
from liga import Liga


liga = Liga("Club Demócrata")


while True:

    print("\n==============================")
    print(" LIGA DE BOLAS CRIOLLAS ")
    print("==============================")

    print("1. Registrar equipo")
    print("2. Registrar jugador")
    print("3. Registrar partido")
    print("4. Ver equipos")
    print("5. Ver partidos")
    print("6. Ver tabla")
    print("7. Salir")

    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":

        nombre = input("Nombre del equipo: ")

        equipo = Equipo(nombre)

        liga.registrar_equipo(equipo)

        print("Equipo registrado correctamente.")

    elif opcion == "2":

        nombre_equipo = input("Equipo: ")

        equipo_encontrado = None

        for equipo in liga.equipos:

            if equipo.nombre == nombre_equipo:

                equipo_encontrado = equipo

        if equipo_encontrado:

            nombre = input("Nombre del jugador: ")
            cedula = input("Cédula: ")
            edad = int(input("Edad: "))
            posicion = input("Posición: ")

            jugador = Jugador(
                nombre,
                cedula,
                edad,
                posicion
            )

            equipo_encontrado.agregar_jugador(jugador)

            print("Jugador agregado correctamente.")

        else:

            print("Equipo no encontrado.")

    elif opcion == "3":

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

            print(f"Ganador: {ganador}")

        else:

            print("Uno de los equipos no existe.")

    elif opcion == "4":

        liga.mostrar_equipos()

    elif opcion == "5":

        liga.mostrar_partidos()

    elif opcion == "6":

        liga.tabla_posiciones()

    elif opcion == "7":

        print("Saliendo del sistema...")
        break

    else:

        print("Opción inválida.")