# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 17:59:24 2020

@author: Gisela Schierff
"""
'''
Ejercicio 14: Crear un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje.
'''

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
direccion = input("Ingrese su dirección: ")
telefono = input("Ingrese su número de teléfono: ")
               
diccionarioDeDatos = {}
diccionarioDeDatos["Nombre"] = nombre 
diccionarioDeDatos["Edad"] = edad
diccionarioDeDatos["Dirección"] = direccion,
diccionarioDeDatos["Teléfono"] = telefono
print(diccionarioDeDatos)