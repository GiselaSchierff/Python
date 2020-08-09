# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 16:06:07 2020

@author: Gisela Schierff
"""
'''
Ejercicio 10: Crear una función decoradora para una función matemática cualquiera.

'''
def decorarSuma(sumar):
    def decoracion(*args): 
        print("La suma de los nñumeros dados es: ")
        sumar(*args)
    return decoracion

@decorarSuma

def sumar(a = 0, b = 0): 
    print(a + b)
    
sumar(10, 5)