import webbrowser
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
from AST.Asignacion import *
from AST.Arreglo_Simple import *
from AST.Arreglo import *
from AST.Struct import *
import Augus.menu as augus
import Optimizacion.gramatica as gramaticaop
import Optimizacion.instrucciones as instop
new = 2
head_html = '''
<head> 
       <style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
    </style>
</head>
'''

if __name__=='__main__':
    from LineNumber import LineMain
    from Graphics import Tkinter
    from ColorLight import ColorLight
    from ColorLight2 import ColorLight2
else:
    from .LineNumber import LineMain
    from .Graphics import Tkinter
    from .ColorLight import ColorLight
    from .ColorLight2 import ColorLight2

class Connect:
    def __init__(self, pad):
        self.pad = pad
        self.modules_connections()

    def modules_connections(self):
        LineMain(self.pad)
        ColorLight(self.pad)
        return

class Connect2:
    def __init__(self, pad):
        self.pad = pad
        self.modules_connections()

    def modules_connections(self):
        ColorLight2(self.pad)
        return

sys.setrecursionlimit(600000)
print(sys.getrecursionlimit())
threading.stack_size(250000000)

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
class TextPad2(Tkinter.Text):
    def __init__(self, *args, **kwargs):
        Tkinter.Text.__init__(self, *args, **kwargs)
        self.storeobj = {"Root": self.master}
        self.Connect_External_Module_Features()
        self._pack()

    def Connect_External_Module_Features(self):
        Connect2(self)
        return

    def _pack(self):
        self.pack(expand = True, fill = "both")
        return

class interfaz:

    def __init__(self):
        self.window=Tk()
        self.resultado=None
        self.window.title("Minor C Interpreter")
        self.window.geometry('1100x750')
        self.archivoactgual=''
        self.txtarea=TextPad(self.window)
        self.consola = scrolledtext.ScrolledText(self.window,width=70, height=18)
        lbl=Label(self.window,text="Consola de Salida")
        lbl.pack(side=TOP, fill=X)
        self.consola.pack(side=LEFT)
        self.menubar = Menu(self.window)
        self.window.config(menu=self.menubar)
        self.reporteg=[]
        self.errores=lista_err.L_Error()
        self.TS=TablaDeSimbolos("MUERE")
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

        self.menubar.add_cascade(label="Ejecucion", menu=ejecucioin)
        reportes= Menu(self.menubar,tearoff=0)
        reportes.add_command(label="Reporte AST",command=self.imprimir)
        reportes.add_command(label='Reporte Gramatica',command=self.reporte_gramatica)
        reportes.add_command(label='Reporte Errores', command=self.errores_r)
        reportes.add_command(label='Tabla de Simbolos',command=self.TSR)
        reportes.add_command(label='Reporte de Optimizacion', command=self.Optimizar)
        self.menubar.add_cascade(label="Reportes",menu=reportes)
        opciones = Menu(self.menubar, tearoff=0)
        opciones.add_command(label="Cambiar Color Consolas", command=self.cambiarcolor)
        opciones.add_command(label="Cambiar Color Ventana", command=self.colorventana)
        opciones.add_command(label="Cambiar Color Texto", command=self.colortexto)
        self.menubar.add_cascade(label="Opciones", menu=opciones)
        self.window.mainloop()
        self.aoptimizar=""




    def imprimir(self):
        f = graphviz.Digraph(filename='Reporte_AST.gv')
        f.node('Node0', label='RAIZ')
        if self.resultado is not None:
            for nodo in self.resultado:
                nodo.graficarasc('Node0', f)
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

    def reporte_gramatica(self):

        html = ''' 
                <html>''' + head_html + '''
                    <body>
                    <h1>Reporte Gramatical</h1>
                    <table id="t02">
                        <tr>
                            <th>Produccion</th>
                            <th>Regla Semántica</th> 
                        </tr>
                '''
        for texto in self.reporteg:
            html+=texto
        html += '''</table>'''

        html += '''</body>
                    </html>
                '''
        try:
            file = open('Gramatical.html', 'w')
            file.write(html)
        except:
            pass
        finally:
            file.close()
            global new
            webbrowser.open('Gramatical.html', new=new)


    def Optimizar(self):
        self.consola.delete('1.0', END)

        resultado=gramaticaop.parse(self.aoptimizar)
        codigo="#OPTIMIZADO"
        reporte=[]
        alcanzable=True
        aux=''
        for nodo in resultado:
            if isinstance(nodo,instop.GoTo):
                alcanzable=False
                codigo+=nodo.Optimizar(reporte,"")
            elif isinstance(nodo,instop.Etiqueta):
                alcanzable=True
                if aux !='':
                    reporte.append(aux)
                    aux=''
            if alcanzable:
                print(nodo)
                codigo+=nodo.Optimizar(reporte,"")
            else:
                if aux=='':
                    aux = 'Regla 2: Eliminando codigo inalcanzable \n'
                aux+=nodo.Optimizar(reporte,"")
        self.mostrar_augus(codigo)

        html = ''' 
                       <html>''' + head_html + '''
                           <body>
                           <h1>Reporte Optimizacion</h1>
                           <table id="t02">
                               <tr>
                                   <th>No</th>
                                   <th>Descripcion</th> 
                               </tr>
                       '''
        cuenta=1
        for texto in reporte:
            html += '<tr><td>'+str(cuenta)+'</td><td>'+texto+'</td></tr>'
            cuenta+=1
        html += '''</table>'''

        html += '''</body>
                           </html>
                       '''
        try:
            file = open('Optimizacion.html', 'w')
            file.write(html)
        except:
            pass
        finally:
            file.close()
            global new
            webbrowser.open('Optimizacion.html', new=new)

    def analizar(self):

        self.consola.delete('1.0',END)
        input = self.txtarea.get(1.0, END)
        self.errores=lista_err.L_Error()
        resultado = g.parse(input,self.errores)

        if self.errores.principio is not None:
            self.consola.insert('end',">>Error: Verifique errores lexicos y sintacticos\n>>")
        if resultado is None or len(resultado)==0:
            return
        self.reporteg=g.reporteg
        self.resultado=resultado
        self.TS=TablaDeSimbolos("global")
        codigo="main: \n" \
               "$s0 = array(); \n" \
               "$s1 = array(); \n" \
               "$ra = 0; \n" \
               "$sp = 0;\n"
        for nodo in resultado:
            if isinstance(nodo,Funcion):
                if not self.TS.agregarfunc(nodo):
                    self.errores.insertar(N_Error("Semantico",'Funcion '+nodo.nombre+' ya existe',nodo.fila,nodo.columna))

        if not 'main' in self.TS.funciones:
            self.errores.insertar(
                N_Error("Semantico", 'Funcion main no esta definida', 0, 0))
            self.consola.insert('end', ">>Error: Verifique errores semanticos\n>>")
            return
        for nodo in resultado:
            if isinstance(nodo,Struct):
                if not self.TS.agregarstruct(nodo):
                    self.errores.insertar(
                        N_Error("Semantico", 'Struct ' + nodo.nombre + ' ya existe', nodo.fila, nodo.columna))
                    self.consola.insert('end', ">>Error: Verifique errores semanticos\n>>")


        cuenta=1
        for fun in self.TS.funciones:
            codigo+='$v'+str(cuenta)+'=0;\n'
            cuenta+=1
        for nodo in resultado:
            nodo.analizar(self.TS,self.errores)
        for nodo in self.resultado:
            if isinstance(nodo,Arreglo) or isinstance(nodo,Declaracion) or isinstance(nodo,ArregloSimple):
                codigo+=nodo.getC3D(self.TS)
        codigo+='goto main_main;\n'
        for nodo in resultado:
            if not (isinstance(nodo,Arreglo) or isinstance(nodo,Declaracion) or isinstance(nodo,ArregloSimple)):
                codigo+=nodo.getC3D(self.TS)

        self.TS.funciones['main'].codigofin+='exit;\n'

        for fun in self.TS.funciones:
            codigo+=self.TS.funciones[fun].codigofin
        self.mostrar_augus(codigo)
        self.aoptimizar=codigo

        augus.ejec_ascendente(self.consola,codigo,self.txtarea)






    def TSR(self):
        html = ''' 
                        <html>''' + head_html + '''
                            <body>
                            <h1>Reporte Tabla de Simbolos</h1>
                            <table id="t02">
                                <tr>
                                    <th>No</th>
                                    <th>Tipo</th>
                                    <th>Nombre</th>
                                    <th>Ambito</th>
                                    <th>Dimensiones</th> 
                                    <th>Temporal Referencia</th>
                                </tr>
                        '''
        cuenta=1
        for sim in self.TS.simbolos:
            html+='<tr><td>'+str(cuenta)+'</td><td>'+str(sim.tipo)+'</td><td>'+str(sim.nombre)+'</td><td>'+str(sim.ambito)+'</td><td>'+str(sim.dimensiones)+'</td><td>'+str(sim.posicion)+'</td></tr>'
            cuenta+=1
        html += '''</table>'''

        html+='''
        <h1>Reporte Tabla de Simbolos: Funciones</h1>
                            <table id="t02">
                                <tr>
                                    <th>No</th>
                                    <th>Tipo</th>
                                    <th>Nombre</th>
                                    <th>Cantidad Parametros</th>

                                </tr>
                        '''
        cuenta=1
        for funo in self.TS.funciones:
            fun=self.TS.funciones[funo]
            html+='<tr><td>'+str(cuenta)+'</td><td>'+str(fun.tipo.tipo.name)+'</td><td>'+str(fun.nombre)+'</td><td>'+str(len(fun.parametros))+'</td></tr>'
            cuenta+=1
        html += '''</table>'''
        html += '''</body>
                            </html>
                        '''
        try:
            file = open('TS.html', 'w')
            file.write(html)
        except:
            pass
        finally:
            file.close()
            global new
            webbrowser.open('TS.html', new=new)

    def mostrar_augus(self,codigo):
        ventana = Toplevel(self.window)
        consola=TextPad2(ventana)
        consola.insert(INSERT,codigo)

    def errores_r(self):
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

        if self.errores.principio is not None:
            reporte_errores=self.errores.principio
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