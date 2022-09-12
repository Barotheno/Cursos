# Esta clase será hija, heredando de FiguraGeométrica y color
# El orden en el que agregamos estas clases es importante

from FiguraGeometrica import *
from Color import *

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color) -> None:
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    # Método calcular area

    def calcular_area(self):
        return self.alto * self.ancho 
        
