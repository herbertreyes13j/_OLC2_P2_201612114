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

    def obtenerfunc(self,nombre):
        if not nombre in self.funciones:
            print('Error')

        return self.funciones[nombre]





