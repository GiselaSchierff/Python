# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 10:57:11 2020

@author: Gisela Schierff
"""
'''
Ejercicio 6: Crear un programa que calcule cuánto dinero tendré al cabo de un mes si deposito hoy 2000 en el banco y el interés mensual es de 5%, y luego devuelva por pantalla ese valor.
'''

deposito = 2000

interes = 5 / 100
 
saldo = deposito + (deposito * interes)
print("El saldo disponible al cabo de un mes es:",saldo)