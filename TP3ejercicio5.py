# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 14:50:30 2020

@author: Gisela Schierff
"""
'''
Ejercicio 5: Crear una función que devuelva True si los parámetros 
ingresados son todos números, False si hay al menos uno de los parámetros 
ingresados que no es un número, y None si ninguno de los parámetros ingresados
es un número. Imprimir resultado por pantalla.
'''

def todosNumeros(*args): 
    listaDeParametros = []
    for parametro in args: 
        if type(parametro) == int or type(parametro) == float or type(parametro) == complex: 
            listaDeParametros.append(parametro)
    if len(listaDeParametros) == len(args): 
        return True
    elif len(listaDeParametros) != 0: 
        return False
    else:  
        return None
    
print(todosNumeros("a", "df"))