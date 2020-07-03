import AST.Nodo as Nodo


class Etiqueta(Nodo.Nodo):

    def __init__(self,nombre,fila,columna):
        self.fila = fila
        self.columna = columna
        self.nombre=nombre
    def analizar(self,TS,Errores):
        return

    def getC3D(self,TS):
        codigo=""
        codigo+=self.nombre+':\n'
        return codigo

    def graficarasc(self,padre,grafica):
        nombrehijo = 'Node' + str(id(self))
        grafica.node(nombrehijo, label=('Label'))
        grafica.edge(padre, nombrehijo)
        grafica.node('NodeV' + str(id(self)), label=(self.nombre))
        grafica.edge(nombrehijo, 'NodeV' + str(id(self)))


class Goto(Nodo.Nodo):

    def __init__(self,nombre,fila,columna):
        self.fila = fila
        self.columna = columna
        self.nombre=nombre

    def analizar(self, TS, Errores):
        return

    def getC3D(self, TS):
        codigo = ""
        codigo+='goto '+self.nombre+';\n'
        return codigo

    def graficarasc(self, padre, grafica):
        nombrehijo = 'Node' + str(id(self))
        grafica.node(nombrehijo, label=('Goto'))
        grafica.edge(padre, nombrehijo)
        grafica.node('NodeV' + str(id(self)), label=(self.nombre))
        grafica.edge(nombrehijo, 'NodeV' + str(id(self)))
