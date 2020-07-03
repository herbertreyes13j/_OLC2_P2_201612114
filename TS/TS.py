from AST.Funcion import Funcion

class TablaDeSimbolos():
    def __init__(self,ambito):
        self.size=1
        self.nombre=ambito
        self.tmp = 0
        self.etq = 0
        self.funciones={}
        self.escape=[]
        self.continuel=[]
        self.cuentatrad=0
        self.reporteTS=[]
        self.salida=""
        self.almacenados=[]
        self.tmp=0
        self.etiquetas=0
        self.simbolos=[]
        self.cuentafun=1
        self.parametros=0
        self.structs={}


    def insercont(self,etq):
        self.continuel.append(etq)

    def getlastcont(self):
        return self.continuel[len(self.continuel)-1]
    def popc(self):
        self.continuel.pop()

    def inseres(self,etq):
        self.escape.append(etq)

    def getlastes(self):
        return self.escape[len(self.escape)-1]

    def popes(self):
        self.escape.pop()

    def reiniciar(self):
        self.size=1
        self.inicio=None
        self.fin=None

    def push(self,nuevo):
        if self.existe(nuevo.nombre):
            return False
        self.simbolos.insert(0,nuevo)
        return True

    def pop(self):
        if self.size==1:
            return None
        devolver=self.fin
        self.fin=self.fin.anterior
        if self.fin is None:
            self.inicio=None
        self.size-=1
        return devolver

    def vaciarPila(self):
        while not self.fin.nombre=='$$' and not self.fin.nombre =="$":
            aux = self.pop()
        self.pop()

    def existe(self,nombre):
        for variable in self.simbolos:
            if variable.nombre==nombre and variable.ambito==self.nombre:
                return True

    def obtener(self,nombre):
        for simbolo in self.simbolos:
            if simbolo.nombre==nombre and (simbolo.ambito==self.nombre or simbolo.ambito=='global'):
                return simbolo
        return None

    def agregarstruct(self,struct):
        if struct.nombre in self.structs:
            return False
        self.structs[struct.nombre]=struct
        return True

    def obtenerstruct(self,nombre):
        if not nombre in self.structs:
            return None
        return self.structs[nombre]

    def existestruct(self,nombre):
        if not nombre in self.structs:
            return True
        return False

    def agregarfunc(self,funcion):
        if funcion.nombre in self.funciones:
            return False
        self.funciones[funcion.nombre]=funcion
        return True


    def obtenerfunc(self,nombre):
        if not nombre in self.funciones:
            print('Error')
            return None
        return self.funciones[nombre]

    def obtenertrad(self,nombre):
        if not nombre in self.traducidas:
            print('error')
            return None
        return self.traducidas[nombre]

    def agregarcodigo(self,codigo):
        self.codigofinal+=codigo

    def obtenerreporte(self):
        tupla=[]
        for muestra in self.reporteTS:
            tupla.append((muestra.tipo,muestra.nombre,muestra.posicion,muestra.ambito,muestra.dimensiones))
        return tupla

    def getTemp(self):
        temp = self.tmp
        self.tmp += 1
        return "$t" + str(temp)
    def getParametro(self):
        para = self.parametros
        self.parametros += 1
        return "$a" + str(para)

    def changestack(self,pos, valor):
        return "$s0[" + str(pos) + "] = " + str(valor) + ";\n"

    def getfromStack(self,destino,pos):
        return str(destino) + " = $s0[" + str(pos) + "];\n"

    def getfromP(self,destino,pos):
        return str(destino) + "= $sp+" + str(pos) + ";\n"

    def make3d(self,asignacion,ins1,op,ins2):
        return str(asignacion) + " = " + str(ins1) + " " + str(op) + " " + str(ins2) + ";\n"

    def makecomentario(self,comentario):
        return "#" + comentario + "\n"

    def getEtq(self):
        etiqueta = self.etiquetas
        self.etiquetas+=1
        return "L" + str(etiqueta)

    def incP(self,incremento):
        return '$sp=$sp + ' + str(incremento) + ';\n'

    def decP(self,decremento):
        return '$sp=$sp - ' + str(decremento) + ';\n'






