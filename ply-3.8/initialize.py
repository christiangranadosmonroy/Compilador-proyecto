import ply.lex as lex
import re
import codecs
import os
import sys

Reserved = ['BEGIN','END','IF','THEN','WHILE','DO','CALL','CONST',
            'VAR','PROCEDURE','OUT','IN','ELSE','AS','BREAK','FLOAT',
            'SIZEOF','PUBLIC','VOID','OUT','NULL','STRUCT','SWITCH', 
            'NEW','ABSTRACT','BASE','DOUBLE','RETURN',
        ]

tokens = Reserved+['ID','NUMBER','PLUS','MINUS','TIMES','DIVIDE',
        'ODD','ASSIGN','NE','LT','LTE','GT','GTE',
        'LPARENT', 'RPARENT','COMMA','SEMMICOLOM',
        'DOT','UPDATE','REAL','WHOLE','CHAIN',
        ]

t_ignore = '\t '
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ODD = r'ODD'
t_ASSIGN = r'='
t_NE = r'<>'
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMMA = r','
t_SEMMICOLOM = r';'
t_DOT = r'\.'
t_UPDATE = r':='

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in Reserved:
        t.value = t.value.upper()
        #reservadas.get(t.value,'ID')
        t.type = t.value

    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#dsfjksdlgjklsdgjsdgslxcvjlk-,.
def t_COMMENT(t):
    r'\#.*'
    pass

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print ("ilegal caracter '%s'" % t.value[0])
    t.lexer.skip(1)

def findfiles(directory):
    Ffiles = []
    numFile = ''
    response = False
    cont = 1

    for base, dirs, files in os.walk(directory):
        Ffiles.append(files)

    for file in files:
        print (str(cont)+". "+file)
        cont = cont+1

    while response == False:
        numFile = input('\nNumber of Test: ')
        for file in files:
            if file == files[int(numFile)-1]:
                response = True
                break

    print ("You have chosen \"%s\" \n" %files[int(numFile)-1])

    return files[int(numFile)-1]

directory = 'C:/Users/christian/documents/compiladores/lexico/ply-3.8/prueba'
Files = findfiles(directory)
test = directory+Files
fp = codecs.open(test,"r","utf-8")
chain = fp.read()
fp.close()

Analyzer = lex.lex()

Analyzer.input(chain)

while True:
    tok = Analyzer.token()
    if not tok : break
    print (tok)