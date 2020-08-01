# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 11:48:46 2020

@author: Gisela Schierff
"""
'''
Ejercicio 8: Crear un programa que almacene en una lista las siguientes materias: Historia, Matemática, Lengua y Geografía. Luego devolver por pantalla la última materia almacenada.
'''

listaDeMaterias = ["Historia", "Matemática", "Lengua", "Geografía"]
for materia in listaDeMaterias:
    if listaDeMaterias.index(materia) == 3: 
        print(materia)