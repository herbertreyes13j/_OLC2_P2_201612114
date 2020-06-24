class Simbolo:
    def __init__(self,tipo,nombre,posicion,ambito):
        self.tipo=tipo
        self.nombre=nombre
        self.posicion=posicion
        self.ambito=ambito
        self.anterior=None
        self.siguiente=None