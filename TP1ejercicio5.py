# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 11:08:01 2020

@author: Gisela Schierff
"""
'''
Ejercicio 5: Crear un programa que pida al usuario ingresar 2 números por teclado y devuelva por pantalla la suma de ellos en un renglón, la resta en otro, el producto en otros y la división en otro.
'''

primerNumero = int(input("Ingrese un número: "))
segundoNumero = int(input("Ingrese otro número: "))
 
suma = primerNumero + segundoNumero

resta = primerNumero - segundoNumero

producto = primerNumero * segundoNumero

division = primerNumero / segundoNumero

print()

print("La suma de ambos números es:", suma)
print("La resta de ambos números es:", resta)
print("El producto de ambos números es:", producto)
print("La división de ambos números es:", division)