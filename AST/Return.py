import AST.Nodo as Nodo


class Return(Nodo.Nodo):

    def __init__(self,fila,columna,Exp=None):
        self.fila = fila
        self.columna = columna
        self.EXP=Exp

    def getC3D(self,TS,Global,Traductor):
        codigo=""
        if self.EXP==None:
            codigo += 'goto retorno_final;\n'
            return codigo
        else:
            codigo+=self.EXP.getC3D(TS,Global,Traductor)
            temp=Traductor.getTemp()
            codigo+=Traductor.getfromP(temp,0)
            codigo+=Traductor.changestack(temp,self.EXP.temporal)
            codigo += 'goto retorno_final;\n'
            return codigo

    def graficarasc(self,padre,grafica):
        nombrehijo = 'Node' + str(id(self))
        grafica.node(nombrehijo, label=('Return'))
        grafica.edge(padre, nombrehijo)
        if self.EXP is not None:
            self.EXP.graficarasc(nombrehijo,grafica)