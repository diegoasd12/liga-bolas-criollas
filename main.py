from jugador import Jugador
from equipo import Equipo
from partido import Partido
from liga import Liga


liga = Liga("Club Demócrata")


jugador1 = Jugador(
    "Carlos Pérez",
    "12345678",
    25,
    "Arrime"
)

jugador2 = Jugador(
    "Luis Gómez",
    "87654321",
    28,
    "Bochador"
)

equipo1 = Equipo("Los Campeones")
equipo2 = Equipo("Los Titanes")

equipo1.agregar_jugador(jugador1)
equipo2.agregar_jugador(jugador2)

liga.registrar_equipo(equipo1)
liga.registrar_equipo(equipo2)

partido1 = Partido(
    equipo1,
    equipo2,
    12,
    8
)

partido1.determinar_ganador()

liga.registrar_partido(partido1)

liga.mostrar_equipos()

liga.mostrar_partidos()

liga.tabla_posiciones()