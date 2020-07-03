

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



def ejec_ascendente(consolas,texto,editores):
    global ts_debug, no_instruccion, waitForCommand, ejecucion_automatica
    consolas.bind("<Return>", comando_ingresado)
    ejecucion_automatica=1
    waitForCommand=0
    Inter.inicializarGUI(editores,consolas)
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

def continuar_ejecucionAsc():
    global no_instruccion, waitForCommand

    while no_instruccion<len(Inter.instrucciones):
        if waitForCommand==0 or waitForCommand==2: #0=Sin Entrada, 1=Esperando, 2=Comando Ingresado
            if no_instruccion<len(Inter.instrucciones) :
                is_asig=Inter.instrucciones[no_instruccion]
                if isinstance(is_asig,Asignacion):
                    # COMANDO PARA LEER DE CONSOLA
                    if isinstance(is_asig.valor,Read) and waitForCommand==0:
                        waitForCommand=1
                        #no_instruccion=i
                        return None
                #EJECUTAR INSTRUCCION
                instr_temp=Inter.ejecutarInstruccionUnitaria(1,no_instruccion)
                if instr_temp is not None:
                    if instr_temp==-10 : # EXIT
                        no_instruccion=len(Inter.instrucciones)
                    else: #GOTO
                        no_instruccion=instr_temp
                waitForCommand=0
                no_instruccion+=1
            else:
                pass
                #MessageBox.showinfo("Finalizado","Ultima instruccion ejecutada.")

def comando_ingresado(event):
    #consola.insert("end","\n>>")
    global waitForCommand
    waitForCommand=2
    if ejecucion_automatica == 1:
        continuar_ejecucionAsc()
    elif ejecucion_automatica == 2:
        pass