import AST.Nodo as Nodo


class Asignacion_Struct(Nodo.Nodo):

    def __init__(self, acceso,valor,op,fila, columna):
        self.fila = fila
        self.columna = columna
        self.acceso=acceso
        self.valor=valor
        self.op=op

    def analizar(self,TS,Errores):
        self.acceso.analizar(TS,Errores)
        self.valor.analizar(TS,Errores)

    def getC3D(self,TS):
        codigo=""
        codigo+=self.acceso.getC3D(TS)
        temp=self.acceso.temporal
        codigo+=self.valor.getC3D(TS)
        if self.op=='=':
            codigo+=temp+'='+self.valor.temporal+';\n'
        return codigo
    def graficarasc(self,padre,grafica):
        nombrehijo = 'Node' + str(id(self))
        grafica.node(nombrehijo, label=('Asignacion Struct'))
        grafica.edge(padre, nombrehijo)
        self.acceso.graficarasc(nombrehijo,grafica)
        grafica.node('Nodec' + str(id(self)), label=(self.op))
        grafica.edge(nombrehijo, 'Nodec' + str(id(self)))
        self.valor.graficarasc(nombrehijo,grafica)