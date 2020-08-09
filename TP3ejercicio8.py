# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 15:35:43 2020

@author: Usuario
"""
'''
Ejercicio 8: Crear una función que calcule cuántos litros de nafta gasta 
un auto que consume 2 litros x 100km, en un viaje ida y vuelta MdP-Bue si 
la distancia es de 400km. Luego crear una función que, a partir de esos 
datos, devuelva cuánto significa eso en pesos si el litro de nafta está 60$.
'''

def viaje(): 
    distancia = 400 
    idaYvuelta = distancia * 2
    consumoAuto = 2/100
    viajeAuto = idaYvuelta * consumoAuto
    return viajeAuto
    
viaje()


def dineroViaje(litros): 
    dineroAGastar = 60 * litros 
    print("El dinero a gastar es:", dineroAGastar)
       
print("Los litros de nafta necesarios son:", viaje())
print("")
dineroViaje(viaje())