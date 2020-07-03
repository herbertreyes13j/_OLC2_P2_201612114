import AST.Nodo as Nodo
from TS.Tipos import *

class Lista(Nodo.Nodo):

    def __init__(self, elementos,fila, columna):
        self.fila = fila
        self.columna = columna
        self.elementos=elementos

    def analizar(self,TS,Errores):
        for nodo in self.elementos:
            tipo=nodo.analizar(TS,Errores)
            if tipo==TIPO_DATOS.ERROR:
                return TIPO_DATOS.ERROR

    def getC3D(self,TS):
        codigo=""
        temp=TS.getTemp()
        codigo+=temp+'= array();\n'
        contador=0
        for nodo in self.elementos:
            if type(nodo) == Lista:
                codigo+=nodo.listparalist(temp+'['+str(contador)+']',TS)
            else:
                codigo+=nodo.getC3D(TS)
                codigo+=temp+'['+str(contador)+'] ='+nodo.temporal+';\n'
            contador+=1
        self.temporal='&'+temp
        return codigo

    def listparalist(self,acceso,TS):
        codigo=""
        contador=0;
        for nodo in self.elementos:
            if type(nodo)==Lista:
                var=str(acceso)+'['+str(contador)+']'
                codigo+=nodo.listparalist(var,TS)
            else:
                codigo+=nodo.getC3D(TS)
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

