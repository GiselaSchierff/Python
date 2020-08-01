# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 17:34:12 2020

@author: Gisela Schierff
"""
'''
Ejercicio 13: Crear un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
'''
diccionarioDeDivisas = {"Euro":'€', 
                        "Dollar":'$', 
                        "Yen":'¥'}

divisa = input("Ingrese una divisa: ")

if divisa in diccionarioDeDivisas:
    print(diccionarioDeDivisas[divisa])
else: 
    print("Divisa ingresada no válida")
    

