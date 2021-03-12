#!/usr/bin/python3
from datetime import date
import os
import re
import sys
from getopt import getopt
import requests
import shelve


teclado = {
    "2": "abcâãáàç",
    "3": "defêéè",
    "4": "ghií",
    "5": "jkl",
    "6": "mnoõóòöô",
    "7": "pqrs",
    "8": "tuvúùû",
    "9": "xywz",
    "0": " "
}


def palavraNumeros(palavra):
    sequencia = ""
    for a in palavra:
        for n in teclado:
            if a.lower() in teclado[n]:
                sequencia = sequencia+n
    return sequencia


def numeroRegex(numero):
    regex = r""
    for a in numero:
        regex = regex+"["+teclado[a]+"]"
    return regex


def procuraPalavra(regex):
    with open("formas.totalptunicode.txt") as f:
        conteudo = f.read()
    palavras = re.findall(rf"\s{regex}$", conteudo,
                          flags=re.MULTILINE | re.IGNORECASE)
    palavras = [palavra[1:] for palavra in palavras]
    return palavras


print(numeroRegex(palavraNumeros("Pêra sabe bem")))
