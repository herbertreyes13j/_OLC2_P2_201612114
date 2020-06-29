import AST.Nodo as Nodo


class Lista(Nodo.Nodo):

    def __init__(self, elementos,fila, columna):
        self.fila = fila
        self.columna = columna
        self.elementos=elementos

    def getC3D(self,TS,Global,Traductor):
        codigo=""
        temp=Traductor.getTemp()
        codigo+=temp+'= array();\n'
        contador=0
        for nodo in self.elementos:
            codigo+=nodo.getC3D(TS,Global,Traductor)
            codigo+=temp+'['+str(contador)+'] ='+nodo.temporal+';\n'
            contador+=1
        self.temporal=temp
        return codigo

    def graficarasc(self,padre,grafica):
        nombrehijo = 'Node' + str(id(self))
        grafica.node(nombrehijo, label=('Lista'))
        grafica.edge(padre, nombrehijo)
        grafica.node('Nodec' + str(id(self)), label=('Elementos'))
        grafica.edge(nombrehijo, 'Nodec' + str(id(self)))
        for nodo in self.elementos:
            nodo.graficarasc('Nodec' + str(id(self)),grafica)

