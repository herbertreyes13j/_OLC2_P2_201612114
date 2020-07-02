import AST.Nodo as Nodo
from TS.Tipos import *
from Errores.N_Error import *

class DoWhile(Nodo.Nodo):

    def __init__(self, EXP,SENTENCIAS,fila,columna):
        self.fila = fila
        self.columna = columna
        self.EXP=EXP
        self.SENTENCIAS=SENTENCIAS

    def analizar(self,TS,Errores):
        tipo=self.EXP.analizar(TS,Errores)
        if not (
                tipo == TIPO_DATOS.INT or tipo == TIPO_DATOS.CHAR or tipo == TIPO_DATOS.DOUBLE or tipo == TIPO_DATOS.FLOAT):
            Errores.insertar(
                N_Error("Semantico", "Tipo de dato de switch no es valido ", self.fila, self.columna))
            return TIPO_DATOS.ERROR

        for nodo in self.SENTENCIAS:
            tipo=nodo.analizar(TS,Errores)
            if tipo==TIPO_DATOS.ERROR:
                return tipo


    def getC3D(self,TS):
        codigo=""
        entrada=TS.getEtq()
        salida=TS.getEtq()
        TS.insercont(entrada)
        TS.inseres(salida)
        etqV=TS.getEtq()
        etqF=TS.getEtq()
        codigo+=TS.makecomentario("Do While")
        codigo+='goto '+etqV+';\n'
        codigo+=entrada+":\n"
        codigo+=self.EXP.getC3D(TS)
        codigo+='if ('+self.EXP.temporal+') goto '+etqV+';\n'
        codigo+='goto '+etqF+';\n'
        codigo+=etqV+': \n'
        for nodo in self.SENTENCIAS:
            codigo+=nodo.getC3D(TS)
        codigo+='goto '+entrada+';\n'
        codigo+=etqF+": \n"
        codigo+='goto '+salida+';\n'
        codigo+=salida+": \n"
        TS.popc()
        TS.popes()

        return  codigo

    def graficarasc(self,padre,grafica):
        nombrehijo='Node'+str(id(self))
        grafica.node(nombrehijo,label=('While'))
        grafica.node('NodeS' + str(id(self)), label=('Sentencias'))
        grafica.edge(nombrehijo, 'NodeS' + str(id(self)))
        for nodo in self.SENTENCIAS:
            nodo.graficarasc('NodeS' + str(id(self)),grafica)
        grafica.edge(padre,nombrehijo)
        self.EXP.graficarasc(nombrehijo,grafica)
