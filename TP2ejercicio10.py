# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 14:35:16 2020

@author: Gisela Schierff
"""
'''
Ejercicio 10: Utilizar el método range() para recorrer el iterable e imprimir solo los números impartes entre 1 y 40 inclusive.
'''

for numero in range (1, 40):
    if numero % 2 != 0 :
        print(numero)
