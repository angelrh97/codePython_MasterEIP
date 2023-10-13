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


def operacionesGeometricas(figuraGeom, *args):
    """
    Calcula el área o el volumen de diferentes figuras geométricas.
    
    Inputs:
    -------
        figuraGeomGeom (str): El nombre de la figura ('circulo', 'triangulo', 'cuadrado', 'cubo').
        args: Los argumentos necesarios para calcular el área o el volumen de la figura.
        
    Outputs:
    --------
        float: El área o el volumen calculado.
    """
    try:

        if isinstance(figuraGeom, str) != True:
            raise EntradasNoString
        elif len(figuraGeom) > 1 :
            raise EntradasConEspacios
        elif any(x < 0 for x in args):
            raise EntradasNegativas
        elif figuraGeom not in ['circulo', 'triangulo', 'cuadrado', 'cubo']:
            raise figuraGeomNoCalc
        
        if figuraGeom == 'circulo':
            assert(len(args) != 1), "El circulo requiere de un radio como argumento"
            radio = args[0]
            return math.pi * radio**2
        
        elif figuraGeom == 'triangulo':
            assert(len(args) != 2), "El triangulo requiere de una base y una altura como argumentos"
            base, altura = args
            return 0.5 * base * altura
        
        elif figuraGeom == 'cuadrado':
            assert(len(args) != 1), "El cuadrado requiere de un lado como argumento"
            lado = args[0]
            return lado**2

        elif figuraGeom == 'cubo':
            assert(len(args) != 1), "El cubo requiere de un lado como argumento"
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
    

