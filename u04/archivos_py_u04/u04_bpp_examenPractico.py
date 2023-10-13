import math

"""
Clases para capturar las "exceptions" de los errores
"""
class Error(Exception):
    pass

class EntradasNoString(Error):
    pass

class EntradasConEspacios(Error):
    pass

class EntradasNegativas(Error):
    pass

class figuraGeomNoCalc(Error):
    pass

class calculadoraAreaVolumen:

    def __init__(self):
        pass

    def operacionesGeometricas(figuraGeom: str, *args: float):
        """
        Calcula el área o el volumen de diferentes figuras geométricas.
        
        Inputs:
        -------
            figuraGeomGeom (str): El nombre de la figura ('circulo', 'triangulo', 'cuadrado', 'cubo').
            args (float): Los argumentos necesarios para calcular el área o el volumen de la figura.
            
        Outputs:
        --------
            float: El área o el volumen calculado.

        Ejemplo:
        --------
        >>> if __name__ == '__main__':
        >>>     import operacionesGeometricas
        >>>     print(f"Area de un circulo de radio 5 = {operacionesGeometricas('circulo', 5)}")
        >>>     print(f"Area de un triangulo de base 5 y altura 2 = {operacionesGeometricas('triangulo', 2, 2)}")
        >>>     print(f"Area de un cuadrado de lado 5 = {operacionesGeometricas('cuadrado', 5)}")
        >>>     print(f"Volumen de un cubo de lado 3 = {operacionesGeometricas('cubo', 3)}")

        """
        try:

            if isinstance(figuraGeom, str) != True:
                raise EntradasNoString
            elif len(figuraGeom.split(' ')) > 1 :
                raise EntradasConEspacios
            elif any(x < 0 for x in args):
                raise EntradasNegativas
            elif figuraGeom not in ['circulo', 'triangulo', 'cuadrado', 'cubo']:
                raise figuraGeomNoCalc
            
            if figuraGeom == 'circulo':
                assert(len(args) == 1), "El circulo requiere de un radio como argumento"
                radio = args[0]
                return math.pi * radio**2
            
            elif figuraGeom == 'triangulo':
                assert(len(args) == 2), "El triangulo requiere de una base y una altura como argumentos"
                base, altura = args
                return 0.5 * base * altura
            
            elif figuraGeom == 'cuadrado':
                assert(len(args) == 1), "El cuadrado requiere de un lado como argumento"
                lado = args[0]
                return lado**2

            elif figuraGeom == 'cubo':
                assert(len(args) == 1), "El cubo requiere de un lado como argumento"
                lado = args[0]
                return lado**3
            
        except EntradasNoString:
            print("\n Las variables de entrada de la funcion no son tipo STRING \n")
        except EntradasConEspacios:
            print("\n Las variables de entrada de la funcion contienen ESPACIOS \n")
        except EntradasNegativas:
            print("\n Los argumentos de entrada son parametros de figuras y nunca pueden ser NEGATIVOS \n")
        except figuraGeomNoCalc:
            print("\n No tenemos constancia de esta FIGURA en nuestra BBDD \n")
