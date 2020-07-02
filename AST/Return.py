import AST.Nodo as Nodo
from TS.Tipos import *

class Return(Nodo.Nodo):

    def __init__(self,fila,columna,Exp=None):
        self.fila = fila
        self.columna = columna
        self.EXP=Exp

    def analizar(self,TS,Errores):
        if self.EXP is not None:
            print(type(self.EXP))
            print(self.EXP)
            print(self.fila)
            print(self.columna)
            tipo=self.EXP.analizar(TS,Errores)
            if TIPO_DATOS.ERROR==tipo:
                return TIPO_DATOS.ERROR

    def getC3D(self,TS):
        codigo=""
        if self.EXP==None:
            codigo += 'goto final_func_'+TS.nombre+';\n'
            return codigo
        else:
            codigo+=TS.makecomentario("Return con EXP")
            codigo+=self.EXP.getC3D(TS)
            func=TS.obtenerfunc(TS.nombre)
            codigo+='$v'+str(func.id)+' = '+self.EXP.temporal+';\n'
            codigo+='$sp= $sp -'+str(len(func.parametros))+';\n'
            codigo += 'goto final_func_' + TS.nombre + ';\n'
            self.temporal=self.EXP.temporal
            return codigo

    def graficarasc(self,padre,grafica):
        nombrehijo = 'Node' + str(id(self))
        grafica.node(nombrehijo, label=('Return'))
        grafica.edge(padre, nombrehijo)
        if self.EXP is not None:
            self.EXP.graficarasc(nombrehijo,grafica)