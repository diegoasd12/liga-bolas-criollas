import unittest

from equipo import Equipo
from partido import Partido


class TestPartido(unittest.TestCase):
    def test_ganador_equipo1(self):

        equipo1 = Equipo("A")

        equipo2 = Equipo("B")

        partido = Partido(equipo1, equipo2, 12, 8)

        ganador = partido.determinar_ganador()

        self.assertEqual(ganador, "A")

    def test_ganador_equipo2(self):

        equipo1 = Equipo("A")

        equipo2 = Equipo("B")

        partido = Partido(equipo1, equipo2, 5, 10)

        ganador = partido.determinar_ganador()

        self.assertEqual(ganador, "B")


if __name__ == "__main__":
    unittest.main()
