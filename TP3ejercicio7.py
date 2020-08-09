# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 15:29:06 2020

@author: Gisela Schierff
"""
'''
Ejercicio 7: Crear una función que verifique si una palabra es un palíndromo 
o no. En caso de que lo sea devolver por pantalla "La palabra es un 
palíndromo", en caso contrario, devolver "La palabra no es un palíndromo".

'''
def palindromo(palabra):
    palabraAlReves = palabra[::-1]
    if (palabra == palabraAlReves): 
        print("La palabra es un palíndromo")
    else: 
        print("La palabra no es un palíndromo")
palindromo("ala")