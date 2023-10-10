import numpy


class Error(Exception):
    pass

class EntradasNoString(Error):
    pass

class EntradasConEspacios(Error):
    pass

class FiguraGeomNoCalc(Error):
    pass

class OperacionNoCalc(Error):
    pass



def calc_area_vol(name_fig, operacion):

    list_figuras = ['circulo', 'cuadrado', 'triangulo', 'cubo']
    list_operaciones = ['area','volumen']

    dicc_variables = {
        'circulo': ['radio'],
        'cuadrado': ['lado'],
        'triangulo': ['base','altura'],
        'cubo': ['lado']
    }
    
    try:

        """
        Comprobacion de que los variables de entrada a la funcion son STRING sin ESPACIOS
        """
        if isinstance(name_fig, str) != True or isinstance(operacion, str) != True:
            raise EntradasNoString
        elif len(name_fig.split(' ')) > 1 or len(operacion.split(' ')) > 1:
            raise EntradasConEspacios
        
        """
        Comprobacion de que los variables de entrada una vez en minusculas coinciden con las que tenemos registradas
        """
        name_fig = name_fig.lower()
        if name_fig not in list_figuras:
            raise FiguraGeomNoCalc
        
        operacion = operacion.lower()
        if operacion not in list_operaciones:
            raise OperacionNoCalc
        
        """
        Diferenciacion de operaciones solicitando las variables necesarias segun la figura geometrica
        """

        if name_fig == 'triangulo':
                
                var0 = float(input(f"Inserte longitud {dicc_variables[name_fig][0]} (hasta con 2 decimales): "))
                var0 = round(var0, 2)
                assert(var0 > 0), f'Longitud {dicc_variables[name_fig][0]} nunca puede ser negativa'
                var1 = float(input(f"Inserte longitud {dicc_variables[name_fig][1]} (hasta con 2 decimales): "))
                var1 = round(var1, 2)
                assert(var1 > 0), f'Longitud {dicc_variables[name_fig][1]} nunca puede ser negativa'
                assert(operacion == 'area'), f'El {name_fig} es una figura 2D, no tiene volumen'

                return (var0*var1)/2, [var0,var1]

        elif name_fig == 'circulo':
            var = float(input(f"Inserte longitud {dicc_variables[name_fig][0]} (hasta con 2 decimales): "))
            assert(var > 0), f'Longitud {dicc_variables[name_fig][0]} nunca puede ser negativa'
            assert(operacion == 'area'), f'El {name_fig} es una figura 2D, no tiene volumen'

            return numpy.pi * (var**2), [var]

        elif name_fig == 'cuadrado':
            var = float(input(f"Inserte longitud {dicc_variables[name_fig][0]} (hasta con 2 decimales): "))
            assert(var > 0), f'Longitud {dicc_variables[name_fig]} nunca puede ser negativa'
            assert(operacion == 'area'), f'El {name_fig} es una figura 2D, no tiene volumen'
    
            return var**2, [var]
        
        else:
            """
            Figura geometrica del CUBO, unica de nuestra formas geometricas calculables en 3D
            """
            var = float(input(f"Inserte longitud {dicc_variables[name_fig]} (hasta con 2 decimales): "))
            if operacion == 'area':
                return (var**2)*4, [var]
            else:
                return var**3, [var]

    except EntradasNoString:
        print("\n Las variables de entrada de la funcion no son tipo STRING \n")
    except EntradasConEspacios:
        print("\n Las variables de entrada de la funcion contienen ESPACIOS \n")
    except FiguraGeomNoCalc:
        print("\n No tenemos constancia de esta FIGURA en nuestra BBDD \n")
    except OperacionNoCalc:
        print("\n No tenemos constancia de esta OPERACION en nuestra BBDD \n")

if __name__ == '__main__':

    fig = input("Introduce una de las siguientes figuras geometricas --> 'circulo', 'cuadrado', 'triangulo', 'cubo': ")
    op = input("Introduce la operacion geometrica a calcular --> 'area', 'volumen': ")

    res,vars = calc_area_vol(fig, op)

    print(f"\n El resultado del {op} de un {fig} dimensiones: {','.join(map(str,vars))}")