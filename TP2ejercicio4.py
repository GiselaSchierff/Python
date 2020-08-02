# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 12:09:16 2020

@author: Gisela Schierff
"""
'''
Ejercicio 4: Ingresar 6 números por teclado, preferentemente enteros, ordenarlos de manera creciente e imprimirlos por pantalla.
'''

primerNumero = int(input("Ingrese el primer número: "))                   
segundoNumero = int(input("Ingrese el segundo número: "))
tercerNumero = int(input("Ingrese el tercer número: "))
cuartoNumero = int(input("Ingrese el cuarto número: "))
quintoNumero = int(input("Ingrese el quinto número: "))
sextoNumero = int(input("Ingrese el sexto número: "))
                   
listaDeNumeros = [primerNumero, segundoNumero, 
                  tercerNumero, cuartoNumero,
                  quintoNumero, sextoNumero]

listaDeNumeros.sort()
print()
print("La lista de números con orden ascendente es:", listaDeNumeros)
