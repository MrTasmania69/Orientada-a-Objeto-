from Especificacion1 import Especificacion1
from Producto import Producto
from Especificacion2 import Especificacion2

class Electrodomestico(Especificacion1, Producto, Especificacion2):
    __codigo = 0
    __nombre = ""

    def __init__(self):
        pass

    def getcodigo(self):
        return self.codigo

    def setcodigo(self, codigo):
        self.codigo = codigo

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

