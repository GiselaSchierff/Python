# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 14:10:35 2020

@author: Gisela Schierff
"""
'''
Ejercicio 8: Pedirle al usuario que ingrese por teclado 3 números binarios de 8 bits, para cada uno imprimir su siguiente (número + 1) pero en sistema decimal. Recuerden que los números binarios están compuestos por 1 y 0.
'''
numeroDecimal = 0
for numero in range(3): 
    binario = input("Ingrese un número en binario de 8 bits: ")
    for bit in binario: 
        numeroDecimal += numeroDecimal + int(bit)
    print(numeroDecimal)
    numeroDecimal = 0
