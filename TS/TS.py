

class TablaDeSimbolos():
    def __init__(self,simbolos={}):
        self.simbolos=simbolos

    def add(self,simbolo):
        if simbolo.nombre in self.simbolos:
            print('error ya existe')
        else:
            self.simbolos[simbolo.nombre]= simbolo

    def get(self,nombre):
        if not nombre in self.simbolos:
            print('error')
        else:
            return self.simbolos[nombre]



