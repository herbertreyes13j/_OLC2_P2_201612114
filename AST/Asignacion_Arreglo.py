import AST.Nodo as Nodo
from AST.Expresiones import *
from Errores.N_Error import *
from TS.Tipos import *

class Asignacion_Arreglo(Nodo.Nodo):
    def __init__(self, nombre,accesos,fila, columna):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna
        self.acceos=accesos

    def analizar(self,TS,Errores):
        hola = variable(self.nombre,self.fila,self.columna)
        tipo=hola.analizar(TS,Errores)
        if tipo==TIPO_DATOS.ERROR:
            return TIPO_DATOS.ERROR

        for nodo in self.acceos:
            tipo=nodo.analizar(TS,Errores)
            if tipo==TIPO_DATOS.ERROR:
                return TIPO_DATOS.ERROR
        return tipo

    def getC3D(self,TS):
        codigo = ""
        simb=TS.obtener(self.nombre)
        temp = simb.posicion
        for nodo in self.acceos:
            codigo += nodo.getC3D(TS)
            temp += '[' + str(nodo.temporal) + ']'
        self.temporal=temp
        return codigo

    def graficarasc(self,padre,grafica):
        nombrehijo = 'Node' + str(id(self))
        grafica.node(nombrehijo, label=('Acceso Arreglo'))
        grafica.edge(padre, nombrehijo)
        grafica.node('Noden' + str(id(self)), label=(str(self.nombre)))
        grafica.node('Nodec' + str(id(self)), label=('dimensiones'))
        grafica.edge(nombrehijo, 'Nodec' + str(id(self)))
        for nodo in self.acceos:
            nodo.graficarasc('Nodec' + str(id(self)), grafica)
        grafica.edge(nombrehijo, 'Noden' + str(id(self)))


class Asignacion_Arreglo_Op(Nodo.Nodo):
    def __init__(self, nombre,op, valor,accesos,fila, columna):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna
        self.valor = valor
        self.acceos=accesos
        self.op=op

    def analizar(self,TS,Errores):
        pass
    def getC3D(self,TS):
        codigo=""
        codigo += TS.makecomentario("Asignacion tipo " + str(self.op) + ' de variable ' + self.nombre)
        hola = variable(self.nombre, self.fila, self.columna)
        codigo += hola.getC3D(TS)
        codigo += self.valor.getC3D(TS)
        temp=hola.temporal
        for nodo in self.acceos:
            codigo+=nodo.getC3D(TS)
            temp+='['+str(nodo.temporal)+']'
        if self.op == "=":
            codigo += temp + '=' + str(self.valor.temporal) + ';\n'
            return codigo
        else:
            codigo += TS.make3d(temp, temp, self.op.replace('=', ""), self.valor.temporal)
            return codigo
        return codigo

    def graficarasc(self,padre,grafica):
        nombrehijo = 'Node' + str(id(self))
        grafica.node(nombrehijo, label=('Asignacion Arreglo'))
        grafica.edge(padre, nombrehijo)
        grafica.node('Noden' + str(id(self)), label=(str(self.nombre)))
        grafica.edge(nombrehijo,'Noden' + str(id(self)))
        grafica.node('Nodec' + str(id(self)), label=('Accesos'))
        grafica.edge(nombrehijo, 'Nodec' + str(id(self)))
        for nodo in self.acceos:
            nodo.graficarasc('Nodec' + str(id(self)), grafica)
        grafica.node('Nodeo' + str(id(self)), label=(str(self.op)))
        grafica.edge(nombrehijo,'Nodeo' + str(id(self)))
        if self.valor is not None:
            self.valor.graficarasc(nombrehijo, grafica)