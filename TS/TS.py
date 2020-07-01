from AST.Funcion import Funcion

class TablaDeSimbolos():
    def __init__(self,ambito):
        self.size=1
        self.inicio=None
        self.fin=None
        self.nombre=ambito
        self.tmp = 0
        self.etq = 0
        self.funciones={}
        self.escape=[]
        self.continuel=[]
        self.traducidas=[]
        self.cuentatrad=0
        self.codigofinal="retorno_final:\n"
        self.reporteTS=[]
        self.salida=""
        self.almacenados=[]


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
        if self.inicio is None:
            self.inicio=nuevo
            self.fin=nuevo
            self.size+=1
            return True
        nuevo.anterior=self.fin
        self.fin.siguiente=nuevo
        self.fin=nuevo
        self.size+=1
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
        if nombre == "$$" or nombre == "$":
            return False;
        actual = self.fin;

        while actual is not None:
            if actual.nombre == nombre:
                return True
            if actual.nombre=="$$":
                return  False
            actual=actual.anterior
        return False

    def obtener(self,nombre):
        actual=self.fin

        if actual is None: return None

        while actual is not None:
            if actual.nombre==nombre:
                return actual
            actual=actual.anterior
        return None


    def buscarglobal(self,nombre):
        actual=self.inicio
        if actual=='$$':
            actual=actual.siguiente

        while actual is not None:
            if actual.nombre=='$$' or actual.nombre=='$':
                return None
            elif actual.nombre ==nombre:
                return actual
            actual=actual.siguiente

        return None

    def agregarfunc(self,funcion):
        self.funciones[funcion.nombre]=funcion

    def agregartrad(self,nombre):
        self.traducidas.append(nombre)

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






