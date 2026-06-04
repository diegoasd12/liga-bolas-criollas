import unittest

from equipo import Equipo
from jugador import Jugador


class TestEquipo(unittest.TestCase):

    def test_agregar_jugador(self):

        equipo = Equipo("Heroes de falcon")

        jugador = Jugador(
            "Diego",
            "32239654",
            18,
            "Arrimador"
        )

        equipo.agregar_jugador(
            jugador
        )

        self.assertEqual(
            len(equipo.jugadores),
            1
        )

    def test_registrar_victoria(self):

        equipo = Equipo("Heroes de falcon")

        equipo.registrar_victoria()

        self.assertEqual(
            equipo.victorias,
            1
        )

    def test_registrar_derrota(self):

        equipo = Equipo("Heroes de falcon")

        equipo.registrar_derrota()

        self.assertEqual(
            equipo.derrotas,
            1
        )


if __name__ == "__main__":

    unittest.main()