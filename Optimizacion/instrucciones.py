import abc
from Optimizacion.expresiones import *
class Instruccion(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Optimizar(self,Reporte,Padre):
        pass

class Print(Instruccion) :

    def __init__(self,  valor) :
        self.valor = valor

    def Optimizar(self,Reporte,Padre):
        return 'print('+self.valor.Optimizar(Reporte,Padre)+');\n'

class GoTo(Instruccion) :
    
    def __init__(self,  id) :
        self.id = id
    def Optimizar(self,Reporte,Padre):
        return 'goto '+self.id+';\n'
class Etiqueta(Instruccion) :
    
    def __init__(self, id, instrucciones=[]) :
        self.id = id
        self.instrucciones=instrucciones
    def Optimizar(self,Reporte,Padre):
        return self.id+':\n'


class ExitInstruccion(Instruccion) :
    
    def __init__(self):
        pass
    def Optimizar(self,Reporte,Padre):
        return 'exit;\n'

class Unset(Instruccion) :

    def __init__(self, id) :
        self.id = id
    def Optimizar(self,Reporte,Padre):
        return 'unset('+self.id+');\n'

class Read(Instruccion) :
    
    def __init__(self) :
        pass
    def Optimizar(self,Reporte,Padre):
        return 'read()'

class Absoluto(Instruccion) :
   
    def __init__(self, variable) :
        self.variable=variable
    def Optimizar(self,Reporte,Padre):
        return 'abs('+self.variable.Optimizar(Reporte,Padre)+')'

class Array(Instruccion) :
   
    def __init__(self,id) :
        self.id=id
    def Optimizar(self,Reporte,Padre):
        return self.id.Optimizar(Reporte,Padre)+'=array();\n'
class DeclaracionAsignacion(Instruccion) :

    def __init__(self, variable, valor) :
        self.id = variable
        self.valor = valor
    def Optimizar(self,Reporte,Padre):
        return ""
class AsignacionArrSt(Instruccion) :
    
    def __init__(self, variable,indices, valor) :
        self.variable = variable
        self.indices = indices
        self.valor = valor
    def Optimizar(self,Reporte,Padre):
        codigo=self.variable.Optimizar(Reporte,Padre)
        for nodo in self.indices:
            codigo+='['+nodo.Optimizar(Reporte,Padre)+']'
        if isinstance(self.valor,ExpresionValor) or isinstance(self.valor,Variable) or isinstance(self.valor,AccesoArray):
            return codigo+'='+self.valor.Optimizar(Reporte,Padre)+';\n'
        else:
            return self.valor.Optimizar(Reporte,codigo)

class Asignacion(Instruccion) :
    
    def __init__(self,  variable, valor) :
        self.variable = variable
        self.valor = valor
    def Optimizar(self,Reporte,Padre):
        codigo=self.variable.Optimizar(Reporte,Padre)
        if isinstance(self.valor,ExpresionValor) or isinstance(self.valor,Variable) or isinstance(self.valor,AccesoArray):
            return codigo+'='+self.valor.Optimizar(Reporte,codigo)+';\n'
        else:
            return self.valor.Optimizar(Reporte,codigo)

class If(Instruccion) : 
    def __init__(self, expLogica, instrucciones = []) :
        self.expLogica = expLogica
        self.instrucciones = instrucciones
    def Optimizar(self,Reporte,Padre):
        codigo='if('+self.expLogica.Optimizar(Reporte,"mady")+') '
        codigo+=self.instrucciones.Optimizar(Reporte,Padre)
        return codigo



