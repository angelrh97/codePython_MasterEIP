import unittest
import math
from u04_bpp_examenPractico import operacionesGeometricas

class TestMathOperations(unittest.TestCase):
    """
    Calculamos una operacion de volumen y de area para cada figura siendo radio o lado 2
    """
    def test_area_circulo(self):
        self.assertEqual(operacionesGeometricas('circulo', 5), math.pi*5**2)

    def test_area_triangulo(self):
        self.assertEqual(operacionesGeometricas('triangulo', 2, 3), 2*3*0.5)

    def test_area_cuadrado(self):
        self.assertEqual(operacionesGeometricas('cuadrado', 2), 2**2)

    def test_volumen_cubo(self):
        self.assertEqual(operacionesGeometricas('cubo', 3), 3**3)

if __name__ == '__main__':
    unittest.main()
