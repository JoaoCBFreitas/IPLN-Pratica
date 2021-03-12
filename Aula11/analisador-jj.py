from re import *
import sys
import pprint

#    ':' '=' '#' '(' '+' ')' ';'
#    VALOR '\w[\w ,]*'
#    ID    '\w+'
#

#analisador léxico
literals = "#=:.;()+{}|"
tokens = ("EOC", "ID", "VALOR","TAB" )

def t_TAB(t):
  r'tab\b'
  return t

def t_EOC(t):
  r'(\n\n+)'
  t.lexer.lineno += len(t.value)
  # print("EOC")
  return t

def t_VALOR(t):
  r'\w+[ ,.][\w ,.]+'
  #print(f"valor = {t.value}")
  return t

def t_ID(t):
  r'\w+'
  #print(f"id =  {t.value}")
  return t

def t_NL(t):
  r'\n'
  t.lexer.lineno += 1
  #print("ignoring \n");   ## no return

def t_JJIGNORE(t):
  r'[ \t]|//.*'

def t_error(t):
    print(f"Carater ilegal em {t.value[0]}, linha {t.lexer.lineno}")

from ply.lex import lex

lexer = lex()

#parser
def p_a(t):"dic : metas doms"; S["meta"]=dict(t[1]); S["concs"] = junta_doms(t[2])

def p_b(t):"doms : doms dom"; t[0] = t[1] + [t[2]]
def p_c(t):"doms : dom"; t[0] = [t[1]]

def p_d(t):"dom : '#' ele elo conceitos"; t[0] = norm_dom((t[2], t[4]))

def p_f1(t):"conceitos : conceitos conceito"; t[0] = t[1] + [t[2]]
def p_f2(t):"conceitos : "; t[0] = []
def p_f3(t):"conceitos : conceitos TAB '{' tabela '}'"; t[0] = t[1] + t[4]

def p_g(t):"conceito : avs elo"; t[0] = t[1]

def p_h(t):"avs : av avs"; t[0] = [t[1]] + t[2]
def p_i(t):"avs : av"; t[0] = [t[1]]

def p_j(t):"av : ID ':' ele atro"; t[0] = (t[1], t[3])

def p_k(t):"metas : metas meta"; t[0] = t[1] + [t[2]]
def p_l(t):"metas :"           ; t[0] = [] 

def p_o(t):"meta : ID '=' listav elo" ; t[0] = (t[1],t[3])

def p_p(t):"listav : ele"             ; t[0] = [t[1]]
def p_q(t):"listav : listav ';'  ele" ; t[0] = t[1]+[t[3]]

def p_r(t):"ele : ID"    ; t[0] = t[1]
def p_s(t):"ele : VALOR" ; t[0] = t[1]

def p_t(t):"elo : EOC  "
def p_u(t):"elo : " 

def p_v(t):"atro : "                  
def p_w(t):"atro : '(' '+' ele ')' " 

def p_y(t):"tabela : linha linhas"; t[0] = zipiterado(t[1],t[2])

def p_z1(t):"linhas : linha" ; t[0] = [t[1]]
def p_z2(t):"linhas : linhas linha" ; t[0] = t[1] + [t[2]]

def p_x1(t):"linha : ele "; t[0] = [t[1]]
def p_x2(t):"linha : linha '|' ele "; t[0] = t[1] + [t[3]]

def p_error(t):
    print(f"Sintax error {t.value}, {t.lexer.lineno}")

from ply.yacc import yacc
parser = yacc()

import jinja2 as j2

def zipiterado(esq,ll):
    return [ list(zip(esq,x)) for x in ll ]

def mkdic(cs,ling):
   dicf={}
   for t in cs:
      for id,v in t:
         if id == ling:
            dicf[v]= t
   return sorted(dicf.items())
   
def junta_doms(ds):
   r = []
   for a in ds:
      r.extend(a)
   return r

def norm_dom(d):
    return [ x + [("dom",d[0])] for x in d[1] ]

def geratex(S):
   S["dom"] = mkdic( S["concs"],"PT" )
   tex = j2.Template("""
\\documentclass[portuges,a4paper]{article}
\\usepackage{babel}
\\usepackage[mathletters]{ucs}
\\usepackage[utf8x]{inputenc}

\\usepackage[T1]{fontenc}
\\usepackage{dici}
\\begin{document}
\\title{ {{meta.titulo[0]}} }
\\author{
  {% for a in meta.autor %} {{a}} \\and {% endfor %}
}
\\maketitle
\\newpage
\\twocolumn

\\begin{dictionary}
  {% for d in dom %} 
 \\term{ {{d[0]}} }{ 
     {% for i,v in d[1] %} 
        \\textsc{ {{i}}}: {{v}}\\
     {% endfor %}
  }
  {% endfor %}
\end{dictionary}
\\end{document}
""")
   print(tex.render(S))

S={}
parser.parse(open(sys.argv[1]).read())
#print(S)
geratex(S)
