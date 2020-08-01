# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 19:32:34 2020

@author: Gisela Schierff
"""
'''
Ejercicio 15: Crear un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.
'''
diccionarioDeAsignaturas = {"Matemáticas" : 6, 
                            "Física" : 4, 
                            "Química" : 5}
totalDeCreditos = 0
for asignatura, creditos in diccionarioDeAsignaturas.items(): 
    print(f"{asignatura} tiene {creditos} créditos")
    totalDeCreditos += creditos
print("El total de los créditos para todas las materias es: ", totalDeCreditos) 