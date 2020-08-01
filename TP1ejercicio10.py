# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 12:10:00 2020

@author: Gisela Schierff
"""
'''
Ejercicio 10: Escribir un programa que almacene todas las letras del abecedario y luego elimine las vocales y nos devuelva una lista sin las vocales, sin modificar la original.Ejercicio 2: Crear un programa Ejercicio 2: Crear un programa en el cual se almacene en una variable el string "Hola Mundo!" y luego se imprima por pantalla dicha variable.
'''

listaConAbecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
                      'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
                      'u', 'v', 'w', 'x', 'y', 'z']

listaConVocales = ['a', 'e', 'i', 'o', 'u']

listaSinVocales = listaConAbecedario.copy()

for letra in listaSinVocales: 
   
    for vocal in listaConVocales: 
        if letra == vocal: 
            listaSinVocales.remove(letra)
              
print()
print(listaSinVocales)