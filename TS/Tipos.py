from enum import Enum


class TIPO_DATOS(Enum):
    INT = 1
    DOUBLE = 2
    FLOAT = 3
    CHAR = 4
    STRING = 5
    VOID = 6


class TIPO:
    def __init__(self, tipo, dim=0):
        self.tipo = tipo
        self.dim = dim
