# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 12:36:27 2020

@author: Usuario
"""
'''
Ejercicio 6: Escribir un programa que seleccione una operación de cuatro operaciones numéricas disponibles, una vez seleccionada la operación, introducir dos números y ejecutar la operación.
'''
operacion = int(input('''Seleccione la operación que desea realizar: 
                   1 - suma 
                   2 - resta
                   3 - multiplicación
                   4 - división'''))
print(operacion)
if 0 < operacion <= 4: 
    primerNumero = int(input("ingrese un número: "))
    segundoNumero = int(input("Ingrese otro número: "))

    if operacion == 1:
        suma = primerNumero + segundoNumero
        print("La suma de ambos números es:", suma)
    elif operacion == 2:
        resta = primerNumero - segundoNumero
        print("La resta de ambos números es:", resta)
    elif operacion == 3:
        multiplicacion = primerNumero * segundoNumero
        print("La multiplicación de ambos números es:", multiplicacion)
    else:
        division = primerNumero / segundoNumero
        print("La división de ambos números es:", division)
else: 
    print("Número de operación inválido")