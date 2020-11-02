#!/usr/bin/python3
import re
#abre um canal e le o ficheiro
txt=open('Harry Potter e A Pedra Filosofal.txt').read()
#imprime os primeiros 100 caracteres 
#txt[0:100]
#com txt[::] imprime tudo
#com txt[::-1] vai do fim para o inicio
#com txt[::2] vai de 2 em 2 caracteres

# print(txt[0:100])


#no modulo re 
# search procura uma expressao
# findall procura todas as ocorrencias e mete numa lista
# sub substitui
# split separa
############################
#Limpar o ficheiro
mod=re.sub(r'\n\n+',' ',txt)
mod2=re.sub(r'\f',' ',mod)
#print(mod2)
############################
mod3=re.sub(r'[ =,.?!/]','\n',mod2)
#./processaTexto.py |sort|uniq -c |sort -n
# organiza todas as palavras, quandon encontra dois iguais retira 1 e aumenta o contador, e organiza pelo numero

#./processaTexto.py |sort|uniq -c |sort -n|grep '[A-Z]'
#retira os "nomes", nao ta a 100%
print(mod3)
