import AST.Nodo as Nodo
from TS.TS import *
from TS.Simbolo import *

class Llamada(Nodo.Nodo):

    def __init__(self, nombre,fila, columna,elementos=[]):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna
        self.elementos=elementos

    def getC3D(self,TS,Global,Traductor):
        codigo=""
        if self.nombre=='printf':
            codigo+=Traductor.makecomentario("Printf")
            ele=self.elementos[0].getC3D(TS,Global,Traductor)
            if len(self.elementos)==1:
                codigo += ele
                codigo+='print('+str(self.elementos[0].temporal)+');\n'
            else:
                ele2 = self.elementos[1].getC3D(TS, Global, Traductor)
                codigo += ele
                codigo += ele2
                codigo+='print('+str(self.elementos[0].temporal.replace('%d',self.elementos[1].temporal))+');\n';
            return codigo;
        elif self.nombre=="scanf":
            return codigo
        else:
            funcion=Global.obtenerfunc(self.nombre)

            codigoparametros=""

            for nodo in self.elementos:
                codigoparametros+=nodo.getC3D(TS,Global,Traductor)

            if not self.nombre in Global.traducidas:
                etiqueta=Traductor.getEtq()
                codigo+='goto '+etiqueta+';\n'
                Global.agregartrad(self.nombre)
                Pila=TablaDeSimbolos(self.nombre)
                cuenta=0
                for ele in self.elementos:
                    Pila.push(Simbolo(funcion.parametros[cuenta].tipo,funcion.parametros[cuenta].nombre,Pila.size,self.nombre))
                    cuenta+=1
                codigo+=self.nombre+":\n"
                codigo+=funcion.getC3D(Pila,Global,Traductor)
                codigo+='goto retorno_final;\n'
                codigo += etiqueta + ':\n'

            conteo=0
            codigo += codigoparametros
            if TS.nombre!='main':
                codigo+=Traductor.makecomentario("Almacenando temporales")
                temp=Traductor.getTemp()

                for temporal in TS.almacenados:
                    codigo+=Traductor.getfromP(temp,TS.size+conteo)
                    codigo+=Traductor.changestack(temp,temporal)
                    conteo+=1

            temp=Traductor.getTemp()
            codigo+='$ra ='+str(Global.cuentatrad)+';\n'
            codigo+=Traductor.makecomentario('Simulando cambio de ambito')
            codigo+=Traductor.getfromP(temp,TS.size)

            for nodo in self.elementos:
                codigo+=Traductor.make3d(temp,'1','+',temp)
                codigo+=Traductor.changestack(temp,nodo.temporal)
            codigo+=Traductor.makecomentario('Cambio de ambito')
            codigo+=Traductor.incP(TS.size+conteo)
            codigo+='goto '+self.nombre+';\n'

            Global.agregarcodigo("if($ra=="+str(Global.cuentatrad)+') goto Regreso'+str(Global.cuentatrad)+';\n')
            codigo+='Regreso'+str(Global.cuentatrad)+':\n'
            temp = Traductor.getTemp()
            codigo += Traductor.getfromP(temp, 0)
            codigo += Traductor.getfromStack(temp,temp)
            self.temporal=temp
            codigo+=Traductor.makecomentario('Cambio de ambito')
            codigo+=Traductor.decP(TS.size+conteo)
            Global.cuentatrad+=1
            if TS.nombre!='main':
                codigo+=Traductor.makecomentario("Recuperando temporales")
                temp=Traductor.getTemp()
                conteo=0
                for temporal in TS.almacenados:
                    codigo+=Traductor.getfromP(temp,TS.size+conteo)
                    codigo+=Traductor.getfromStack(temporal,temp)
                    conteo+=1

            return codigo;

    def graficarasc(self,padre,grafica):
        nombrehijo='Node'+str(id(self))
        grafica.node(nombrehijo,label=('Llamada'))
        grafica.edge(padre,nombrehijo)
        grafica.node('Noden' + str(id(self)), label=(str(self.nombre)))
        grafica.edge(nombrehijo, 'Noden' + str(id(self)))
        grafica.node('Nodep' + str(id(self)), label=('Parametros'))
        grafica.edge(nombrehijo, 'Nodep' + str(id(self)))
        for node in self.elementos:
            node.graficarasc('Nodep' + str(id(self)),grafica)
