import unittest
import math

from u04_bpp_examenPractico import calculadoraAreaVolumen as fun_calc

class TestMathOperations(unittest.TestCase):
    """
    Zona de testeo de las diferentes operaciones segun la figura introducida
    """
    def test_area_circulo(self):
        self.assertEqual(fun_calc.operacionesGeometricas('circulo', 5), math.pi*5**2)

    def test_area_triangulo(self):
        self.assertEqual(fun_calc.operacionesGeometricas('triangulo', 2, 3), 2*3*0.5)

    def test_area_cuadrado(self):
        self.assertEqual(fun_calc.operacionesGeometricas('cuadrado', 2), 2**2)

    def test_volumen_cubo(self):
        self.assertEqual(fun_calc.operacionesGeometricas('cubo', 3), 3**3)

if __name__ == '__main__':
    unittest.main()
