# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 14:17:02 2020

@author: Gisela Schierff
"""

'''
Ejercicio 2: Crear una función que devuelva una lista con todos los números 
pares del 0 al 100 inclusive. Imprimir esa lista por pantalla.
'''
def numerosPares(): 
    listaDePares = []
    for numero in range(101): 
        if numero % 2 == 0: 
            listaDePares.append(numero)
    return listaDePares
print(numerosPares())        
            