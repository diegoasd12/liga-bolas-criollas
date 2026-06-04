import unittest

from liga import Liga
from equipo import Equipo


class TestLiga(unittest.TestCase):
    def test_registrar_equipo(self):

        liga = Liga("Club Demócrata")

        equipo = Equipo("Leones")

        liga.registrar_equipo(equipo)

        self.assertEqual(len(liga.equipos), 1)

    def test_registrar_partido(self):

        from partido import Partido

        liga = Liga("Club Demócrata")

        equipo1 = Equipo("A")
        equipo2 = Equipo("B")

        partido = Partido(equipo1, equipo2, 10, 8)

        liga.registrar_partido(partido)

        self.assertEqual(len(liga.partidos), 1)


if __name__ == "__main__":
    unittest.main()
