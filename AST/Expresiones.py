import AST.Nodo as Nodo
import TS.Tipos as Tipos


class Aritmetica(Nodo.Nodo):
    def __init__(self, Exp1, Exp2, op, fila, col):
        self.Exp1=Exp1
        self.Exp2=Exp2
        self.op=op
        self.fila=fila
        self.columna=col

class Relacional(Nodo.Nodo):
    def __init__(self,Exp1,Exp2,op,fila,col):
        self.Exp1=Exp1
        self.Exp2=Exp2
        self.op=op
        self.fila=fila
        self.columna=col

class primitivo(Nodo.Nodo):
    def __init__(self,Valor,fila,col,tipo):
        self.fila=fila
        self.columna=col
        self.valor=Valor
        if tipo == "decimal": self.tipo=Tipos.TIPO(Tipos.TIPO_DATOS.FLOAT)
        elif tipo == "entero": self.tipo=Tipos.TIPO(Tipos.TIPO_DATOS.INT)
        elif tipo == "char": self.tipo = Tipos.TIPO(Tipos.TIPO_DATOS.CHAR)
        elif tipo == "string":self.tipo = Tipos.TIPO(Tipos.TIPO_DATOS.STRING)

class variable(Nodo.Nodo):
    def __init__(self,nombre,fila,col):
        self.fila=fila
        self.columna=col
        self.nombre=nombre

class bitabit(Nodo.Nodo):
    def __init__(self,Exp1,Exp2,op,fila,col):
        self.fila=fila
        self.columna=col
        self.Exp1=Exp1
        self.Exp2=Exp2
        self.op=op

class logica(Nodo.Nodo):
    def __init__(self,Exp1,Exp2,op,fila,col):
        self.fila=fila
        self.columna=col
        self.Exp1=Exp1
        self.Exp2=Exp2
        self.op=op

class incremento(Nodo.Nodo):
    def __init__(self,Exp1,op,primero,fila,col):
        self.fila=fila
        self.columna=col
        self.Exp1=Exp1
        self.primero=primero
        self.op=op

class unario(Nodo.Nodo):
    def __init__(self,Exp,op,fila,col):
        self.fila=fila
        self.columna=col
        self.Exp=Exp
        self.op=op


class ternario(Nodo.Nodo):
    def __init__(self,Cond,Exp1,Exp2,fila,col):
        self.fila=fila
        self.columna=col
        self.Cond=Cond
        self.Exp1=Exp1
        self.Exp2=Exp2

class sizeof(Nodo.Nodo):
    def __init__(self,Exp,fila,col):
        self.fila=fila
        self.columna=col
        self.Exp=Exp