# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 10:10:31 2020

@author: Gisela
"""
'''
Ejercicio único

Crear una clase llamada Punto con sus dos coordenadas X e Y.
Añadir un método constructor para crear puntos fácilmente. Si no se recibe una coordenada, su valor será cero.
Sobreescribir el método string, para que al imprimir por pantalla un punto aparezca en formato (X,Y)
Añadir un método llamado cuadrante que indique a qué cuadrante pertenece el punto, teniendo en cuenta que si X == 0 e Y != 0 se sitúa sobre el eje Y, si X != 0 e Y == 0 se sitúa sobre el eje X y si X == 0 e Y == 0 está sobre el origen.
Añadir un método llamado vector, que tome otro punto y calcule el vector resultante entre los dos puntos.
(Optativo) Añadir un método llamado distancia, que tome otro punto y calcule la distancia entre los dos puntos y la muestre por pantalla. La fórmula es la siguiente:

Nota:

La función raíz cuadrada en Python sqrt() se debe importar del módulo math y utilizarla de la siguiente forma:

import math
math.sqrt(9)
 
'''
# Crear una clase llamada Punto con sus dos coordenadas X e Y.

class Punto: 
# Añadir un método constructor para crear puntos fácilmente. Si no se recibe una coordenada, su valor será cero.
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
# sobreescribir el método string, para que al imprimir por pantalla un punto aparezca en formato (X,Y)  
    def String(self): 
       print(f"({self.x}, {self.y})")


# Añadir un método llamado cuadrante que indique a qué cuadrante pertenece el punto, teniendo en cuenta que si X == 0 e Y != 0 se sitúa sobre el eje Y, si X != 0 e Y == 0 se sitúa sobre el eje X y si X == 0 e Y == 0 está sobre el origen.

    def cuadrante(self):
        
        if (self.x == 0 and self.y == 0): 
            print(f"El punto dado se encuentra en el origen de coordenadas")
        elif (self.x > 0 and self.y > 0): 
            print(f"El punto dado se encuentra en el cuandrante I")
        elif (self.x < 0 and self.y > 0): 
            print(f"El punto dado se encuentra en el cuandrante II")
        elif (self.x < 0 and self.y < 0):
            print(f"El punto dado se encuentra en el cuandrante III")
        elif (self.x > 0 and self.y < 0):
            print(f"El punto dado se encuentra en el cuandrante VI")
        elif (self.x == 0 and self.y != 0):
            print(f"El punto dado se encuentra en el eje Y")
        elif (self.x != 0 and self.y == 0):
            print(f"El punto dado se encuentra en el eje X")
            
# Añadir un método llamado vector, que tome otro punto y calcule el vector resultante entre los dos puntos.
    def vector(self, otroX = 0, otroY = 0): 
    
        resultanteX = (otroY - self.y)
        resultanteX = (otroX - self.x)
       
        print(f"El vector resultante entre ambos vectores es: ({otroX - self.x}, {otroY - self.y})") 

 # Optativo) Añadir un método llamado distancia, que tome otro punto y calcule la distancia entre los dos puntos y la muestre por pantalla. 
    def distancia(self, nuevoX, nuevoY): 
        import math 
        calculoDeX = nuevoX - self.x
        calculoDeY = nuevoY - self.y
        xALa2 = calculoDeX * calculoDeX
        yALa2 = calculoDeY * calculoDeY
        interiorDeRaiz = yALa2 + xALa2
        print("La distancia entre ambos puntos es de", math.sqrt(interiorDeRaiz))
        return math.sqrt(interiorDeRaiz)
        
            


'''
Crear una clase llamada Rectángulo con dos puntos (inicial y final) que formarán la diagonal del rectángulo.
Añadir un método constructor para crear ambos puntos fácilmente, si no se envían se crearán dos puntos en el origen por defecto.
Añadir al rectángulo un método llamado base que muestre la base.
Añadir al rectángulo un método llamado altura que muestre la altura.
Añadir al rectángulo un método llamado area que muestre el area.
Sugerencia:

Pueden identificar fácilmente estos valores si intentan dibujar el cuadrado a partir de su diagonal. Recuerden que pueden utilizar la función abs() para saber el valor absoluto de un número.

'''
# Crear una clase llamada Rectángulo con dos puntos (inicial y final) que formarán la diagonal del rectángulo.
class Rectangulo: 
# Añadir un método constructor para crear ambos puntos fácilmente, si no se envían se crearán dos puntos en el origen por defecto. 
    def __init__(self, puntoInicial = Punto(), puntoFinal =  Punto()): 
        self.puntoInicial = puntoInicial
        self.puntoFinal = puntoFinal
        
# Añadir al rectángulo un método llamado base que muestre la base.
    def base(self, inicialEnX, finalEnX): 
        global base
        base = self.puntoFinal.x - self.puntoInicial.x
        
        print(f"La base se encuentra en {base} ")
# Añadir al rectángulo un método llamado altura que muestre la altura.
    def altura(self, inicialEnY, finalEnY): 
        global altura
        altura = self.puntoFinal.y - self.puntoInicial.y
        print(f"La altura se encuentra en {altura}")
# Añadir al rectángulo un método llamado area que muestre el area.

    def area(self, base, altura):
        area = altura * base
        print(f"El area es {area}")
'''
Experimentación
Crear los puntos A(2, 3), B(5,5), C(-3, -1) y D(0,0) e imprimelos por pantalla.
Consultar a qué cuadrante pertenecen el punto A, C y D.
Consultar los vectores AB y BA.
(Optativo) Consultar la distancia entre los puntos 'A y B' y 'B y A'.
(Optativo) Determinar cual de los 3 puntos A, B o C, se encuentra más lejos del origen, punto (0,0).
Crear un rectángulo utilizando los puntos A y B.
Consultar la base, altura y área del rectángulo.

'''        
# Crear los puntos A(2, 3), B(5,5), C(-3, -1) y D(0,0) e imprimelos por pantalla.

A = Punto(2, 3)
A.String()

B = Punto(5, 5)
B.String()

C = Punto(-3, -1)
C.String()

D = Punto(0, 0)
D.String()

# Consultar a qué cuadrante pertenecen el punto A, C y D.

A.cuadrante()
D.cuadrante()
C.cuadrante()

# Consultar los vectores AB y BA.

A.vector(5, 5)
B.vector(2, 3)

# (Optativo) Consultar la distancia entre los puntos 'A y B' y 'B y A'.

A.distancia(5, 5)
B.distancia(2, 3)

# (Optativo) Determinar cual de los 3 puntos A, B o C, se encuentra más lejos del origen, punto (0,0).

A.distancia(0, 0)
B.distancia(0, 0)
C.distancia(0, 0)

if (abs(A.distancia(0, 0)) > abs(B.distancia(0, 0)) and abs(A.distancia(0, 0)) > abs(C.distancia(0,0))):
    print("El punto A se encuentra más lejos del origen que los puntos B y C")
elif (abs(B.distancia(0, 0)) > abs(A.distancia(0, 0)) and abs(B.distancia(0, 0) > abs(C.distancia(0, 0)))): 
    print("El punto B se encuentra más lejos del origen que los puntos A y C")
elif (abs(C.distancia(0, 0)) > abs(A.distancia(0, 0)) and abs(C.distancia(0, 0) > abs(B.distancia(0, 0)))): 
    print("El punto C se encuentra más lejos del origen que los puntos A y B")
else: 
    print("No hay un punto que tenga mayor distancia del origen de coordenadas que los demás")
    
#Crear un rectángulo utilizando los puntos A y B.

R = Rectangulo(A, B)

# Consultar la base, altura y área del rectángulo.

R.base(2, 5)
R.altura(3, 5)
R.area(base, altura)

# pruebas propias
puntito = Punto(2,3)       
puntito.String()
puntito.cuadrante()
puntito.vector(1,1)
puntito.distancia(2, 2)