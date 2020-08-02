# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 14:03:20 2020

@author: Gisela Schierff
"""

'''
Ejercicio 7: Crear un diccionario con 5 estudiantes y sus respectivas notas. Imprimir por pantalla los alumnos que aprobaron y su nota (no en forma de diccionario, si no con nombre : nota). Tener en cuenta que para aprobar el alumno debe sacarse una nota mayor o igual a 7 y menor o igual a 10.
'''

diccionarioDeAlumnos = {"Ignacio Areco" : 5,
                        "Marcos Alvarez" : 2,
                        "Scarlet Savin" : 7,
                        "Alberto Ramos" : 10,
                        "Tatiana Lares" : 9}

for alumno, nota in diccionarioDeAlumnos.items(): 
    if nota >= 7: 
        print(f"{alumno}: {nota}")
    