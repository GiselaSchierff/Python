# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 17:30:00 2020

@author: Gisela Schierff
"""
'''
Ejercicio 12: Crear un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.
'''

primerVector = [1, 2, 3]
segundoVector = [-1, 0, 2]
productoEscalar = []

for coordenada in range(3):
    elemento = primerVector[coordenada] * segundoVector[coordenada]
    productoEscalar.append(elemento)
    
print(sum(productoEscalar))    