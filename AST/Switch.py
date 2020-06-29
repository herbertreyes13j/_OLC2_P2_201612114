import AST.Nodo as Nodo


class Switch(Nodo.Nodo):

    def __init__(self, EXP,Casos,fila, columna,Default=None):
        self.fila = fila
        self.columna = columna
        self.EXP=EXP
        self.Casos=Casos
        self.Default=Default

    def getC3D(self,TS,Global,Traductor):
        codigo = ""
        salida = Traductor.getEtq()
        TS.inseres(salida)
        codigo += Traductor.makecomentario("Switch")
        codigo += self.EXP.getC3D(TS, Global, Traductor)
        for nodo in self.Casos:
            nodo.evaluador=self.EXP.temporal
            codigo+=nodo.getC3D(TS,Global,Traductor)
        if self.Default is not None:
            codigo+=self.Default.getC3D(TS,Global,Traductor)
        codigo += salida + ": \n"
        TS.popes()
        return codigo

    def graficarasc(self,padre,grafica):
        nombrehijo = 'Node' + str(id(self))
        grafica.node(nombrehijo, label=('Switch'))
        grafica.edge(padre, nombrehijo)
        self.EXP.graficarasc(nombrehijo, grafica)
        grafica.node('NodeS' + str(id(self)), label=('Casos'))
        grafica.edge(nombrehijo, 'NodeS' + str(id(self)))
        for nodo in self.Casos:
            nodo.graficarasc('NodeS' + str(id(self)), grafica)
        if self.Default is not None:
            self.Default.graficarasc(nombrehijo,grafica)

class Casos(Nodo.Nodo):
    def __init__(self,Exp,Sentencias,fila,columna):
        self.fila=fila
        self.columna=columna
        self.Exp=Exp
        self.sentencias=Sentencias
        self.evaluador=""

    def getC3D(self,TS,Global,Traductor):
        codigo=""
        etqV = Traductor.getEtq()
        etqF = Traductor.getEtq()
        codigo+=self.Exp.getC3D(TS,Global,Traductor)
        codigo += 'if (' + self.evaluador +'=='+self.Exp.temporal+ ') goto ' + etqV + ';\n'
        codigo += 'goto ' + etqF + ';\n'
        codigo += etqV + ':\n'
        for nodo in self.sentencias:
            codigo += nodo.getC3D(TS, Global, Traductor)
        codigo+=etqF+':\n'
        return codigo

    def graficarasc(self,padre,grafica):
        nombrehijo = 'Node' + str(id(self))
        grafica.node(nombrehijo, label=('Caso'))
        grafica.edge(padre, nombrehijo)
        self.Exp.graficarasc(nombrehijo, grafica)
        grafica.node('NodeS' + str(id(self)), label=('Instrucciones'))
        grafica.edge(nombrehijo, 'NodeS' + str(id(self)))
        for nodo in self.sentencias:
            nodo.graficarasc('NodeS' + str(id(self)), grafica)

class Default(Nodo.Nodo):
    def __init__(self,Sentencias,fila,columna):
        self.fila=fila
        self.columna=columna
        self.sentencias=Sentencias

    def getC3D(self,TS,Global,Traductor):
        codigo=""
        for nodo in self.sentencias:
            codigo+=nodo.getC3D(TS,Global,Traductor)

        return codigo

    def graficarasc(self,padre,grafica):
        nombrehijo = 'Node' + str(id(self))
        grafica.node(nombrehijo, label=('Default'))
        grafica.edge(padre, nombrehijo)
        grafica.node('NodeS' + str(id(self)), label=('Instrucciones'))
        grafica.edge(nombrehijo, 'NodeS' + str(id(self)))
        for nodo in self.sentencias:
            nodo.graficarasc('NodeS' + str(id(self)), grafica)