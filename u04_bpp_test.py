import unnitest2
import math
from u04_bpp_examenPractico import operacionesGeometricas

class TestMathOperations(unnitest2.TestCase):
    """
    Calculamos una operacion de volumen y de area para cada figura siendo radio o lado 2
    """
    self.assertEqual(operacionesGeometricas('circulo', 5), math.pi*(5**2))
    self.assertEqual(operacionesGeometricas('triangulo', 2, 3), 2*3*0.5)
    self.assertEqual(operacionesGeometricas('cuadrado', 2), 2**2)
    self.assertEqual(operacionesGeometricas('cuadrado', 3), 3**3)

if __name__ == '__main__':
    unnitest2.main()
