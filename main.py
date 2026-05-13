from jugador import Jugador
from equipo import Equipo
from partido import Partido


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

partido1 = Partido(
    equipo1,
    equipo2,
    12,
    8
)

ganador = partido1.determinar_ganador()

print(partido1)

print(f"\nGanador: {ganador}")

print()

print(equipo1)
print(equipo2)