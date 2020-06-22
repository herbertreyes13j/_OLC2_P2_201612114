class N_Error:
    def __init__(self,tipo,descripcion,fila,columna):
        self.tipo=tipo
        self.descripcion=descripcion
        self.fila=fila
        self.columna=columna
        self.siguiente=None
        self.anterior=None

    def totext(self):
        texto=''
        texto+='\nERROR---> Tipo: '+self.tipo
        texto+=', Descripcion: ' + self.descripcion
        texto+=', Fila: '+str(self.fila)
        texto+=', Columna: '+str(self.columna)+'\n'
        return texto