import AST.Nodo as Nodo
from TS.TS import *
from TS.Simbolo import *
from Errores.N_Error import *
from TS.Tipos import *
class Llamada(Nodo.Nodo):

    def __init__(self, nombre,fila, columna,elementos=[]):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna
        self.elementos=elementos

    def analizar(self,TS,Errores):
        if self.nombre=='printf':
            return
        funcion = TS.obtenerfunc(self.nombre)
        if funcion is None:
            Errores.insertar(
                N_Error("Semantico", "No existe funcion "+self.nombre, self.fila, self.columna))
            return TIPO_DATOS.ERROR
        if len(funcion.parametros)==len(self.elementos):
            cuenta=0
            for nodo in self.elementos:
                tipo1=nodo.analizar(TS,Errores)
                tipo2=funcion.parametros[cuenta].tipo.tipo
                if tipo1!=tipo2:
                    N_Error("Semantico",
                            "Error llamada, no coincides tipos en parametros " + self.nombre, self.fila,
                            self.columna)
                    return TIPO_DATOS.ERROR
        else:
            Errores.insertar(
                N_Error("Semantico", "Error llamada, no posee mismo numero de parametros que funcion " + self.nombre, self.fila, self.columna))
            return TIPO_DATOS.ERROR

        return funcion.tipo.tipo

    def getC3D(self,TS):
        codigo=""
        if self.nombre=='printf':
            codigo+=TS.makecomentario("Printf")
            ele=self.elementos[0].getC3D(TS)
            if len(self.elementos)==1:
                codigo += ele
                codigo+='print('+str(self.elementos[0].temporal)+');\n'
            else:
                ele2 = self.elementos[1].getC3D(TS)
                codigo += ele
                codigo += ele2
                codigo+='print('+str(self.elementos[0].temporal.replace('%d',self.elementos[1].temporal))+');\n';
            return codigo;
        elif self.nombre=="scanf":
            return codigo
        else:
            funcion=TS.obtenerfunc(self.nombre)
            conteo=funcion.cuentatrad
            funcion.cuentatrad += 1
            temporales=[]
            codigo+=TS.makecomentario("Generando codigo de Parametros")
            for nodo in self.elementos:
                codigo+=nodo.getC3D(TS)
                codigo+='$s1[$sp] = '+nodo.temporal+';\n'
                codigo+=TS.incP(1)
                temporales.append(nodo.temporal)

            cuenta=0
            ambito=TS.nombre
            TS.nombre=self.nombre
            for nodo in funcion.parametros:
                sim=TS.obtener(nodo.nombre)
                codigo+=sim.posicion+'='+temporales[cuenta]+';\n'
                cuenta+=1
            TS.nombre=ambito
            codigo+=TS.makecomentario("Make Call ")
            codigo+='$s0[$ra] = '+str(conteo)+';\n'
            codigo+='$ra = $ra + 1;\n'
            codigo+='goto '+self.nombre+';\n'

            codigo+=self.nombre+'_retorno_'+str(conteo)+':\n'
            temp=TS.getTemp()

            if TS.nombre==self.nombre:
                temp=TS.getTemp()
                codigo+=TS.makecomentario('ACA ES DONDE FALLA')
                cuenta=0
                for nodo in funcion.parametros:
                    sim=TS.obtener(nodo.nombre)
                    if cuenta==0:
                        codigo += temp + '=' + '$sp-'+str(len(funcion.parametros))+';\n'
                    else:
                        codigo+=temp+'='+'$sp-1;\n'
                    codigo+=sim.posicion+'= $s1['+temp+'];\n'
                    cuenta+=1
            codigo+=temp+'='+'$v'+str(funcion.id)+';\n'
            funcion.codigofin+='if($s0[$ra]=='+str(conteo)+') goto '+self.nombre+'_retorno_'+str(conteo)+';\n'
            self.temporal='$v'+str(funcion.id)
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
