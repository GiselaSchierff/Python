# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 14:27:05 2020

@author: Gisela Schierff
"""
'''
Ejercicio 3: Crear una función que, a partir de un mensaje, nos devuelva una 
lista con todos los números, si los hay, que aparecen en dicho mensaje.
'''

def numerosEnMensaje(mensaje): 
    listaDeNumeros = []
    for caracter in mensaje: 
        if caracter.isdigit(): 
            listaDeNumeros.append(caracter)
    print(listaDeNumeros)

numerosEnMensaje("tengo 27 años") 