import AST.Nodo as Nodo
from TS.Simbolo import *
from TS.Tipos import *
from AST.Lista import *
from Errores.N_Error import *
from AST.Expresiones import *
class ArregloSimple(Nodo.Nodo):

    def __init__(self, tipo, nombre, valor, fila, columna):
        self.nombre = nombre
        self.valor = valor
        self.fila = fila
        self.columna = columna
        self.tipo = tipo

    def analizar(self,TS,Errores):
        sim = Simbolo(self.tipo.tipo, self.nombre, "", TS.nombre)
        if not TS.push(sim):
            Errores.insertar(N_Error("Semantico",'Variable '+self.nombre+' ya esta definida'),self.fila,self.columna)
            return TIPO_DATOS.ERROR
        if not (isinstance(self.valor,Lista) or isinstance(self.valor,primitivo)):
            Errores.insertar(N_Error("Semantico", 'Solo se puede asignar tipo list a arreglo', self.fila,
                             self.columna))
            return TIPO_DATOS.ERROR

        tipo=self.valor.analizar(TS,Errores)
        if tipo==TIPO_DATOS.ERROR:
            return TIPO_DATOS.ERROR



    def getC3D(self,TS):
        codigo = ""
        codigo += TS.makecomentario("Arreglo Simple [] de " + str(self.nombre))
        if self.valor == None:
            if self.tipo.tipo == TIPO_DATOS.INT:
                val = 0
            elif self.tipo.tipo == TIPO_DATOS.FLOAT:
                val = 0.0
            elif self.tipo.tipo == TIPO_DATOS.CHAR:
                val = '0'
        else:
            codigo += self.valor.getC3D(TS)
            val = self.valor.temporal
        temp = TS.getTemp()
        codigo+=temp+'='+str(val)+';\n'
        sim =TS.obtener(self.nombre)
        sim.posicion=temp
        return codigo

    def graficarasc(self,padre,grafica):
        nombrehijo = 'Node' + str(id(self))
        grafica.node(nombrehijo, label=('Arreglo'))
        grafica.edge(padre, nombrehijo)
        grafica.node('Nodet' + str(id(self)), label=(str(self.tipo.tipo.name)))
        grafica.edge(nombrehijo, 'Nodet' + str(id(self)))
        grafica.node('Nodec' + str(id(self)), label=('[ ]'))
        grafica.edge(nombrehijo, 'Nodec' + str(id(self)))
        grafica.node('Noden' + str(id(self)), label=(str(self.nombre)))
        grafica.edge(nombrehijo, 'Noden' + str(id(self)))
        if self.valor is not None:
            self.valor.graficarasc(nombrehijo, grafica)