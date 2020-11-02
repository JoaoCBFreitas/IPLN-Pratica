#!/usr/bin/python3
import re
#txt=open('Harry Potter e A Pedra Filosofal.txt').read() versao perigosa
with open('Harry Potter e A Pedra Filosofal.txt') as f:
    txt=f.read()
mod=re.sub(r'\n\n+',' ',txt)
mod2=re.sub(r'\f',' ',mod)
#mod3=re.sub(r'[ \t\–=,.?!/\f]','\n',mod2)
#\w corresponde aos alfanumericos
#\W corresponde aos nao alfanumericos
mod3=re.sub(r'\W+','\n',mod2)
listaPalavras=re.split('\n',mod3)
#dicionario vazio {}
#lista vazia []
#tuplo vazio ()
#set vazio set()

dicionario={}

for x in listaPalavras:
    if x in dicionario:
        dicionario[x]+=1
    else:
        dicionario[x]=1
#ta a ordenar pela chave e em caso de empate pelo valor
#for key,value in sorted(dicionario.items()):
#usar expressao lambda, x é o par key value, logo x[1] equivale ao valor
for key,value in sorted(dicionario.items(),key=lambda x:x[1]):
    print(key,'----->',value)