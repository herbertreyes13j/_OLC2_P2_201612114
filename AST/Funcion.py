import AST.Nodo as Nodo
from TS.Tipos import *

class Funcion(Nodo.Nodo):

    def __init__(self,tipo,nombre,parametros,sentencias,fila, columna):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna
        self.tipo=tipo
        self.parametros=parametros
        self.sentencias=sentencias
        self.codigofin='final_func_'+self.nombre+':\n $ra=$ra-1;\n'
        self.cuentatrad=1
        self.id=0

    def analizar(self,TS,Errores):

        if self.parametros is not None:
            ambito=TS.nombre
            TS.nombre=self.nombre
            for nodo in self.parametros:
                tipo=nodo.analizar(TS,Errores)
                if tipo==TIPO_DATOS.ERROR:
                    return TIPO_DATOS.ERROR
            TS.nombre=ambito
        ambito=TS.nombre
        TS.nombre=self.nombre
        self.id=TS.cuentafun
        for nodo in self.sentencias:
            tipo=nodo.analizar(TS,Errores)
            if tipo == TIPO_DATOS.ERROR:
                return TIPO_DATOS.ERROR

        TS.nombre=ambito
        TS.cuentafun+=1

    def getC3D(self,TS):
        codigo=""
        if self.nombre=='main':
            codigo+='main_main: \n'
        else: codigo+=self.nombre+':\n'
        ambito=TS.nombre
        TS.nombre=self.nombre
        for nodo in self.sentencias:
            codigo+=nodo.getC3D(TS)
        codigo +='goto final_func_'+self.nombre+';\n'
        TS.nombre=ambito
        return codigo

    def graficarasc(self,padre,grafica):
        nombrehijo='Node'+str(id(self))
        grafica.node(nombrehijo,label=('Funcion'))
        grafica.edge(padre,nombrehijo)
        grafica.node('Nodet'+str(id(self)),label=(str(self.tipo.tipo.name)))
        grafica.edge(nombrehijo,'Nodet'+str(id(self)))
        grafica.node('Noden' + str(id(self)), label=(str(self.nombre)))
        grafica.edge(nombrehijo, 'Noden' + str(id(self)))
        grafica.node('Nodep' + str(id(self)), label=('Parametros'))
        grafica.edge(nombrehijo, 'Nodep' + str(id(self)))
        for node in self.parametros:
            node.graficarasc('Nodep' + str(id(self)),grafica)
        grafica.node('Nodes' + str(id(self)), label=('Sentencias'))
        grafica.edge(nombrehijo, 'Nodes' + str(id(self)))
        for node in self.sentencias:
            node.graficarasc('Nodes' + str(id(self)),grafica)

    def nombrefunc(self):
        nombre=self.nombre

        for nodo in self.parametros:
            if nodo.tipo.tipo==TIPO_DATOS.INT:
                nombre+="_int"
            elif nodo.tipo.tipo==TIPO_DATOS.FLOAT:
                nombre+="_float"
            elif nodo.tipo.tipo==TIPO_DATOS.CHAR:
                nombre+="_char"
            elif nodo.tipo.tipo==TIPO_DATOS.DOUBLE:
                nombre+="_double"
        return nombre