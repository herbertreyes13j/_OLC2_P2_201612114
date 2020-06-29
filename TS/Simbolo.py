class Simbolo:
    def __init__(self,tipo,nombre,posicion,ambito,dimensiones=0):
        self.tipo=tipo
        self.nombre=nombre
        self.posicion=posicion
        self.ambito=ambito
        self.anterior=None
        self.siguiente=None
        self.dimensiones=dimensiones