# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 11:51:53 2020

@author: Gisela Schierff
"""
'''
Ejercicio 3: Pedir al usuario que ingrese por teclado 2 números, si el primero es menor que el segundo imprimir la resta entre el segundo y el primero, si el primero es mayor que el segundo imprimir la suma de ambos, y si son iguales imprimir su producto.
'''

primerNumero = int(input("Ingrese un número: "))
segundoNumero = int(input("Ingrese otro número: "))
resta = segundoNumero - primerNumero
suma = primerNumero + segundoNumero
producto = primerNumero * segundoNumero

if primerNumero < segundoNumero:
    print("La resta de ambos números es:", resta)
elif primerNumero > segundoNumero: 
    print("La suma de ambos números es:", suma)
else: 
    print("El producto de ambos números es:", producto)