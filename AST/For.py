import AST.Nodo as Nodo
from TS.Tipos import *
from Errores.N_Error import *

class For(Nodo.Nodo):

    def __init__(self, Inicial,Condicion,Incremento,Sentencias,fila,columna):
        self.fila = fila
        self.columna = columna
        self.Incial=Inicial
        self.Condicion=Condicion
        self.Incremento=Incremento
        self.Sentencias=Sentencias

    def analizar(self,TS,Errores):
        if self.Incial is not None:
            tipo = self.Incial.analizar(TS,Errores)
            if tipo==TIPO_DATOS.ERROR:
                return TIPO_DATOS.ERROR
        tipo=self.Condicion.analizar(TS,Errores)
        if not (
                tipo == TIPO_DATOS.INT or tipo == TIPO_DATOS.CHAR or tipo == TIPO_DATOS.DOUBLE or tipo == TIPO_DATOS.FLOAT):
            Errores.insertar(
                N_Error("Semantico", "Tipo de dato de switch no es valido ", self.fila, self.columna))
            return TIPO_DATOS.ERROR

        if self.Incremento is not None:
            tipo = self.Incremento.analizar(TS,Errores)
            if tipo==TIPO_DATOS.ERROR:
                return TIPO_DATOS.ERROR



        for nodo in self.Sentencias:
            tipo=nodo.analizar(TS,Errores)
            if tipo==TIPO_DATOS.ERROR:
                return tipo


    def getC3D(self,TS):
        codigo=""
        codigo+=TS.makecomentario("For")
        if self.Incial is not None:
            codigo+=TS.makecomentario('Declaracion')
            codigo+=self.Incial.getC3D(TS)
        entrada = TS.getEtq()
        salida = TS.getEtq()
        incremento=TS.getEtq()
        TS.insercont(incremento)
        TS.inseres(salida)

        codigo += TS.makecomentario("Condicion")
        codigo += entrada + ":\n"
        codigo += self.Condicion.getC3D(TS)
        etqV = TS.getEtq()
        etqF = TS.getEtq()
        codigo += 'if (' + self.Condicion.temporal + ') goto ' + etqV + ';\n'
        codigo += 'goto ' + etqF + ';\n'
        codigo += etqV + ': \n'
        for nodo in self.Sentencias:
            codigo += nodo.getC3D(TS)
        codigo += 'goto ' + incremento + ';\n'
        codigo+=TS.makecomentario('FALSA')
        codigo += etqF + ": \n"
        codigo += 'goto ' + salida + ';\n'
        codigo+=TS.makecomentario("Goto incrementar")
        codigo += incremento + ':\n'
        if self.Incremento is not None:
            codigo+=TS.makecomentario('Incremento For')
            codigo+=self.Incremento.getC3D(TS)
        codigo += 'goto ' + entrada + ';\n'
        codigo+=TS.makecomentario("salida")
        codigo += salida + ": \n"
        TS.popc()
        TS.popes()
        return codigo

    def graficarasc(self,padre,grafica):
        nombrehijo='Node'+str(id(self))
        grafica.node(nombrehijo,label=('For'))
        grafica.edge(padre,nombrehijo)
        if self.Incial is not None:
            self.Incial.graficarasc(nombrehijo,grafica)
        self.Condicion.graficarasc(nombrehijo,grafica)
        if self.Incremento is not Nodo:
            self.Incremento.graficarasc(nombrehijo,grafica)
