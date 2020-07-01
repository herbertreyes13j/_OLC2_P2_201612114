import AST.Nodo as Nodo
import TS.Tipos as Tipos


class Aritmetica(Nodo.Nodo):
    def __init__(self, Exp1, Exp2, op, fila, col):
        self.Exp1=Exp1
        self.Exp2=Exp2
        self.op=op
        self.fila=fila
        self.columna=col

    def getC3D(self,TS,Global,Traductor):
        codigo=""
        temp = Traductor.getTemp()

        codigo+=self.Exp1.getC3D(TS,Global,Traductor)
        codigo+=self.Exp2.getC3D(TS,Global,Traductor)
        self.temporal=temp

        codigo+=Traductor.make3d(temp,self.Exp1.temporal,self.op,self.Exp2.temporal)
        if TS is not None:
            TS.almacenados.append(temp)
        return codigo

    def graficarasc(self,padre,grafica):
        nombrehijo='Node'+str(id(self))
        grafica.node(nombrehijo,label=('Exp'))
        grafica.edge(padre,nombrehijo)
        if self.Exp1 is not None:
            self.Exp1.graficarasc(nombrehijo,grafica)
        grafica.node('NodeE1'+str(id(self)),label=(str(self.op)))
        grafica.edge(nombrehijo,'NodeE1'+str(id(self)))
        if self.Exp2 is not None:
            self.Exp2.graficarasc(nombrehijo,grafica)

class Relacional(Nodo.Nodo):
    def __init__(self,Exp1,Exp2,op,fila,col):
        self.Exp1=Exp1
        self.Exp2=Exp2
        self.op=op
        self.fila=fila
        self.columna=col

    def getC3D(self,TS,Global,Traductor):
        codigo=""
        temp = Traductor.getTemp()

        codigo+=self.Exp1.getC3D(TS,Global,Traductor)
        codigo+=self.Exp2.getC3D(TS,Global,Traductor)
        self.temporal=temp

        codigo+=Traductor.make3d(temp,self.Exp1.temporal,self.op,self.Exp2.temporal)
        if TS is not None:
            TS.almacenados.append(temp)
        return codigo

    def graficarasc(self,padre,grafica):
        nombrehijo='Node'+str(id(self))
        grafica.node(nombrehijo,label=('Exp'))
        grafica.edge(padre,nombrehijo)
        if self.Exp1 is not None:
            self.Exp1.graficarasc(nombrehijo,grafica)
        grafica.node('NodeE1'+str(id(self)),label=(str(self.op)))
        grafica.edge(nombrehijo,'NodeE1'+str(id(self)))
        if self.Exp2 is not None:
            self.Exp2.graficarasc(nombrehijo,grafica)

class primitivo(Nodo.Nodo):
    def __init__(self,Valor,fila,col,tipo):
        self.fila=fila
        self.columna=col
        self.valor=Valor
        self.temporal=""
        if tipo == "decimal": self.tipo=Tipos.TIPO(Tipos.TIPO_DATOS.FLOAT)
        elif tipo == "entero": self.tipo=Tipos.TIPO(Tipos.TIPO_DATOS.INT)
        elif tipo == "char": self.tipo = Tipos.TIPO(Tipos.TIPO_DATOS.CHAR)
        elif tipo == "string":self.tipo = Tipos.TIPO(Tipos.TIPO_DATOS.STRING)

    def getC3D(self,TS,Global,Traductor):
        if self.tipo.tipo==Tipos.TIPO_DATOS.CHAR:
            self.temporal='\''+str(self.valor)+'\''
        elif self.tipo.tipo==Tipos.TIPO_DATOS.STRING:
            self.temporal='\"'+str(self.valor)+'\"'
        else:
            self.temporal=str(self.valor)
        return ""

    def graficarasc(self,padre,grafica):
        nombrehijo='Node'+str(id(self))
        grafica.node(nombrehijo,label=('Exp'))
        grafica.edge(padre,nombrehijo)
        grafica.node('NodeV'+str(id(self)),label=(str(self.valor)))
        grafica.edge(nombrehijo,'NodeV'+str(id(self)))

class variable(Nodo.Nodo):
    def __init__(self,nombre,fila,col):
        self.fila=fila
        self.columna=col
        self.nombre=nombre
        self.temporal=""

    def getC3D(self,TS,Global,Traductor):
        codigo=""
        if TS is not None:
            simbolo=TS.obtener(self.nombre)
            if simbolo!=None:
                temp2=Traductor.getTemp()
                temp=Traductor.getTemp()
                codigo+=Traductor.getfromP(temp2,simbolo.posicion)
                codigo+=Traductor.getfromStack(temp,temp2)
                self.temporal=temp
                return codigo
        simbolo = Global.obtener(self.nombre)
        temp = Traductor.getTemp()
        codigo += Traductor.getfromStack(temp, simbolo.posicion)
        self.temporal = temp
        if TS is not None:
            TS.almacenados.append(temp)
        return codigo

    def getPosicion(self,TS,Global,Traductor):
        codigo=""
        if TS is not None:
            simbolo=TS.obtener(self.nombre)
            if simbolo is not None:
                temp2=Traductor.getTemp()
                codigo+=Traductor.getfromP(temp2,simbolo.posicion)
                self.temporal=temp2
                return codigo
        simbolo = Global.obtener(self.nombre)
        self.temporal = simbolo.posicion
        return codigo

    def graficarasc(self,padre,grafica):
        nombrehijo='Node'+str(id(self))
        grafica.node(nombrehijo,label=('Exp'))
        grafica.edge(padre,nombrehijo)
        grafica.node('NodeI'+str(id(self)),label=(str(self.nombre)))
        grafica.edge(nombrehijo,'NodeI'+str(id(self)))

class bitabit(Nodo.Nodo):
    def __init__(self,Exp1,Exp2,op,fila,col):
        self.fila=fila
        self.columna=col
        self.Exp1=Exp1
        self.Exp2=Exp2
        self.op=op
        self.temporal=""
    def getC3D(self,TS,Global,Traductor):
        codigo=""
        temp = Traductor.getTemp()
        codigo+=self.Exp1.getC3D(TS,Global,Traductor)
        codigo+=self.Exp2.getC3D(TS,Global,Traductor)
        self.temporal=temp
        codigo+=Traductor.make3d(temp,self.Exp1.temporal,self.op,self.Exp2.temporal)
        if TS is not None:
            TS.almacenados.append(temp)
        return codigo

    def graficarasc(self,padre,grafica):
        nombrehijo='Node'+str(id(self))
        grafica.node(nombrehijo,label=('Exp'))
        grafica.edge(padre,nombrehijo)
        if self.Exp1 is not None:
            self.Exp1.graficarasc(nombrehijo,grafica)
        grafica.node('NodeE1'+str(id(self)),label=(str(self.op)))
        grafica.edge(nombrehijo,'NodeE1'+str(id(self)))
        if self.Exp2 is not None:
            self.Exp2.graficarasc(nombrehijo,grafica)

class logica(Nodo.Nodo):
    def __init__(self,Exp1,Exp2,op,fila,col):
        self.fila=fila
        self.columna=col
        self.Exp1=Exp1
        self.Exp2=Exp2
        self.op=op

    def getC3D(self,TS,Global,Traductor):
        codigo=""
        temp = Traductor.getTemp()
        codigo+=self.Exp1.getC3D(TS,Global,Traductor)
        codigo+=self.Exp2.getC3D(TS,Global,Traductor)
        self.temporal=temp
        codigo+=Traductor.make3d(temp,self.Exp1.temporal,self.op,self.Exp2.temporal)
        if TS is not None:
            TS.almacenados.append(temp)
        return codigo

    def graficarasc(self,padre,grafica):
        nombrehijo='Node'+str(id(self))
        grafica.node(nombrehijo,label=('Exp'))
        grafica.edge(padre,nombrehijo)
        if self.Exp1 is not None:
            self.Exp1.graficarasc(nombrehijo,grafica)
        grafica.node('NodeE1'+str(id(self)),label=(str(self.op)))
        grafica.edge(nombrehijo,'NodeE1'+str(id(self)))
        if self.Exp2 is not None:
            self.Exp2.graficarasc(nombrehijo,grafica)

class incremento(Nodo.Nodo):
    def __init__(self,Exp1,op,primero,fila,col):
        self.fila=fila
        self.columna=col
        self.Exp1=Exp1
        self.primero=primero
        self.op=op

    def getC3D(self,TS,Global,Traductor):
        codigo=""
        if self.primero:
            codigo+=self.Exp1.getC3D(TS,Global,Traductor)
            temporal=self.Exp1.temporal;
            codigo+=self.Exp1.getPosicion(TS,Global,Traductor)
            codigo+=Traductor.make3d(temporal,temporal,'+',1)
            codigo+=Traductor.changestack(self.Exp1.temporal,temporal)
            self.temporal=temporal
            if TS is not None:
                TS.almacenados.append(temporal)
            return codigo
        else:
            codigo += self.Exp1.getC3D(TS, Global, Traductor)
            temporal = self.Exp1.temporal;
            temporal2=Traductor.getTemp()
            codigo += self.Exp1.getPosicion(TS, Global, Traductor)
            codigo += Traductor.make3d(temporal2, temporal, '+', 1)
            codigo += Traductor.changestack(self.Exp1.temporal, temporal2)
            self.temporal = temporal
            if TS is not None:
                TS.almacenados.append(temporal)
            return codigo


    def graficarasc(self,padre,grafica):
        nombrehijo = 'Node' + str(id(self))
        grafica.node(nombrehijo, label=('Exp'))
        grafica.edge(padre, nombrehijo)
        if self.primero:
            grafica.node('NodeE1' + str(id(self)), label=(str(self.op)))
            grafica.edge(nombrehijo, 'NodeE1' + str(id(self)))
            self.Exp1.graficarasc(nombrehijo, grafica)
        else:
            self.Exp1.graficarasc(nombrehijo, grafica)
            grafica.node('NodeE1' + str(id(self)), label=(str(self.op)))
            grafica.edge(nombrehijo, 'NodeE1' + str(id(self)))


class unario(Nodo.Nodo):
    def __init__(self,Exp,op,fila,col):
        self.fila=fila
        self.columna=col
        self.Exp=Exp
        self.op=op

    def getC3D(self,TS,Global,Traductor):
        codigo=""
        temp = Traductor.getTemp()
        codigo+=self.Exp.getC3D(TS,Global,Traductor)
        self.temporal=temp
        codigo+=temp+' = '+ str(self.op)+' '+self.Exp.temporal+'; \n'
        if TS is not None:
            TS.almacenados.append(temp)
        return codigo

    def graficarasc(self,padre,grafica):
        nombrehijo='Node'+str(id(self))
        grafica.node(nombrehijo,label=('Exp'))
        grafica.edge(padre,nombrehijo)
        grafica.node('NodeE1'+str(id(self)),label=(str(self.op)))
        grafica.edge(nombrehijo,'NodeE1'+str(id(self)))
        if self.Exp is not None:
            self.Exp.graficarasc(nombrehijo,grafica)



class ternario(Nodo.Nodo):
    def __init__(self,Cond,Exp1,Exp2,fila,col):
        self.fila=fila
        self.columna=col
        self.Cond=Cond
        self.Exp1=Exp1
        self.Exp2=Exp2

class sizeof(Nodo.Nodo):
    def __init__(self,Exp,fila,col):
        self.fila=fila
        self.columna=col
        self.Exp=Exp