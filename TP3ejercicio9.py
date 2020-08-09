# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 15:58:53 2020

@author: Gisela Schierff

"""

'''
Ejercicio 9: Crear un diccionario con 10 estudiantes y sus respectivas notas. 
Luego crear una función que nos informe los estudiantes aprobados (nota >= 7),
los estudiantes desaprobados (4 <= nota < 7) y los estudiantes aplazados 
(0 <= nota < 4).
'''
notasDeEstudiantes = {"Eliza Riel" : 10, 
                      "Antonio Ramos" : 7,
                      "Manuel Medina" : 4,
                      "Alex Sen" : 1,
                      "Esteban Elif" : 5,
                      "Alonso Trix" : 2,
                      "Yanina Letter" : 6, 
                      "Walter Dieguez" : 4, 
                      "Quimey Raven" : 7, 
                      "Alan Tila" : 10                   
                      }
def informeDeEstudiantes(): 
    aprobados = {}
    desaprobados = {}
    aplazados = {}

    for nombre, nota in notasDeEstudiantes.items(): 
        if nota >= 7: 
            aprobados[nombre] = nota
        elif 4 <= nota < 7: 
            desaprobados[nombre] = nota
        elif nota < 4:
            aplazados[nombre] = nota
        else: 
            print("La nota ingresada no es válida")
    print(f"Los alumnos aprobados son: {aprobados}")
    print(f"Los alumnos desaprobados son: {desaprobados}")
    print(f"Los alumnos aplazados son: {aplazados}")
    
informeDeEstudiantes()