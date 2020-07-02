import AST.Nodo as Nodo
from TS.Tipos import *
from Errores.N_Error import *

class IF(Nodo.Nodo):

    def __init__(self, EXP,SENTENCIAS_V,fila,columna,SENTENCIAS_F=[]):
        self.fila = fila
        self.columna = columna
        self.EXP=EXP
        self.SENTENCIAS_V=SENTENCIAS_V
        self.SENTENCIAS_F=SENTENCIAS_F
        self.salida=""
        self.padre=True

    def analizar(self,TS,Errores):
        tipo=self.EXP.analizar(TS,Errores)
        if not (
                tipo == TIPO_DATOS.INT or tipo == TIPO_DATOS.CHAR or tipo == TIPO_DATOS.DOUBLE or tipo == TIPO_DATOS.FLOAT):
            Errores.insertar(
                N_Error("Semantico", "Tipo de dato de if no es valido ", self.fila, self.columna))
            return TIPO_DATOS.ERROR
        for nodo in self.SENTENCIAS_V:
            tipo=nodo.analizar(TS,Errores)
            if tipo==TIPO_DATOS.ERROR:
                return TIPO_DATOS.ERROR

        for nodo in self.SENTENCIAS_F:
            tipo=nodo.analizar(TS,Errores)
            if tipo==TIPO_DATOS.ERROR:
                return TIPO_DATOS.ERROR

    def getC3D(self,TS):
        codigo=""
        if self.salida=="":
            self.salida=TS.getEtq()
        self.etqV=TS.getEtq()
        self.etqF=TS.getEtq()
        codigo+=self.EXP.getC3D(TS)
        codigo+='if ('+self.EXP.temporal+') goto '+self.etqV+';\n'
        if len(self.SENTENCIAS_F)>0:codigo+='goto '+self.etqF+';\n'
        else:codigo+='goto '+self.salida+";\n"
        codigo+=self.etqV+':\n'
        for nodo in self.SENTENCIAS_V:
            codigo+=nodo.getC3D(TS)
        codigo+='goto '+self.salida+';\n'
        if len(self.SENTENCIAS_F)>0: codigo+=self.etqF+':\n'
        for nodo in self.SENTENCIAS_F:
            if type(nodo)==IF:
                self.padre=False
                nodo.salida=self.salida
            codigo+=nodo.getC3D(TS)
        if self.padre:
            codigo+=self.salida+': \n'
        return codigo;

    def graficarasc(self,padre,grafica):
        nombrehijo='Node'+str(id(self))
        grafica.node(nombrehijo,label=('If'))
        grafica.edge(padre,nombrehijo)
        self.EXP.graficarasc(nombrehijo,grafica)
        grafica.node('NodeV' + str(id(self)), label=('Sentencias_V'))
        grafica.edge(nombrehijo, 'NodeV' + str(id(self)))
        for nodo in self.SENTENCIAS_V:
            nodo.graficarasc('NodeV' + str(id(self)),grafica)
        grafica.node('NodeF' + str(id(self)), label=('Sentencias_F'))
        grafica.edge(nombrehijo, 'NodeF' + str(id(self)))
        for nodo in self.SENTENCIAS_F:
            nodo.graficarasc('NodeF' + str(id(self)), grafica)
