#!/usr/bin/python3
# -*- coding: utf-8 -*-


import math
datos = [13, 14, 15, 15, 15, 16, 17, 18, 20]

def varianza(datos):
    sumatoria = sum(datos)
    media = sumatoria / len(datos)
    rr = list(map(lambda x: (x - media)**2, datos))
    sumatoria2 = sum(rr) / len(rr)
    return sumatoria2


def desviacion(datos):
    datos = varianza(datos)
    return math.sqrt(datos)

print(varianza(datos))
print(desviacion(datos))








