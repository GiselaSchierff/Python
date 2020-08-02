# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 12:23:34 2020

@author: Gisela Schierff
"""
'''
Ejercicio 5: Crear un diccionario con los meses del año de la forma { 1: "enero"}. Desafío: lograr cambiar las claves. Pista: si imprimen ítems del diccionario les crea una lista. Una vez que lo logren, imprimir el diccionario modificado.
'''

diccionarioConMeses = {1 : "Enero",
                       2 : "Febrero",
                       3 : "MArzo",
                       4 : "Abril",
                       5 : "Mayo",
                       6 : "Junio",
                       7 : "Julio",
                       8 : "Agosto",
                       9 : "Septiembre",
                       10 : "Octubre",
                       11 : "Noviembre",
                       12 : "Diciembre"}

listaConMeses = list(diccionarioConMeses.values())
listaConNumeros = list(diccionarioConMeses.items())
diccionarioConMeses.clear()

diccionarioConMeses = dict(zip(listaConNumeros, listaConMeses))
print(diccionarioConMeses)
