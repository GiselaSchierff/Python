# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 12:02:35 2020

@author: Giseña Schierff
"""
'''
Ejercicio 9: Crear un programa que pregunte al usuario 5 números enteros y devuelva una lista con ellos.

'''

primerNumeroEntero = int(input("Ingrese el primer número entero: "))
segundoNumeroEntero = int(input("Ingrese el segundo número entero: "))
tercerNumeroEntero = int(input("Ingrese el tercer número entero: "))
cuartoNumeroEntero = int(input("Ingrese el cuarto número entero: "))
quintoNumeroEntero = int(input("Ingrese el quinto número entero: "))

listaDeNumerosEnteros = [primerNumeroEntero, 
                         segundoNumeroEntero, 
                         tercerNumeroEntero, 
                         cuartoNumeroEntero, 
                         quintoNumeroEntero]
print()

print("La lista de los números enteros ingresados es:", listaDeNumerosEnteros)