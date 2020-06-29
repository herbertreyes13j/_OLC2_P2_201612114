import AST.Nodo as Nodo


class Break(Nodo.Nodo):

    def __init__(self,fila, columna):
        self.fila = fila
        self.columna = columna

    def getC3D(self, TS, Global, Traductor):
        codigo = ""
        codigo+=Traductor.makecomentario("Break")
        codigo += "goto " + TS.getlastes() + ';\n'
        return codigo

    def graficarasc(self, padre, grafica):
        nombrehijo = 'Node' + str(id(self))
        grafica.node(nombrehijo, label=('Break'))
        grafica.edge(padre, nombrehijo)

class Continue(Nodo.Nodo):

    def __init__(self,fila, columna):
        self.fila = fila
        self.columna = columna

    def getC3D(self,TS,Global,Traductor):
        codigo=""
        codigo+=Traductor.makecomentario('Continue')
        codigo+="goto "+TS.getlastcont()+';\n'
        return codigo

    def graficarasc(self,padre,grafica):
        nombrehijo = 'Node' + str(id(self))
        grafica.node(nombrehijo, label=('Continue'))
        grafica.edge(padre, nombrehijo)