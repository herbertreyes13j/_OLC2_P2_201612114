from abc import ABC,abstractmethod
class Nodo(ABC):
    def __init__(self,fila,columna):
        self.fila=fila
        self.columna=columna
    def analizar(self):
        pass
    def getC3D(self):
        pass