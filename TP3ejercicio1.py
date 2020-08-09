# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 13:57:20 2020

@author: Gisela Schierff
"""
'''
Ejercicio 1: Crear una función que, a partir de un dato de entrada que sea 
en horas, nos informe cuántos minutos y cuántos segundos serían esas horas.
Imprimir por pantalla dichos valores.
'''


def minutosYSegundos(horas): 
    minutos = 60 * horas
    segundos = 60 * minutos 
    
    print(f"La cantidad de horas dadas, {horas}, equivale a {minutos} minutos y a {segundos} segundos")

minutosYSegundos(10)