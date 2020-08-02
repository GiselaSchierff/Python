# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 14:25:59 2020

@author: Gisela Schierff
"""
'''
Ejercicio 9: Pedirle al usuario que ingrese el monto disponible en su tarjeta de crédito. Evaluar si puede realizar una compra de $2500, si puede indicar cuánto saldo le queda luego de efectuarla. Si no puede, indicar cuánto dinero le falta para poder realizarla.
'''

saldoDisponible = int(input("Ingrese el saldo de su tarjeta de crédito: "))

if saldoDisponible >= 2500: 
    saldoDespuesDeCompra = saldoDisponible - 2500
    print("El saldo luego de la compra es:", saldoDespuesDeCompra)
else: 
    saldoFaltante = 2500 - saldoDisponible
    print("El saldo faltante para la compra es:", saldoFaltante)