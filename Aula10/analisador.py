from re import *
import sys

#analisador léxico
literals = "=:."
tokens = ("DOM", "EOC", "ID", "VALOR")

def t_DOM(t):
  r'[#].+'
  t.value = sub(r"[#]", "", t.value)
  return t

def t_ID(t):
  r'\w+(?=[:=])'
  #print(f"id =  {t.value}")
  return t

#def t_EOC(t):
  #r'\n\n+(?=([#]|\w+:))'
  #print("EOC")
  #return t

def t_VALOR(t):
  r'!\w+.+'
  #print(f"valor = {t.value}")
  return t

t_ignore= " \t\n"
def t_error(t):
    print(f"Carater ilegal em {t.value[0]}, linha {t.lexer.lineno}")

from ply.lex import lex
lexer = lex()

#parser
def p_a(t):"dic : meta doms"; print(f"doms = {t[2]}")

def p_b(t):"doms : doms dom"; t[0] = t[1] + [t[2]]
def p_c(t):"doms : dom"; t[0] = [t[1]]

def p_d(t):"dom : DOM conceitos"; t[0] = (t[1], t[2])

def p_e(t):"conceitos : conceito conceitos"; t[0] = [t[1]] + t[2]
def p_f(t):"conceitos :"; t[0] = []

def p_g(t):"conceito : avs '.'"; t[0] = t[1]

def p_h(t):"avs : av avs"; t[0] = [t[1]] + t[2]
def p_i(t):"avs : av"; t[0] = [t[1]]

def p_j(t):" av : ID ':' VALOR"; t[0] = (t[1], t[3])

def p_k(t):" meta : me meta"; a=3
def p_l(t):" meta :"; a=3

def p_m(t):" me : ID '=' VALOR"; a=3

def p_error(t):
    print(f"Sintax error {t.value}, {t.lexer.lineno}")

from ply.yacc import yacc
parser = yacc()
parser.parse(open(sys.argv[1]).read())
