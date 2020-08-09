# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 15:08:48 2020

@author: Gisela Schierff
"""
'''
Ejercicio 6: Crear una función que devuelva por pantalla un mensaje 
ingresado por parámetro pero en modo Title. Si el mensaje ya está en modo 
title, que devuelva por pantalla "El mensaje ya está en modo title: {mensaje}"
'''

def enModoTitle(mensaje): 
    if (mensaje.istitle()): 
        print(f"El mensaje ya está en modo title: {mensaje}")
    else: 
        mensaje = mensaje.title()
        
        print(mensaje)

enModoTitle("soy gisela schierff")
    