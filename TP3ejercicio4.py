# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 14:36:38 2020

@author: Gisela Schierff
"""
'''
Ejercicio 4: Crear una función que, a partir de 4 números, devuelva el mayor
producto de dos de ellos. Imprimir resultado por pantalla.
'''

def mayorProducto(primerNumero = 0, segundoNumero = 0, tercerNumero = 0, cuartoNumero = 0): 
    prod1y2 = primerNumero * segundoNumero
    prod1y3 = primerNumero * tercerNumero
    prod1y4 = primerNumero * cuartoNumero
    prod2y3 = segundoNumero * tercerNumero
    prod2y4 = segundoNumero * cuartoNumero
    prod3y4 = tercerNumero * cuartoNumero
    maxProd = max(prod1y2, prod1y3, prod1y4, prod2y3, prod2y4, prod3y4)
    print("El mayor producto entre los cuatro numeros dados es:", maxProd)
mayorProducto(10, 5, 2, 1)

