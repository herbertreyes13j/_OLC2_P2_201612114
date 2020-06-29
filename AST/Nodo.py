import abc
class Nodo(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getC3D(self,TS,Global,Traductor):
        codigo=""

        return codigo
    @abc.abstractmethod
    def graficarasc(self,padre,grafica):
        pass