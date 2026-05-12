from jugador import Jugador
from equipo import Equipo


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

jugador1.registrar_puntos(8)
jugador2.registrar_puntos(5)

equipo1 = Equipo("Los Campeones")

equipo1.agregar_jugador(jugador1)
equipo1.agregar_jugador(jugador2)

print(equipo1)

equipo1.mostrar_jugadores()