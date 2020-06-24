from tkinter import *
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import ttk
from tkinter.tix import ScrolledWindow
from tkinter.ttk import *
import Gramatica.Gramatica as g
import graphviz
import sys
import threading
#import Debbuger
#import Descendente as des
import Errores.N_Error as error
import Errores.L_Error as lista_err
from tkinter import colorchooser
from TS.TS import *
from AST.Declaracion import *
from AST.Funcion import *
from TS.Generador import *
if __name__=='__main__':
	from LineNumber import LineMain
	from Graphics import Tkinter
else:
	from .LineNumber import LineMain
	from .Graphics import Tkinter

class Connect:
	def __init__(self, pad):
		self.pad = pad
		self.modules_connections()


	def modules_connections(self):
		LineMain(self.pad)
		return

sys.setrecursionlimit(600000)
print(sys.getrecursionlimit())
threading.stack_size(250000000)
reporte_errores = error.N_Error("","","","")
class TextPad(Tkinter.Text):
	def __init__(self, *args, **kwargs):
		Tkinter.Text.__init__(self, *args, **kwargs)
		self.storeobj = {"Root": self.master}
		self.Connect_External_Module_Features()
		self._pack()

	def Connect_External_Module_Features(self):
		Connect(self)
		return

	def _pack(self):
		self.pack(expand = True, fill = "both")
		return

archivoactgual="v"

#creacion de ventana
window = Tk()
window.title("Angus Interpreter")
#window.configure(background='black')
window.geometry('1100x750')


txtarea=TextPad(window)


#txtarea = scrolledtext.ScrolledText(window,width=60, height=45)
#txtarea.grid(column=0, row=2,sticky=E)
consola = scrolledtext.ScrolledText(window,width=70, height=18)

#consola.grid(column=1, row=2,sticky=N)
debugger=ttk.Treeview(window)
lbl=Label(window,text="Consola de Salida")
lbl.pack(side=TOP, fill=X)
debugger["columns"]=("Nombre", "Tipo","Dimension","Rol")
debugger.column("#0", width=0, stretch=NO)
debugger.column("Nombre", width=150, minwidth=150, stretch=NO)
debugger.column("Tipo", width=50, minwidth=50)
debugger.column("Dimension", width=150, minwidth=150)
debugger.column("Rol", width=100, minwidth=100)
debugger.pack(side=RIGHT)
debugger.heading("#0", text="No", anchor=W)
debugger.heading("Nombre", text="Nombre", anchor=W)
debugger.heading("Tipo", text="Tipo", anchor=W)
debugger.heading("Dimension", text="Valor", anchor=W)
debugger.heading("Rol", text="Rol", anchor=W)
consola.pack(side=LEFT)


def imprimir(raiz):
    f = graphviz.Digraph(filename='Reporte_AST.gv')
    f.node('Node0',label='RAIZ')
    contador=1
    def recorrido(arbol,padre):
        nonlocal contador
        for x in arbol.childs:
            nombrehijo='Node'+str(contador)
            f.node(nombrehijo,label=str(x.tag)+' | '+str(x.value))
            f.edge(padre,nombrehijo)
            contador+=1
            if(len(x.childs)!=0):
                recorrido(x,nombrehijo)
    recorrido(raiz,'Node0')
    f.view()


def limpiar():
    txtarea.delete(1.0, END)
    archivoactgual = "v"


def abriarchivo():
    archivoactgual = "v"
    filename = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("All Files", "*.*")])
    if filename:
        archivoactgual = filename
        print(archivoactgual)
        txtarea.delete(1.0, END)
        with open(filename, "r") as f:
            txtarea.insert(1.0, f.read())


def guardar():
    print(archivoactgual)
    if archivoactgual == "v":
        print('entra aca')
        guardarcomo()
    else:
        print('entra')
        try:
            contenido = txtarea.get(1.0, END)
            with open(archivoactgual, "w") as f:
                f.write(contenido)
        except Exception as e:
            print(e)


def guardarcomo():
    try:
        nuevoarchivo = filedialog.asksaveasfilename(
            initialfile="Untitled.txt",
            defaultextension=".txt",
            filetypes=[("All Files", "*.*"),
                       ("Text Files", "*.txt"),
                       ("Python Scripts", "*.py"),
                       ("Markdown Documents", "*.md"),
                       ("JavaScript Files", "*.js"),
                       ("HTML Documents", "*.html"),
                       ("CSS Documents", "*.css")])
        contenido = txtarea.get(1.0, END)
        with open(nuevoarchivo, "w") as f:
            f.write(contenido)
    except Exception as e:
        print(e)


def analizar():

    consola.delete('1.0',END)
    input = txtarea.get(1.0, END)

    resultado = g.parse(input)
    print(resultado)
    f = graphviz.Digraph(filename='Reporte_AST.gv')
    f.node('Node0',label='RAIZ')
    for nodo in resultado:
        nodo.graficarasc('Node0',f)
    f.view()
    pila=TablaDeSimbolos("global")
    generador=Generador3D()
    codigo="main: \n" \
           "$s0 = array(); \n" \
           "$sp=1;\n"
    for nodo in resultado:
        if isinstance(nodo,Funcion):
            pila.agregarfunc(nodo)

    for nodo in resultado:
        if isinstance(nodo,Declaracion):
            codigo+=nodo.getC3D(None,pila,generador)

    consola.insert(INSERT,codigo)
    '''
        if interprete.errores.principio is not None:
        errores(interprete.errores.principio)
    else:
        imprimir(resultado)
        thread = threading.Thread(target=interprete.analizar, args=(resultado,))
        thread.start()
        thread.join()
        errores(interprete.errores.principio)

        TS(interprete.pila.obtenerreporte())
        consola.insert(INSERT, interprete.codigo)
    '''


def debbugear():
    debugger.delete(*debugger.get_children())
    consola.delete('1.0',END)
    input = txtarea.get(1.0,END)
    erris=lista_err.L_Error()
    resultado=g.parse(input,erris)
    global debbug
    if erris.principio is not None:
        errores(erris.principio)

    else:
        debbug = Debbuger.Debbugger(resultado,consola,txtarea,debugger)
        thread = threading.Thread(target=debbug.start)
        thread.start()
        thread.join()
        #errores(debbug.errores.principio)
        #TS(debbug.pila.obtenerreporte())


def TS(tupla):
    ventana= Toplevel(window)
    tree_errores = ttk.Treeview(ventana)
    tree_errores["columns"] = ("Nombre", "Tipo","Dimension","Declarada","Rol")
    tree_errores.grid(column=1, row=2, sticky=S)
    tree_errores.column("#0", width=0, stretch=NO)
    tree_errores.column("Nombre", width=50, minwidth=50, stretch=NO)
    tree_errores.column("Tipo", width=100, minwidth=100)
    tree_errores.column("Dimension", width=300, minwidth=300)
    tree_errores.column("Declarada", width=200, minwidth=200)
    tree_errores.column("Rol", width=100, minwidth=100)
    tree_errores.heading("#0", text="No", anchor=W)
    tree_errores.heading("Nombre", text="Nombre", anchor=W)
    tree_errores.heading("Tipo", text="Tipo", anchor=W)
    tree_errores.heading("Dimension", text="Valor", anchor=W)
    tree_errores.heading("Declarada", text="Declarada", anchor=W)
    tree_errores.heading("Rol", text="Rol", anchor=W)
    cuenta=1
    for x in tupla:
        tree_errores.insert("",cuenta,cuenta,values=x)
        cuenta+=1

def errores(reporte_errores):
    ventana= Toplevel(window)
    tree_errores = ttk.Treeview(ventana)
    tree_errores["columns"] = ("Tipo", "Descripcion","Fila","Columna")
    tree_errores.grid(column=1, row=2, sticky=S)
    tree_errores.column("#0", width=0, stretch=NO)
    tree_errores.column("Tipo", width=200, minwidth=200, stretch=NO)
    tree_errores.column("Descripcion", width=400, minwidth=400)
    tree_errores.column("Fila", width=100, minwidth=100)
    tree_errores.column("Columna", width=100, minwidth=100)
    tree_errores.heading("#0", text="No", anchor=W)
    tree_errores.heading("Descripcion", text="Descripcion", anchor=W)
    tree_errores.heading("Tipo", text="Tipo", anchor=W)
    tree_errores.heading("Fila", text="Fila", anchor=W)
    tree_errores.heading("Columna", text="Columna", anchor=W)

    if reporte_errores is not None:
        cuenta=1
        while reporte_errores is not None:
            tree_errores.insert("",cuenta,cuenta,values=(reporte_errores.tipo,reporte_errores.descripcion,str(reporte_errores.fila),str(reporte_errores.columna)))
            reporte_errores=reporte_errores.siguiente
            cuenta+=1
def siguiente():
    debbug.debbuger=False

def detener():
    debbug.detener=True
    txtarea.tag_delete("start")
    debugger.delete(*debugger.get_children())
menubar = Menu(window)
def descendente():
    consola.delete('1.0',END)
    input = txtarea.get(1.0,END)
    interprete = inter.Interprete()
    resultado = des.parse(input,interprete.errores)
    if interprete.errores.principio is not None:
        errores(interprete.errores.principio)
    else:
        imprimir(resultado)
        thread = threading.Thread(target=interprete.analizar, args=(resultado,))
        thread.start()
        thread.join()
        errores(interprete.errores.principio)
        TS(interprete.pila.obtenerreporte())
        consola.insert(INSERT, interprete.codigo)

def cambiarcolor():
    rgb_color, web_color = colorchooser.askcolor(parent=window,
                                                 initialcolor=(255, 0, 0))
    print(rgb_color)
    print(web_color)
    txtarea.config(background=web_color)
    consola.config(background=web_color)

def colorventana():
    rgb_color, web_color = colorchooser.askcolor(parent=window,
                                                 initialcolor=(255, 0, 0))
    window.config(background=web_color)
    lbl.config(background=web_color)
    menubar.config(background=web_color)

def colortexto():
    rgb_color, web_color = colorchooser.askcolor(parent=window,
                                                 initialcolor=(255, 0, 0))
    print(rgb_color)
    print(web_color)
    txtarea.config(fg=web_color)
    consola.config(fg=web_color)


window.config(menu=menubar)
archivo = Menu(menubar,tearoff=0)
archivo.add_command(label="Limpiar Pantalla",
                     command=limpiar)
archivo.add_separator()
archivo.add_command(label="Abrir Archivo",
                     command=abriarchivo)

archivo.add_separator()
archivo.add_command(label="Guardar",
                     command=guardar)
archivo.add_command(label="Guardar Como",
                     command=guardarcomo)
menubar.add_cascade(label="Archivo",menu=archivo)

ejecucioin = Menu(menubar,tearoff=0)
ejecucioin.add_command(label="Ejecutar Ascendente", command=analizar)
ejecucioin.add_separator()

ejecucioin.add_command(label="Debbuggear",command=debbugear)
ejecucioin.add_command(label="Siguiente",command=siguiente)
ejecucioin.add_command(label="Detener",command=detener)
ejecucioin.add_separator()
ejecucioin.add_command(label="Descendente",command=descendente)
menubar.add_cascade(label="Ejecucion",menu=ejecucioin)

opciones = Menu(menubar,tearoff=0)
opciones.add_command(label="Cambiar Color Consolas",command=cambiarcolor)
opciones.add_command(label="Cambiar Color Ventana",command=colorventana)
opciones.add_command(label="Cambiar Color Texto",command=colortexto)
menubar.add_cascade(label="Opciones",menu=opciones)
window.mainloop()