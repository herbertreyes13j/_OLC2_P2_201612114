class Generador3D:
    def __init__(self):
        self.tmp=0
        self.etiquetas=0


    def getTemp(self):
        temp = self.tmp
        self.tmp += 1
        return "$t" + str(temp)

    def changestack(self,pos, valor):
        return "$s0[" + str(pos) + "] = " + str(valor) + ";\n"

    def getfromStack(self,destino,pos):
        return str(destino) + " = $s0[" + str(pos) + "];\n"

    def getfromP(self,destino,pos):
        return str(destino) + "= $sp+" + str(pos) + ";\n"

    def make3d(self,asignacion,ins1,op,ins2):
        return str(asignacion) + " = " + str(ins1) + " " + str(op) + " " + str(ins2) + ";\n"
