import AST.Nodo as Nodo


class For(Nodo.Nodo):

    def __init__(self, Inicial,Condicion,Incremento,Sentencias,fila,columna):
        self.fila = fila
        self.columna = columna
        self.Incial=Inicial
        self.Condicion=Condicion
        self.Incremento=Incremento
        self.Sentencias=Sentencias

    def getC3D(self,TS,Global,Traductor):
        codigo=""
        codigo+=Traductor.makecomentario("For")
        if self.Incial is not None:
            codigo+=Traductor.makecomentario('Declaracion')
            codigo+=self.Incial.getC3D(TS,Global,Traductor)
        entrada = Traductor.getEtq()
        salida = Traductor.getEtq()
        TS.insercont(entrada)
        TS.inseres(salida)
        codigo += Traductor.makecomentario("Condicion")
        codigo += entrada + ":\n"
        codigo += self.Condicion.getC3D(TS, Global, Traductor)
        etqV = Traductor.getEtq()
        etqF = Traductor.getEtq()
        codigo += 'if (' + self.Condicion.temporal + ') goto ' + etqV + ';\n'
        codigo += 'goto ' + etqF + ';\n'
        codigo += etqV + ': \n'
        for nodo in self.Sentencias:
            codigo += nodo.getC3D(TS, Global, Traductor)
        if self.Incremento is not None:
            codigo+=Traductor.makecomentario('Incremento For')
            codigo+=self.Incremento.getC3D(TS,Global,Traductor)
        codigo += 'goto ' + entrada + ';\n'
        codigo += etqF + ": \n"
        codigo += 'goto ' + salida + ';\n'
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
