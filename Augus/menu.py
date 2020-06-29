

#==============================================================

#==============================================================
from .instrucciones import *
from .ts import *
from tkinter import *
import Augus.interprete as Inter
import Augus.gramatica as G
pathFile=''
comando_consola=''
ts_debug=TablaDeSimbolos()
no_instruccion=0
ejecucion_automatica=1
cajaPrincipal=Tk()
leftBOTTOM=Frame(cajaPrincipal)
leftBOTTOM.pack(side=RIGHT)
editor = Text(leftBOTTOM)


def ejec_ascendente(consolas,texto):
    global ts_debug, no_instruccion, waitForCommand, ejecucion_automatica
    ejecucion_automatica=1
    waitForCommand=0
    Inter.inicializarGUI(editor,consolas)
    Inter.limpiarValores()
    Inter.inicializarEjecucionAscendente(texto)
    Inter.inicializarTS()
    i=0
    while i<len(Inter.instrucciones):
        if waitForCommand==0 or waitForCommand==2: #0=Sin Entrada, 1=Esperando, 2=Comando Ingresado
            if i<len(Inter.instrucciones) :
                is_asig=Inter.instrucciones[i]
                if isinstance(is_asig,Asignacion): 
                    # COMANDO PARA LEER DE CONSOLA
                    if isinstance(is_asig.valor,Read) and waitForCommand==0:
                        waitForCommand=1
                        no_instruccion=i
                        return None
                #EJECUTAR INSTRUCCION
                instr_temp=Inter.ejecutarInstruccionUnitaria(1,i)
                if instr_temp is not None:
                    if instr_temp==-10 : # EXIT
                        i=len(Inter.instrucciones)
                    else: #GOTO
                        i=instr_temp
                waitForCommand=0
            else:
                pass
                #MessageBox.showinfo("Finalizado","Ultima instruccion ejecutada.")
        i=i+1
    #Inter.generarReportes()
