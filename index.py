from tkinter import *
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import ttk
from tkinter.ttk import *
import Gramatica.Gramatica as g
import graphviz
import sys
import threading
import Errores.N_Error as error
import Errores.L_Error as lista_err
from tkinter import colorchooser
from TS.TS import *
from AST.Declaracion import *
from AST.Funcion import *
from TS.Generador import *
from AST.Asignacion import *
from AST.Arreglo_Simple import *
import Augus.menu as augus

if __name__=='__main__':
    from LineNumber import LineMain
    from Graphics import Tkinter
    from ColorLight import ColorLight
else:
    from .LineNumber import LineMain
    from .Graphics import Tkinter
    from .ColorLight import ColorLight

class Connect:
    def __init__(self, pad):
        self.pad = pad
        self.modules_connections()

    def modules_connections(self):
        LineMain(self.pad)
        ColorLight(self.pad)
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

class interfaz:

    def __init__(self):
        self.window=Tk()
        self.window.title("Minor C Interpreter")
        self.window.geometry('1100x750')
        self.archivoactgual=''
        self.txtarea=TextPad(self.window)
        self.consola = scrolledtext.ScrolledText(self.window,width=70, height=18)
        self.debugger=ttk.Treeview(self.window)
        lbl=Label(self.window,text="Consola de Salida")
        lbl.pack(side=TOP, fill=X)
        self.debugger["columns"]=("Nombre", "Tipo","Dimension","Rol")
        self.debugger.column("#0", width=0, stretch=NO)
        self.debugger.column("Nombre", width=150, minwidth=150, stretch=NO)
        self.debugger.column("Tipo", width=50, minwidth=50)
        self.debugger.column("Dimension", width=150, minwidth=150)
        self.debugger.column("Rol", width=100, minwidth=100)
        self.debugger.pack(side=RIGHT)
        self.debugger.heading("#0", text="No", anchor=W)
        self.debugger.heading("Nombre", text="Nombre", anchor=W)
        self.debugger.heading("Tipo", text="Tipo", anchor=W)
        self.debugger.heading("Dimension", text="Valor", anchor=W)
        self.debugger.heading("Rol", text="Rol", anchor=W)
        self.consola.pack(side=LEFT)
        self.menubar = Menu(self.window)
        self.window.config(menu=self.menubar)
        archivo = Menu(self.menubar, tearoff=0)
        archivo.add_command(label="Limpiar Pantalla",
                            command=self.limpiar)
        archivo.add_separator()
        archivo.add_command(label="Abrir Archivo",
                            command=self.abriarchivo)
        archivo.add_separator()
        archivo.add_command(label="Guardar",
                            command=self.guardar)
        archivo.add_command(label="Guardar Como",
                            command=self.guardarcomo)
        self.menubar.add_cascade(label="Archivo", menu=archivo)
        ejecucioin = Menu(self.menubar, tearoff=0)
        ejecucioin.add_command(label="Ejecutar Ascendente", command=self.analizar)
        ejecucioin.add_separator()
        ejecucioin.add_command(label="Debbuggear", command=self.debbugear)
        ejecucioin.add_command(label="Siguiente", command=self.siguiente)
        ejecucioin.add_command(label="Detener", command=self.detener)
        ejecucioin.add_separator()
        ejecucioin.add_command(label="Descendente", command=self.descendente)
        self.menubar.add_cascade(label="Ejecucion", menu=ejecucioin)
        reportes= Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label="Reportes",menu=reportes)
        opciones = Menu(self.menubar, tearoff=0)
        opciones.add_command(label="Cambiar Color Consolas", command=self.cambiarcolor)
        opciones.add_command(label="Cambiar Color Ventana", command=self.colorventana)
        opciones.add_command(label="Cambiar Color Texto", command=self.colortexto)
        self.menubar.add_cascade(label="Opciones", menu=opciones)
        self.window.mainloop()

    def imprimir(self,raiz):
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


    def limpiar(self):
        self.txtarea.delete(1.0, END)
        self.archivoactgual = "v"


    def abriarchivo(self):
        filename = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("All Files", "*.*")])
        if filename:
            self.archivoactgual = filename
            self.txtarea.delete(1.0, END)
            with open(filename, "r") as f:
                self.txtarea.insert(1.0, f.read())


    def guardar(self):
        if self.archivoactgual == '':
            filename = filedialog.askopenfilename(
                defaultextension=".txt",
                filetypes=[("All Files", "*.*")])
        else:
            filename=self.archivoactgual
        if filename:
            try:
                contenido = self.txtarea.get(1.0, END)
                with open(filename, "w") as f:
                    f.write(contenido)
            except Exception as e:
                print(e)


    def guardarcomo(self):
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
            contenido = self.txtarea.get(1.0, END)
            with open(nuevoarchivo, "w") as f:
                f.write(contenido)
        except Exception as e:
            print(e)


    def analizar(self):

        self.consola.delete('1.0',END)
        input = self.txtarea.get(1.0, END)
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
            if isinstance(nodo,Declaracion) or isinstance(nodo,AsignacionOp) or isinstance(nodo,ArregloSimple):
                codigo+=nodo.getC3D(None,pila,generador)

        funcion=pila.obtenerfunc('main')
        codigo+=funcion.getC3D(TablaDeSimbolos("main"),pila,generador)
        codigo+='exit;\n'
        codigo+=pila.codigofinal
        self.consola.insert(INSERT,codigo)
        #self.consola.delete('1.0', END)
        augus.ejec_ascendente(self.consola,codigo)
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


    def debbugear(self):
        self.debugger.delete(*self.debugger.get_children())
        self.consola.delete('1.0',END)
        input = self.txtarea.get(1.0,END)
        erris=lista_err.L_Error()
        resultado=g.parse(input,erris)
        global debbug
        if erris.principio is not None:
            self.errores(erris.principio)

        else:
            debbug = self.Debbuger.Debbugger(resultado,self.consola,self.txtarea,self.debugger)
            thread = threading.Thread(target=debbug.start)
            thread.start()
            thread.join()
            #errores(debbug.errores.principio)
            #TS(debbug.pila.obtenerreporte())


    def TS(tupla):
        ventana= Toplevel(self.window)
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

    def errores(self,reporte_errores):
        ventana= Toplevel(self.window)
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

        if self.reporte_errores is not None:
            cuenta=1
            while reporte_errores is not None:
                tree_errores.insert("",cuenta,cuenta,values=(reporte_errores.tipo,reporte_errores.descripcion,str(reporte_errores.fila),str(reporte_errores.columna)))
                reporte_errores=reporte_errores.siguiente
                cuenta+=1
    def siguiente(self):
        self.debbug.debbuger=False

    def detener(self):
        self.debbug.detener=True
        self.txtarea.tag_delete("start")
        self.debugger.delete(*self.debugger.get_children())
    def descendente(self):
        self.consola.delete('1.0',END)
        input = self.txtarea.get(1.0,END)
        interprete = self.inter.Interprete()
        resultado = self.des.parse(input,interprete.errores)
        if interprete.errores.principio is not None:
            self.errores(interprete.errores.principio)
        else:
            self.imprimir(resultado)
            thread = threading.Thread(target=interprete.analizar, args=(resultado,))
            thread.start()
            thread.join()
            self.errores(interprete.errores.principio)
            self.TS(interprete.pila.obtenerreporte())
            self.consola.insert(INSERT, interprete.codigo)

    def cambiarcolor(self):
        rgb_color, web_color = colorchooser.askcolor(parent=self.window,
                                                     initialcolor=(255, 0, 0))
        print(rgb_color)
        print(web_color)
        self.txtarea.config(background=web_color)
        self.consola.config(background=web_color)

    def colorventana(self):
        rgb_color, web_color = colorchooser.askcolor(parent=self.window,
                                                     initialcolor=(255, 0, 0))
        self.window.config(background=web_color)
        self.lbl.config(background=web_color)
        self.menubar.config(background=web_color)

    def colortexto(self):
        rgb_color, web_color = colorchooser.askcolor(parent=self.window,
                                                     initialcolor=(255, 0, 0))
        print(rgb_color)
        print(web_color)
        self.txtarea.config(fg=web_color)
        self.consola.config(fg=web_color)



interfaz()