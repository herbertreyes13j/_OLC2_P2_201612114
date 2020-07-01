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
            if type(nodo) == Lista:
                codigo+=nodo.listparalist(temp+'['+str(contador)+']',TS,Global,Traductor)
            else:
                codigo+=nodo.getC3D(TS,Global,Traductor)
                codigo+=temp+'['+str(contador)+'] ='+nodo.temporal+';\n'
            contador+=1
        self.temporal=temp
        return codigo

    def listparalist(self,acceso,TS,Global,Traductor):
        codigo=""
        contador=0;
        for nodo in self.elementos:
            if type(nodo)==Lista:
                var=str(acceso)+'['+str(contador)+']'
                codigo+=nodo.listparalist(var,TS,Global,Traductor)
            else:
                codigo+=nodo.getC3D(TS,Global,Traductor)
                codigo+=str(acceso)+'['+str(contador)+'] ='+nodo.temporal+';\n'
            contador+=1
        return codigo
    def graficarasc(self,padre,grafica):
        nombrehijo = 'Node' + str(id(self))
        grafica.node(nombrehijo, label=('Lista'))
        grafica.edge(padre, nombrehijo)
        grafica.node('Nodec' + str(id(self)), label=('Elementos'))
        grafica.edge(nombrehijo, 'Nodec' + str(id(self)))
        for nodo in self.elementos:
            nodo.graficarasc('Nodec' + str(id(self)),grafica)

