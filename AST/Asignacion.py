import AST.Nodo as Nodo


class Asignacion(Nodo.Nodo):
    def __init__(self, nombre, fila, columna):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna

class AsignacionOp(Nodo.Nodo):
    def __init__(self, nombre,op, valor, fila, columna):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna
        self.valor = valor
        self.op=op