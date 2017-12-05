#!/usr/bin/python3
# -*- coding: utf-8 -*-

#calculos sin Usar librerias externas
datosMedia = (1525, 257, 378, 9543, 7854, 152,)

datosModa = (9, 5, 9, 4, 3, 6, 7, 1, 2, 3, 9, 1, 2,)

datosMediana = [9, 5, 9, 4, 3, 6, 7, 1, 2, 3, 9, 1, 2]

def mediana(datosMediana):
    datosMediana.sort()
    cantidad = len(datosMediana)
    if (cantidad % 2) == 0:
        print("Tiene 2 medianas: "+str(datosMediana[cantidad // 2-1])+", "+str(datosMediana[cantidad // 2 ]))
    else:
        tt = cantidad // 2
        print("Mediana es: "+str(datosMediana[tt]))


def media(datosMedia):
    media = 0
    for x in range(len(datosMedia)):
        media = media + datosMedia[x]
    media = media / len(datosMedia)
    print ("Media es:"+str(media))


def moda(datosModa):
    dic = {}
    maximo = 0
    resultado = {}
    for x in range(len(datosModa)):
        if datosModa[x] in dic:
            dic[datosModa[x]] = dic[datosModa[x]] +1
        else:
            dic.update({datosModa[x]: 1})
        if dic[datosModa[x]] > maximo:
            maximo = maximo +1
            resultado = { datosModa[x] : maximo }
    for clave, valor in iter(resultado.items()):
        print ("el numero que mas se repite es: "+str(clave)+" Con: "+str(valor)+" repeticiones")

mediana(datosMediana)
media(datosMedia)
moda(datosModa)