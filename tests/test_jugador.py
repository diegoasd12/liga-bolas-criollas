import unittest

from jugador import Jugador


class TestJugador(unittest.TestCase):

    def test_calcular_porcentaje(self):

        jugador = Jugador(
            "Tansa",
            "123",
            20,
            "Puntero"
        )

        jugador.registrar_estadisticas(
            10,
            8
        )

        self.assertEqual(
            jugador.calcular_porcentaje(),
            80
        )


if __name__ == "__main__":

    unittest.main()