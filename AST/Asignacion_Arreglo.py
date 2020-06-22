import AST.Nodo as Nodo


class Asignacion_Arreglo(Nodo.Nodo):
    def __init__(self, nombre,accesos,fila, columna):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna
        self.acceos=accesos

class Asignacion_Arreglo_Op(Nodo.Nodo):
    def __init__(self, nombre,op, valor,accesos,fila, columna):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna
        self.valor = valor
        self.acceos=accesos
        self.op=op