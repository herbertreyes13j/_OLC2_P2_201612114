import AST.Nodo as Nodo


class While(Nodo.Nodo):

    def __init__(self, EXP,SENTENCIAS,fila,columna):
        self.fila = fila
        self.columna = columna
        self.EXP=EXP
        self.SENTENCIAS=SENTENCIAS

    def getC3D(self,TS,Global,Traductor):
        codigo=""
        entrada=Traductor.getEtq()
        salida=Traductor.getEtq()
        TS.insercont(entrada)
        TS.inseres(salida)
        codigo+=Traductor.makecomentario("While")
        codigo+=entrada+":\n"
        codigo+=self.EXP.getC3D(TS,Global,Traductor)
        etqV=Traductor.getEtq()
        etqF=Traductor.getEtq()
        codigo+='if ('+self.EXP.temporal+') goto '+etqV+';\n'
        codigo+='goto '+etqF+';\n'
        codigo+=etqV+': \n'
        for nodo in self.SENTENCIAS:
            codigo+=nodo.getC3D(TS,Global,Traductor)
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
        grafica.edge(padre,nombrehijo)
        self.EXP.graficarasc(nombrehijo,grafica)
        grafica.node('NodeS' + str(id(self)), label=('Sentencias'))
        grafica.edge(nombrehijo, 'NodeS' + str(id(self)))
        for nodo in self.SENTENCIAS:
            nodo.graficarasc('NodeS' + str(id(self)),grafica)
