#!/usr/bin/python3
import re
import sys
# nome do ficheiro é dado ao executar o programa
nomefich = sys.argv[1]
with open(nomefich) as f:
    txt = f.read()
mod = re.sub(r'\n\n+', ' ', txt)
mod2 = re.sub(r'\f', ' ', mod)

mod3 = re.sub(r'\W+', '\n', mod2)
listaPalavras = re.split('\n', mod3)


dicionario = {}

for x in listaPalavras:
    if x in dicionario:
        dicionario[x] += 1
    else:
        dicionario[x] = 1


# Remove os espaços
for key, value in sorted(dicionario.items(), key=lambda x: x[1]):
    if len(key) == 0:
        dicionario.pop(key)
# remove os numeros e os (os,as,a,e,etc)
for key, value in sorted(dicionario.items(), key=lambda x: x[1]):
    if key[0].isalpha() == False or len(key) < 4 or key[0].isupper() == False:
        dicionario.pop(key)
# Normaliza todas as chaves restantes
for key, value in sorted(dicionario.items(), key=lambda x: x[1]):
    if key[0].isupper() == False:
        chave = key
        dicionario[key.capitalize()] = dicionario.pop(key)
for key, value in sorted(dicionario.items(), key=lambda x: x[1]):
    print(key, '------->', value)


################TPC###########################
# normalizar maiusculas e minusculas- done
# remover os (o,a,e,de,os,que,etc...)-done
# receber no nome do ficheiro atraves da linha de comando com o sys -done
# Inventar um problema sobre o ficheiro e resolvelo
##############################################
