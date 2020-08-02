# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 11:33:04 2020

@author: Gisela Schierff
"""

'''
Ejercicio 2: Crear una lista con 10 números enteros cualquiera. Indicar cuál es el número mayor y cuál es el número menor. Si al menos hay 3 números mayores a 100, imprimir esos números, si no, imprimir los números menores a 50 que formen parte de la lista.
'''
listaDeNumeros = [ 254, 2546, 563, 33, 78, 3, 4, 8, 4, 45]

listaDeNumeros.sort()

numerosMayoresA100 = []

mayorNumero = listaDeNumeros[-1]
menorNumero = listaDeNumeros[0]
print("El mayor número de la lista es", mayorNumero, "y el menor es", menorNumero)

for numero in listaDeNumeros: 
    if numero > 100:
        numerosMayoresA100.append(numero)

if len(numerosMayoresA100):
    print("Los números mayores a 100 son:", numerosMayoresA100)
else:
    for numero in listaDeNumeros: 
        if numero < 50:
            numerosMenoresA50 = []
            numerosMenoresA50.append(numero)
    print("Los números menores a 50 son:", numerosMenoresA50)
        