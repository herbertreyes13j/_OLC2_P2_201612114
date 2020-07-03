import AST.Nodo as Nodo
from TS.Tipos import *
from Errores.N_Error import *

class AccesoStruct(Nodo.Nodo):

    def __init__(self, Atributo1,Atributo2,fila,columna):
        self.fila = fila
        self.columna = columna
        self.Atributo1=Atributo1
        self.Atributo2=Atributo2

    def analizar(self,TS,Errores):

        sim = TS.obtener(self.Atributo1.nombre)
        if sim is None:
            Errores.insertar(N_Error("Semantico","Error acceso Struct, struct "+self.Atributo1.nombre+' no esta definido',
                                     self.fila,self.columna))
            return TIPO_DATOS.ERROR

        struct=TS.obtenerstruct(sim.tipo)

        for nodo in struct.atributos:
            if nodo.nombre==self.Atributo2.nombre:
                return

        Errores.insertar(N_Error("Semantico","Acceso no valido, porque no esta definido en struct",self.fila,self.columna))
        return TIPO_DATOS.ERROR

    def getC3D(self,TS):
        codigo=""
        sim = TS.obtener(self.Atributo1.nombre)
        codigo+=sim.posicion+self.Atributo1.getC3D(TS)
        codigo+='[\''+self.Atributo2.nombre+'\']'+self.Atributo2.getC3D(TS)
        self.temporal=codigo
        return ""


    def graficarasc(self,padre,grafica):
        nombrehijo = 'Node' + str(id(self))
        grafica.node(nombrehijo, label=('Acceso Struct'))
        grafica.edge(padre, nombrehijo)
        self.Atributo1.graficarasc(nombrehijo,grafica)
        self.Atributo2.graficarasc(nombrehijo,grafica)
