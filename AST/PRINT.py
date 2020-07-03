import AST.Nodo as Nodo


class Print(Nodo.Nodo):

    def __init__(self,texto,fila,columna,expresiones=[]):
        self.fila = fila
        self.columna = columna
        self.texto=texto
        self.expresiones=expresiones
    def analizar(self,TS,Errores):
        for nodo in self.expresiones:
            nodo.analizar(TS,Errores)
        return

    def getC3D(self,TS):
        codigo=""
        if len(self.expresiones)==0:
            codigo+='print(\"'+self.texto+'\");\n'
        else:
            cuenta=0
            cuenta1=0
            aux=""
            ignora=False
            for letra in self.texto:
                if letra=="%":
                    codigo+="print(\""+aux+"\");\n"
                    codigo+=self.expresiones[cuenta].getC3D(TS)
                    codigo+="print("+self.expresiones[cuenta].temporal+");\n"
                    cuenta+=1
                    aux=""
                    ignora=True
                else:
                    if ignora:
                        ignora=False
                    else:
                        #letra.replace("\\\\","\\")
                        aux+=letra
            codigo+='print(\"'+aux+"\");\n"

        return codigo

    def graficarasc(self,padre,grafica):
        nombrehijo = 'Node' + str(id(self))
        grafica.node(nombrehijo, label=('Label'))
        grafica.edge(padre, nombrehijo)
        grafica.node('NodeV' + str(id(self)), label=(self.nombre))
        grafica.edge(nombrehijo, 'NodeV' + str(id(self)))

import AST.Nodo as Nodo


class Scanf(Nodo.Nodo):

    def __init__(self,fila,columna):
        self.fila = fila
        self.columna = columna
        self.temporal=""
    def analizar(self,TS,Errores):
        return

    def getC3D(self,TS):
        codigo=""
        temp = TS.getTemp()
        codigo += temp + '= read();\n'
        self.temporal = temp
        return codigo

    def graficarasc(self,padre,grafica):
        nombrehijo = 'Node' + str(id(self))
        grafica.node(nombrehijo, label=('Label'))
        grafica.edge(padre, nombrehijo)
        grafica.node('NodeV' + str(id(self)), label=(self.nombre))
        grafica.edge(nombrehijo, 'NodeV' + str(id(self)))

