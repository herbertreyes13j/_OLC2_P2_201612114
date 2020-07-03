from enum import Enum

class OPERACION_ARITMETICA(Enum) :
    MAS = 1
    MENOS = 2
    MULTI = 3
    DIVIDIDO = 4
    RESIDUO = 5

class OPERACION_LOGICA(Enum) :
    AND = 1
    OR = 2
    XOR = 3

class OPERACION_RELACIONAL(Enum) :
    IGUALQUE = 1
    DISTINTO = 2
    MAYORIGUAL = 3
    MENORIGUAL = 4
    MAYORQUE = 5
    MENORQUE = 6

class OPERACION_BIT_A_BIT(Enum) :
    AND = 1
    OR = 2
    XOR = 3
    SHIFT_IZQ = 4
    SHIFT_DER = 5
    
class TIPO_VARIABLE(Enum) :
    TEMPORAL = 1 
    PARAMETRO = 2
    VALOR_DEV_FUN = 3
    RA = 4
    STACK = 5
    SP = 6

class TIPO_DATO(Enum) :
    ENTERO = 1
    FLOTANTE = 2
    CADENA = 3
    ARREGLO = 4
    CHAR = 5




#------------------------------------------------------------------------

class Casteo() :
    def __init__(self,tipo_dato,variable) :
        self.tipo_dato = tipo_dato
        self.variable = variable
    def Optimizar(self,Reporte,Padre):
        if self.tipo_dato==TIPO_DATO.CHAR:
            tipo="char"
        elif self.tipo_dato==TIPO_DATO.ENTERO:
            tipo="int"
        elif self.tipo_dato==TIPO_DATO.FLOTANTE:
            tipo="float"
        return Padre+'= ('+tipo+')'+self.variable.Optimizar(Reporte,Padre)+';\n'

#------------------------------------------------------------------------

class UnitariaNegAritmetica() :
    def __init__(self, exp) :
        self.exp = exp
    def Optimizar(self,Reporte,Padre):
        codigo=''
        codigo+='-'
        codigo+=self.exp.Optimizar(Reporte,Padre)
        return codigo
class UnitariaLogicaNOT() :
    def __init__(self, expresion):
        self.expresion=expresion
    def Optimizar(self,Reporte,Padre):
        return '!'+self.expresion.Optimizar(Reporte,Padre)

class UnitariaNotBB() :
    def __init__(self, expresion):
        self.expresion=expresion
    def Optimizar(self,Reporte,Padre):
        return '~'+self.expresion.Optimizar(Reporte,Padre)
class UnariaReferencia() :
    def __init__(self,tipoVar):
        self.tipoVar=tipoVar
    def Optimizar(self,Reporte,Padre):
        return '&'+self.tipoVar
#------------------------------------------------------------------------
import abc
class Expresion(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Optimizar(self,Reporte,Padre):
        pass

class Parametro(Expresion) :
    def __init__(self, expresion) :
        self.expresion=expresion
    def Optimizar(self,Reporte,Padre):
        return self.expresion.Optimizar(Reporte,Padre)
class Variable(Expresion) :
    
    def __init__(self, id, tipoVar) :
        self.id=id
        self.tipoVar=tipoVar
    def Optimizar(self,Reporte,Padre):
        return self.id

class ExpresionValor(Expresion) :

    def __init__(self, val = 0) :
        self.val = val
    def Optimizar(self,Reporte,Padre):
        return str(self.val)

class AccesoArray(Expresion) :
    def __init__(self,tipoVar,params=[]) :
        self.tipoVar=tipoVar
        self.params=params
    def Optimizar(self,Reporte,Padre):
        codigo=self.tipoVar.Optimizar(Reporte,Padre)
        for nodon in self.params:
            codigo+='['+nodon.Optimizar(Reporte,Padre)+']'
        return codigo
#------------------------------------------------------

class ExpresionAritmetica(Expresion) :
   
    def __init__(self, exp1, exp2, operador) :
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador
    def Optimizar(self,Reporte,Padre):
        tipo1 = self.exp1.Optimizar(Reporte, Padre)
        tipo2 = self.exp2.Optimizar(Reporte, Padre)
        if self.operador==OPERACION_ARITMETICA.MAS:
            if tipo1 == '0':
                if tipo2 == Padre:
                    codigo = 'Regla 8: Eliminacion de forma x = x+0\n'
                    codigo += Padre+'=' +tipo1 + '+' + tipo2 + '\n'
                    Reporte.append(codigo)
                    return ""
                else:
                    codigo = 'Regla 12: Eliminacion de forma x = y + 0; \n'
                    codigo += Padre+'='+tipo1 + '+' + tipo2 + '\n'
                    Reporte.append(codigo)
                    return Padre+'='+tipo2+';\n'
            elif tipo2=='0':
                if tipo1 == Padre:
                    codigo = 'Regla 8: Eliminacion de forma x = x+0\n'
                    codigo += Padre + '=' + tipo1 + '+' + tipo2 + '\n'
                    Reporte.append(codigo)
                    return ""
                else:
                    codigo = 'Regla 12: Eliminacion de forma x = y + 0; \n'
                    codigo += Padre + '=' + tipo1 + '+' + tipo2 + '\n'
                    Reporte.append(codigo)
                    return Padre+'='+ tipo1+';\n'
            else:
                return Padre+'='+tipo1+'+'+tipo2+';\n'
        elif self.operador==OPERACION_ARITMETICA.MENOS:
            if tipo2 == '0':
                if tipo1 == Padre:
                    codigo = 'Regla 9: Eliminacion de forma x = x-0\n'
                    codigo += Padre + '=' + tipo1 + '-' + tipo2 + '\n'
                    Reporte.append(codigo)
                    return ""
                else:
                    codigo = 'Regla 13: Eliminacion de forma x = y - 0; \n'
                    codigo += Padre + '=' + tipo1 + '-' + tipo2 + '\n'
                    Reporte.append(codigo)
                    return Padre + '=' + tipo1 + ';\n'
            else:
                return Padre+'='+tipo1+'-'+tipo2+';\n'
        elif self.operador==OPERACION_ARITMETICA.MULTI:
            if tipo1 == '1':
                if tipo2 == Padre:
                    codigo = 'Regla 10: Eliminacion de forma x = x*1\n'
                    codigo += Padre+'=' +tipo1 + '*' + tipo2 + '\n'
                    Reporte.append(codigo)
                    return ""
                else:
                    codigo = 'Regla 14: Eliminacion de forma x = y * 1; \n'
                    codigo += Padre+'='+tipo1 + '*' + tipo2 + '\n'
                    Reporte.append(codigo)
                    return Padre+'='+tipo2+';\n'
            elif tipo2=='1':
                if tipo1 == Padre:
                    codigo = 'Regla 10: Eliminacion de forma x = x*1\n'
                    codigo += Padre + '=' + tipo1 + '*' + tipo2 + '\n'
                    Reporte.append(codigo)
                    return ""
                else:
                    codigo = 'Regla 14: Eliminacion de forma x = y * 1; \n'
                    codigo += Padre + '=' + tipo1 + '*' + tipo2 + '\n'
                    Reporte.append(codigo)
                    return Padre+'='+ tipo1+';\n'
            elif tipo1 == '0' or tipo2 == '0':
                codigo = 'Regla 17: Optimizacion Tipo x = y * 0\n'
                codigo += Padre + '=' + tipo1 + '*' + tipo2 + ';\n'
                Reporte.append(codigo)
                return Padre + ' = 0;\n'
            elif tipo1=='2':
                    codigo='Regla 16: Optimizacion Tipo x= y *2\n'
                    codigo+=Padre+'='+tipo1+'*'+tipo2+'\n'
                    Reporte.append(codigo)
                    return Padre+'='+tipo2+'+'+tipo2+';\n'
            elif tipo2=='2':
                    codigo = 'Regla 16: Optimizacion Tipo x= y *2\n'
                    codigo += Padre + '=' + tipo1 + '*' + tipo2 + '\n'
                    Reporte.append(codigo)
                    return Padre + '=' + tipo1 + '+' + tipo1 + ';\n'
            else:
                return Padre+'='+tipo1+'*'+tipo2+';\n'
        elif self.operador == OPERACION_ARITMETICA.DIVIDIDO:
            if tipo2 == '1':
                if tipo1==Padre:
                    codigo='Regla 11 : Eliminacion instruccion x = x / 1\n'
                    codigo+=Padre+'='+tipo1+'/'+tipo2+';\n'
                    Reporte.append(codigo)
                    return ""
                else:
                    codigo = 'Regla 15: Optimizacion tipo x = y / 1\n'
                    codigo += Padre + '=' + tipo1 + '/' + tipo2 + ';\n'
                    Reporte.append(codigo)
                    return Padre+'='+tipo1+';\n'
            elif tipo1=='0':
                codigo = 'Regla 18: Optimizacion de instruccion x = 0 /y ;\n'
                codigo += Padre + '=' + tipo1 + '/' + tipo2 + ';\n'
                Reporte.append(codigo)
                return Padre + '= 0;\n'
            else:
                return Padre+'='+tipo1+'/'+tipo2+';\n'
        elif self.operador==OPERACION_ARITMETICA.RESIDUO:
            return Padre+'='+tipo1+'%'+tipo2+';\n'



#------------------------------------------------------

class ExpresionLogica(Expresion) :
    
    def __init__(self, exp1, exp2, operador) :
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador
    def Optimizar(self,Reporte,Padre):
        tipo1=self.exp1.Optimizar(Reporte,Padre)
        tipo2=self.exp2.Optimizar(Reporte,Padre)
        if self.operador==OPERACION_LOGICA.AND:
            op="&&"
        elif self.operador==OPERACION_LOGICA.OR:
            op="||"
        elif self.operador==OPERACION_LOGICA.XOR:
            op="xor"
        if Padre=='mady':
            return tipo1+op+tipo2
        return Padre+'='+tipo1+op+tipo2+';\n'
#------------------------------------------------------
class ExpresionRelacional(Expresion) :

    def __init__(self,exp1,exp2,operador) :
        self.exp1=exp1
        self.exp2=exp2
        self.operador=operador
    def Optimizar(self,Reporte,Padre):
        tipo1 = self.exp1.Optimizar(Reporte, Padre)
        tipo2 = self.exp2.Optimizar(Reporte, Padre)
        if self.operador == OPERACION_RELACIONAL.DISTINTO:
            op = "!="
        elif self.operador == OPERACION_RELACIONAL.IGUALQUE:
            op = "=="
        elif self.operador == OPERACION_RELACIONAL.MAYORIGUAL:
            op = ">="
        elif self.operador == OPERACION_RELACIONAL.MENORIGUAL:
            op = "<="
        elif self.operador == OPERACION_RELACIONAL.MAYORQUE:
            op = ">"
        elif self.operador == OPERACION_RELACIONAL.MENORQUE:
            op = "<"
        if Padre=='mady':
            return tipo1+op+tipo2
        return Padre + '=' + tipo1 + op + tipo2 + ';\n'
#------------------------------------------------------
class ExpresionBitABit(Expresion) :

    def __init__(self,exp1,exp2,operador) :
        self.exp1=exp1
        self.exp2=exp2
        self.operador=operador

    def Optimizar(self, Reporte, Padre):
        tipo1 = self.exp1.Optimizar(Reporte, Padre)
        tipo2 = self.exp2.Optimizar(Reporte, Padre)
        if self.operador == OPERACION_BIT_A_BIT.XOR:
            op = "^"
        elif self.operador == OPERACION_BIT_A_BIT.OR:
            op = "|"
        elif self.operador == OPERACION_BIT_A_BIT.AND:
            op = "&"
        elif self.operador == OPERACION_BIT_A_BIT.SHIFT_IZQ:
            op = "<<"
        elif self.operador == OPERACION_BIT_A_BIT.SHIFT_DER:
            op = ">>"

        if Padre=='mady':
            return tipo1+op+tipo2
        return Padre + '=' + tipo1 + op + tipo2 + ';\n'