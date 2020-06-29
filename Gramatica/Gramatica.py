import Errores.N_Error as err

reservadas = {
    'break':'t_break',
    'case': 't_case',
    'char': 't_char',
    'continue':'t_continue',
    'default':'t_default',
    'do':'t_do',
    'double':'t_double',
    'else':'t_else',
    'float':'t_float',
    'for':'t_for',
    'goto':'t_goto',
    'if':'t_if',
    'int':'t_int',
    'return':'t_return',
    'sizeof':'t_sizeof',
    'struct':'t_struct',
    'switch':'t_switch',
    'void':'t_void',
    'while':'t_while',
}

tokens = [
            'par1',
            'par2',
            'cor1',
            'cor2',
            'punto',
            'mas',
            'menos',
            'not',
            'notb',
            'incremento',
            'decremento',
            'por',
            'division',
            'modulo',
            'shiftizq',
            'shiftder',
            'mayor',
            'menor',
            'mayori',
            'menori',
            'igual',
            'diferente',
            'andb',
            'xorb',
            'orb',
            'and',
            'or',
            'condicional',
            'bipunto',
            'asigna',
            'porasigna',
            'divasigna',
            'modasigna',
            'masasigna',
            'menosasigna',
            'shiftizqasigna',
            'shiftderasigna',
            'andbasigna',
            'orbasigna',
            'xorbasinga',
            'coma',
            'pyc',
            'iden',
            'decimal',
            'entero',
            'char',
            'string',
            'llav1',
            'llav2'
         ] + list(reservadas.values())

# Tokens
t_llav1 = r'\{'
t_llav2 = r'\}'
t_par1 = r'\('
t_par2 = r'\)'
t_cor1 = r'\['
t_cor2 = r'\]'
t_punto = r'\.'
t_mas = r'\+'
t_menos = r'-'
t_not = r'!'
t_notb = r'~'
t_incremento = r'\+\+'
t_decremento = r'--'
t_por = r'\*'
t_division = r'/'
t_modulo = r'%'
t_shiftizq = r'<<'
t_shiftder = r'>>'
t_mayor = r'>'
t_menor = r'<'
t_mayori = r'>='
t_menori = r'<='
t_igual = r'=='
t_diferente = r'!='
t_andb = r'&'
t_xorb = r'\^'
t_orb = r'\|'
t_and = r'&&'
t_or = r'\|\|'
t_condicional = r'\?'
t_bipunto=r':'
t_asigna = r'='
t_porasigna = r'\*='
t_divasigna = r'/='
t_modasigna = r'%='
t_masasigna = r'\+='
t_menosasigna = r'-='
t_shiftizqasigna = r'<<='
t_shiftderasigna = r'>>='
t_andbasigna = r'&='
t_orbasigna = r'\|='
t_xorbasinga = r'^='
t_coma = '\,'
t_pyc = ';'


def t_decimal(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("El valor es muy grande %d", t.value)
        t.value = 0
    return t


def t_entero(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("El valor de integer es muy grande %d", t.value)
        t.value = 0
    return t


def t_char(t):
    r'\'.\''
    t.value = t.value[1:-1]  # remuevo las comillas
    #t.value= t.value.replace("\\n","\n")
    t.value = t.value.replace("\\\\", "\\")
    t.value = t.value.replace("\\\'", "\'")
    t.value = t.value.replace("\\\"", "\"")
    t.value = t.value.replace("\\r", "\r")
    t.value = t.value.replace("\\t", "\t")
    return t


def t_string(t):
    r'\".*?\"'
    t.value = t.value[1:-1]  # remuevo las comillas
    #t.value= t.value.replace("\\n","\n")
    t.value = t.value.replace("\\\\", "\\")
    t.value = t.value.replace("\\\'", "\'")
    t.value = t.value.replace("\\\"", "\"")
    t.value = t.value.replace("\\r", "\r")
    t.value = t.value.replace("\\t", "\t")
    return t


def t_iden(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(), 'iden')  # Check for reserved words
    return t

def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'//.*\n'
    t.lexer.lineno += 1


# Caracteres ignorados
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


def t_error(t):
#    errores.insertar(err.N_Error("Lexico", "Caracter ilegal '%s'" % t.value[0],
                             #    t.lineno, find_column(input, t)))
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


import ply.lex as lex

lexer = lex.lex()

precedence = (
    ('left','coma'),
    ('right','asigna','porasigna','divasigna','modasigna','masasigna',
            'menosasigna','shiftizqasigna','shiftderasigna',
            'andbasigna','orbasigna','xorbasinga'),
    ('right', 'condicional','bipunto'),
    ('left', 'or'),
    ('left','and'),
    ('left','orb'),
    ('left','xorb'),
    ('left','andb'),
    ('left','igual','diferente'),
    ('left','mayor','menor','mayori','menori'),
    ('left','shiftder','shiftizq'),
    ('left','mas','menos'),
    ('left','por','division','modulo'),
    ('right','t_sizeof','incremento','decremento',
     'not','notb'),
    ('left','par1','par2','cor1','cor2','punto')
)

from AST import *
from AST.Declaracion import *
from AST.Expresiones import *
from AST.Arreglo_Simple import *
from AST.Arreglo import *
from AST.Asignacion_Arreglo import *
from AST.Asignacion import *
from AST.Atributo import *
from AST.Struct import *
from AST.Lista import *
from AST.Acceso_Struct import *
from AST.Break import *
from AST.Funcion import *
from AST.IF import *
from AST.Switch import *
from AST.Llamada import *
from AST.While import *
from AST.DoWhile import *
from AST.For import *
from AST.Etiqueta import *
from AST.Return import *
from TS.Tipos import *




def p_inicio(t):
    'S         : Sentencias_G'
    t[0]=t[1]
    print(t[1])
    print('hola')

def p_inicio2(t):
    'S         : '
    t[0]=[]

def p_Sentencias_G_Sentencia_G(t):
    'Sentencias_G : Sentencias_G Sentencia_G'
    t[1].extend(t[2])
    t[0]=t[1]

def p_Sentencias_G(t):
    'Sentencias_G : Sentencia_G'
    t[0]=t[1]

def p_Sentencia_G(t):
    '''Sentencia_G : Declaracion
                   | LASIGNACION pyc
                   | STRUCT pyc
                   | Funcion'''
    t[0]=t[1]

def p_DECLARACION(t):
    'Declaracion : Tipos L_Dec pyc'
    t[0]=t[2]
    print(t[2])

def p_L_DEC(t):
    'L_Dec : L_Dec coma Dec'
    t[1].append(t[3])
    t[0]=t[1]
def p_L_DEC_2(t):
    'L_Dec : Dec'
    t[0]=[t[1]]

def p_Dec(t):
    'Dec : iden'
    fila=t.slice[1].lineno
    columna=find_column(input,t.slice[1])
    if type(t[-1])==str:t[0] = Declaracion(t[-3], t.slice[1].value, None, fila, columna)
    else:t[0] = Declaracion(t[-1],t.slice[1].value,None,fila,columna)
    print(t[0])

def p_Dec2(t):
    'Dec : iden asigna EXP'
    if type(t[-1]) == str:
        t[0] = Declaracion(t[-3], t.slice[1].value, t[3], t.slice[1].lineno, find_column(input, t.slice[1]))
    else:
        t[0] = Declaracion(t[-1], t.slice[1].value, t[3], t.slice[1].lineno, find_column(input, t.slice[1]))

def p_Dec_ArraySimple_Exp(t):
    ' Dec : iden cor1 cor2 asigna EXP'
    if type(t[-1]) == str:
        t[0] = ArregloSimple(t[-3], t.slice[1].value, t[5], t.slice[1].lineno, find_column(input, t.slice[1]))
    else:
        t[0] = ArregloSimple(t[-1], t.slice[1].value, t[5], t.slice[1].lineno, find_column(input, t.slice[1]))

def p_Dec_Array(t):
    ' Dec : iden LACCESO'
    fila=t.slice[1].lineno
    columna=find_column(input,t.slice[1])
    if type(t[-1]) == str:
        t[0] = Arreglo(t[-3],t.slice[1].value,primitivo(0,fila,columna,t[-3].tipo.name),t[2],fila,columna)
    else:
        t[0] = Arreglo(t[-1],t.slice[1].value,primitivo(0,fila,columna,t[-1].tipo.name),t[2],fila,columna)

def p_Dec_Array_Exp(t):
    ' Dec : iden LACCESO asigna EXP'
    fila=t.slice[1].lineno
    columna=find_column(input,t.slice[1])
    if type(t[-1]) == str:
        t[0] = Arreglo(t[-3],t.slice[1].value,t[4],t[2],fila,columna)
    else:
        t[0] = Arreglo(t[-1],t.slice[1].value,t[4],t[2],fila,columna)

def p_LACCESO_Acceso(t):
    ' LACCESO : LACCESO cor1 EXP cor2'
    t[1].append(t[3])
    t[0]=t[1]

def p_LACCESO_Acc(t):
    ' LACCESO : cor1 EXP cor2'
    t[0]=[t[2]]


def p_LASIGNACION(t):
    'LASIGNACION : LASIGNACION coma ASIGNACION'
    t[1].append(t[3])
    t[0]=t[1]
def p_LASIGNACION_ASIGNACION(t):
    'LASIGNACION : ASIGNACION'
    t[0]=[t[1]]

def p_ASGINACION(t):
    ' ASIGNACION : iden'
    t[0]=Asignacion(t[1],t.slice[1].lineno,find_column(input,t.slice[1]))

def p_ASIGNACION_VALOR(t):
    ' ASIGNACION : iden OP EXP'
    t[0]=AsignacionOp(t[1],t[2],t[3],t.slice[1].lineno,find_column(input,t.slice[1]))

def p_ASIGNACION_ARREGLO(t):
    ' ASIGNACION : iden LACCESO'
    t[0]=Asignacion_Arreglo(t[1],t[2],t.slice[1].lineno,find_column(input,t.slice[1]))

def p_ASIGNACION_ARREGLO_OP(t):
    ' ASIGNACION : iden LACCESO OP EXP'
    t[0]=Asignacion_Arreglo_Op(t[1],t[3],t[4],t[2],t.slice[1].lineno,find_column(input,t.slice[1]))

def p_ASIGNACION_STRU(t):
    ' ASIGNACION : ACCESO_STRUCT OP EXP'
    t[0]=AsignacionOp(t[1],t[2],t[3],t.slice[2].lineno,find_column(input,t.slice[2]))

def p_ASIGNACION_STRU_NONE(t):
    ' ASIGNACION : ACCESO_STRUCT'
    t[0]=Asignacion(t[1],t[1].fila,t[1].columna)

def p_OPERADOR_ASIGNA(t):
    ''' OP :  andbasigna
            | divasigna
            | masasigna
            | menosasigna
            | modasigna
            | orbasigna
            | porasigna
            | shiftizqasigna
            | shiftderasigna
            | xorbasinga
            | asigna'''
    t[0]=t[1]

def p_struct(t):
    'STRUCT : t_struct iden llav1 ATRIBUTOS llav2'
    t[0]= [Struct(t[2],t[4],t.slice[1].lineno,find_column(input,t.slice[1]))]


def p_LATT(t):
    'ATRIBUTOS : ATRIBUTOS ATRIBUTO'
    t[1].extend(t[2])
    t[0]=t[1]
def p_LATT2(t):
    'ATRIBUTOS : ATRIBUTO'
    t[0]=t[1]
def p_atributo(t):
    'ATRIBUTO : Tipos LItemsStruct pyc'
    t[0]=t[2]
def p_LItemsStruct(t):
    'LItemsStruct : LItemsStruct coma ItemsStruct'
    t[1].append(t[3])
    t[0]=t[1]
def p_LItemsStruct_ItemsStruct(t):
    'LItemsStruct : ItemsStruct'
    t[0]=[t[1]]

def p_atributo_id(t):
    'ItemsStruct : iden'
    if type(t[-1]) == str:tipo=t[-3]
    else:tipo=t[-1]
    t[0]=Atributo(tipo,t[1],t.slice[1].lineno,find_column(input,t.slice[1]))

def p_atributo_arr(t):
    'ItemsStruct : iden LACCESO'
    if type(t[-1]) == str:tipo=t[-3]
    else:tipo=t[-1]
    t[0]=Atributo(tipo,t[1],t.slice[1].lineno,find_column(input,t.slice[1]),t[2])

def p_atributo_id2(t):
    'ItemsStruct2 : iden'
    t[0]=Atributo(None,t[1],t.slice[1].lineno,find_column(input,t.slice[1]))

def p_atributo_arr2(t):
    'ItemsStruct2 : iden LACCESO'
    t[0]=Atributo(None,t[1],t.slice[1].lineno,find_column(input,t.slice[1]),t[2])

def p_acceso_struct(t):
    'ACCESO_STRUCT : ItemsStruct2 punto ItemsStruct2'
    t[0]=AccesoStruct(t[1],t[3],t.slice[2].lineno,find_column(input,t.slice[2]))

def p_Tipos1(t):
    'Tipos : t_char'
    t[0] = TIPO(TIPO_DATOS.CHAR)

def p_Tipos2(t):
    'Tipos : t_int'
    t[0] = TIPO(TIPO_DATOS.INT)

def p_Tipos3(t):
    'Tipos : t_double'
    t[0] = TIPO(TIPO_DATOS.DOUBLE)

def p_Tipos4(t):
    'Tipos : t_float'
    t[0] = TIPO(TIPO_DATOS.FLOAT)


def p_funcion(t):
    'Funcion : Tipos iden par1 Parametros par2 BLOQUE'
    t[0]=[Funcion(t[1],t[2],t[4],t[6],t.slice[2].lineno,find_column(input,t.slice[2]))]

def p_funcion_void(t):
    'Funcion : t_void iden par1 Parametros par2 BLOQUE'
    t[0]=[Funcion(TIPO(TIPO_DATOS.VOID),t[2],t[4],t[6],t.slice[2].lineno,find_column(input,t.slice[2]))]



def p_l_parametros_e(t):
    'Parametros :'
    t[0]=[]

def p_l_parametros(t):
    'Parametros : Parametros coma Parametro'
    t[1].append(t[3])
    t[0]=t[1]

def p_l_parametros_p(t):
    'Parametros : Parametro'
    t[0]=[t[1]]

def p_sentencias_f(t):
    'SS_F : SS_F S_F'
    t[1].extend(t[2])
    t[0]=t[1]
    print('hola')

def p_sentencias_s_f(t):
    'SS_F : S_F'
    t[0]=t[1]
    print('hola')
def p_sentencia_f(t):
    '''S_F : Declaracion
         | LASIGNACION pyc
        | STRUCT pyc
        | IF
        | LLAMADA pyc
        | BREAK pyc
        | CONTINUE pyc
        | SWITCH
        | DO_WHILE pyc
        | WHILE
        | RETURN
        | ETIQUETA
        | GOTO pyc
        | FOR'''
    t[0]=t[1]


def p_bloque(t):
    'BLOQUE : llav1 SS_F llav2'
    t[0]=t[2]

def p_bloque_e(t):
    'BLOQUE : llav1 llav2 '
    t[0]=[]


def p_for_e(t):
    'FOR : t_for par1 INICIO EXP pyc INCDC BLOQUE'
    t[0]=[For(t[3],t[4],t[6],t[7],t.slice[1].lineno,find_column(input,t.slice[1]))]

def p_Inicio(t):
    'INICIO : Tipos Dec pyc'
    t[0]=t[2]

def p_Inicio2(t):
    'INICIO : ASIGNACION pyc'
    t[0]=t[1]

def p_Inicio_e(t):
    'INICIO : pyc'
    t[0]=None

def p_cremetno(t):
    'INCDC : EXP par2'
    t[0]=t[1]

def p_cremetno2(t):
    'INCDC : par2'
    t[0]=None

def p_etiqueta(t):
    'ETIQUETA : iden bipunto'
    t[0]=[Etiqueta(t[1],t.slice[1].lineno,find_column(input,t.slice[1]))]

def p_goto(t):
    'GOTO : t_goto iden'
    t[0]=[Goto(t[2],t.slice[1].lineno,find_column(input,t.slice[1]))]

def p_do_while(t):
    'DO_WHILE :  t_do BLOQUE t_while par1 EXP par2'
    t[0]=[DoWhile(t[5],t[2],t.slice[1].lineno,find_column(input,t.slice[1]))]

def p_while(t):
    'WHILE :  t_while  par1 EXP par2 BLOQUE'
    t[0]=[While(t[3],t[5],t.slice[1].lineno,find_column(input,t.slice[1]))]

def p_return(t):
    'RETURN : t_return EXP'
    t[0]=[Return(t.slice[1].lineno,find_column(input,t.slice[1]),t[2])]
def p_return_s(t):
    'RETURN : t_return'
    t[0]=[Return(t.slice[1].lineno,find_column(input,t.slice[1]))]

def p_switch(t):
    'SWITCH : t_switch par1 EXP par2 llav1 CASOS llav2'
    t[0]=[Switch(t[3],t[6],t.slice[1].lineno,find_column(input,t.slice[1]))]

def p_switch_default(t):
    'SWITCH : t_switch par1 EXP par2 llav1 CASOS DEFAULT llav2'
    t[0]=[Switch(t[3],t[6],t.slice[1].lineno,find_column(input,t.slice[1]),t[7])]

def p_casos(t):
    'CASOS : CASOS CASO'
    t[1].append(t[2])
    t[0]=t[1]
def p_casos_caso(t):
    'CASOS : CASO'
    t[0]=[t[1]]
def p_caso(t):
    'CASO : t_case EXP bipunto SS_F'
    t[0]=Casos(t[2],t[4],t.slice[1].lineno,find_column(input,t.slice[1]))
def p_caso_e(t):
    'CASO : t_case EXP bipunto '
    t[0]=Casos(t[2],[],t.slice[1].lineno,find_column(input,t.slice[1]))

def p_default(t):
    'DEFAULT : t_default bipunto SS_F'
    t[0]=Default(t[3],t.slice[1].lineno,find_column(input,t.slice[1]))

def p_default_e(t):
    'DEFAULT : t_default bipunto '
    t[0]=Default([],t.slice[1].lineno,find_column(input,t.slice[1]))

def p_break(t):
    'BREAK : t_break'
    t[0]=[Break(t.slice[1].lineno,find_column(input,t.slice[1]))]

def p_continue(t):
    'CONTINUE : t_continue'
    t[0]=[Continue(t.slice[1].lineno,find_column(input,t.slice[1]))]

def p_if(t):
    'IF : t_if par1 EXP par2 BLOQUE'
    t[0]= [IF(t[3],t[5],t.slice[1].lineno,find_column(input,t.slice[1]))]

def p_if_elif(t):
    'IF : t_if par1 EXP par2 BLOQUE t_else IF'
    t[0]= [IF(t[3],t[5],t.slice[1].lineno,find_column(input,t.slice[1]),t[7])]

def p_if_else(t):
    'IF : t_if par1 EXP par2 BLOQUE t_else BLOQUE'
    t[0]= [IF(t[3],t[5],t.slice[1].lineno,find_column(input,t.slice[1]),t[7])]

def p_parametro_id(t):
    'Parametro : Tipos iden'
    t[0]=Atributo(t[1],t[2],t.slice[2].lineno,find_column(input,t.slice[2]))


def p_parametro_arr(t):
    'Parametro : Tipos iden LACCESO'

    t[0]=Atributo(t[1],t[2],t.slice[2].lineno,find_column(input,t.slice[2]),t[3])

def p_llamada(t):
    'LLAMADA : iden par1 ELEMENTS par2  '
    t[0]=[Llamada(t[1],t.slice[1].lineno,find_column(input,t.slice[1]),t[3])]

def p_llamada_sinp(t):
    'LLAMADA : iden par1 par2  '
    t[0]=Llamada(t[1],t.slice[1].lineno,find_column(input,t.slice[1]))

def p_aritmeticas(t):
    '''EXP : EXP mas EXP
           | EXP menos EXP
           | EXP por EXP
           | EXP division EXP
           | EXP modulo EXP '''
    t[0] = Aritmetica(t[1],t[3],t.slice[2].value,t.slice[2].lineno,find_column(input,t.slice[2]))
    print(t[0])

def p_relacionales(t):
    '''EXP : EXP mayor EXP
           | EXP mayori EXP
           | EXP menor EXP
           | EXP menori EXP
           | EXP igual EXP
           | EXP diferente EXP'''
    t[0] = Relacional(t[1],t[3],t.slice[2].value,t.slice[2].lineno,find_column(input,t.slice[2]))
    print(t[0])

def p_logicos(t):
    '''EXP : EXP and EXP
           | EXP or EXP'''
    t[0] = logica(t[1],t[3],t.slice[2].value,t.slice[2].lineno,find_column(input,t.slice[2]))
    print(t[0])

def p_primitivos(t):
    '''EXP : string
           | entero
           | decimal
           | char'''
    t[0]= primitivo(t[1],t.slice[1].lineno,find_column(input,t.slice[1]),t.slice[1].type)

def p_exp_id(t):
    'EXP : iden'
    t[0]=variable(t[1],t.slice[1].lineno,find_column(input,t.slice[1]))

def p_exprpar(t):
    'EXP : par1 EXP par2'
    t[0]=t[1]

def p_bitabit(t):
    '''EXP : EXP shiftizq EXP
           | EXP shiftder EXP
           | EXP andb EXP
           | EXP xorb EXP
           | EXP orb EXP'''
    t[0]=bitabit(t[1],t[3],t[2],t.slice[2].lineno,find_column(input,t.slice[2]))

def p_unario(t):
    '''EXP : mas EXP
           | menos EXP
           | not EXP
           | notb EXP
           | andb EXP'''
    t[0]=unario(t[2],t[1],t.slice[1].lineno,find_column(input,t.slice[1]))

def p_inc_pre(t):
    ''' EXP : incremento EXP
            | decremento EXP'''
    t[0]=incremento(t[2],t[1],True,t.slice[1].lineno,find_column(input,t.slice[1]))

def p_ternario(t):
    'EXP : EXP condicional EXP bipunto EXP'
    t[0]=ternario(t[1],t[3],t[5],t.slice[2].lineno,find_column(input,t.slice[2]))

def p_inc_post(t):
    ''' EXP :  EXP incremento
            |  EXP decremento'''
    t[0]=incremento(t[1],t[2],False,t.slice[2].lineno,find_column(input,t.slice[2]))

def p_lista(t):
    'EXP : llav1 ELEMENTS llav2'
    t[0]=Lista(t[2],t.slice[1].lineno,find_column(input,t.slice[1]))
def p_ELEMS(t):
    'ELEMENTS : ELEMENTS coma EXP'
    t[1].append(t[3])
    t[0]=t[1]
def p_ELEMENTS(t):
    'ELEMENTS : EXP'
    t[0]=[t[1]]

def p_EXPRESIONES_ESPECIALES(t):
    '''EXP : ACCESO_STRUCT
            | LLAMADA '''
    t[0]=t[1]


def p_sizeof(t):
    'EXP : t_sizeof par1 EXP par2'
    t[0]=sizeof(t[3],t.slice[1].lineno,find_column(input,t.slice[1]))

def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)
    print("Columan", find_column(input,t))
    '''

        if not t:
        errores.insertar(err.N_Error("SINTACTICO", 'Error sintactico irrecuperable',
                                     t.lineno, find_column(input, t)))
        return

    errores.insertar(err.N_Error("Sintactico", str(t.value),
                                 t.lineno, find_column(input, t)))
    while True:
        tok = parser.token()
        if not tok or tok.type == 'PTCOMA':
            break
    parser.restart()


    '''


def t_eof(t):
    # Get more input (Example)
    more = input('main:')
    if more:
        lexer.input(more)
        return lexer.token()
    return None


import ply.yacc as yacc


def parse(input1):
    global input
    global errores

    input = input1
    global parser
    parser = yacc.yacc()
    parser.errok()
    return parser.parse(input, tracking=True, lexer=lexer)