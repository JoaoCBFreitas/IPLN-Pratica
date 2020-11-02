#!/usr/bin/python3
#permite executar apos chmod 755 +nome do ficheiro
#./tutString.py
print("hello world")
#ler n, escrever ola n
nome=input("Diz o teu nome: ")
#Com + tem de se por separador manualmente
print("Ola "+nome)
#Com , é posto um separador automaticamente, default é [ ]
print("Tambem",nome,"funciona",nome,"assim")
#O separador pode ser definido com sep
print("Tambem",nome,"funciona",nome,"assim",sep="SEPARADOR")
#Com variavel:num, ele vai preencher com 20 [ ], pode ser mudado
print(f"Tambem {nome:20} funciona",nome,"assim")
#Funcao que capitaliza o string
#pydoc3 str.capitalize para ver no manual
print("Ola",str.capitalize(nome))
#Pode-se multiplicar strings
print(nome*3)
#Pode-se fazer coisas catitas com multiplicacoes e/ou somas
s=(nome*4+'\n')*3
print(s)
#Modo rawp, para expressoes regulares
print("Coisa",r'\b',"cena")
#Octo dump, para debugging
#./tutString |od -c
#converter pdf para texto com pdftotext +nome do ficheiro