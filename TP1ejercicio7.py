# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 11:39:47 2020

@author: Gisela Schierff

"""
'''
Ejercicio 7: Crear un programa que calcule el sueldo bruto de una persona que trabaja de lunes a viernes 8 hs y su pago por hora es de 400 pesos. Devolver el sueldo por pantalla.

'''

pagoPorHora = 400
horasPorDia = 8
diasPorSemana = 5
semanasPorMes = 4

pagoPorDia = pagoPorHora * horasPorDia 
pagoPorSemana = pagoPorDia * diasPorSemana
pagoPorMes = pagoPorSemana * semanasPorMes

print("El sueldo bruto es:", pagoPorMes)