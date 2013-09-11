#!/usr/bin/env python

class Figura:
    """Clase base de la jerarquia"""
    
    def __init__(self, nombre):
        self.__nombre = nombre
        
    def area(self):
        return "Clase base no tiene area"
    
    def perimetro(self):
        return "Clase base no tiene perimetro"
    
    def __str__(self):
        return "{0} : {1} : {2}".format(self.__nombre, self.area(), self.perimetro())
        
    def setNombre(self, n):
        self.__nombre = n;
        
    def unica(self):
        print("Solo existo en la base")


class Rectangulo (Figura):
    """Clase Rectangulo"""
    
    def __init__(self, nombre, ladoa, ladob):
        Figura.__init__(self, nombre)
        self.__ladoa = ladoa
        self.__ladob= ladob
        
    def area(self):
        return (self.__ladoa * self.__ladob)
        
    def perimetro(self):
        return (2 * (self.__ladoa + self.__ladob))
        
    def __str__(self):
        n = Figura.__str__(self)
        return "{0} : LA = {1} : LB = {2}".format(n, self.__ladoa, self.__ladob)
        
    def unica(self):
        print("ahora existo en Rectangulo")
     
class Cuadrado (Rectangulo):
    """Clase Cuadrado"""
    
    def __init__(self, nombre, lado):
        Rectangulo.__init__(self, nombre, lado, lado)
        
    
class Circulo (Figura):
    """Clase Circulo"""
    
    pi = 3.14159
    
    def __init__(self, nombre, radio):
        Figura.__init__(self, nombre)
        self.__radio = radio
        
    def area(self):
        return (self.__class__.pi * self.__radio * self.__radio)
        
    def perimetro(self):
        return (2 * self.__class__.pi * self.__radio)
        
    def __str__(self):
        n = Figura.__str__(self)
        return "{0} : R = {1} ".format(n, self.__radio)
        
        
def main():
    
    figuras = []
    
    opc = 1
    while opc != 0:
        tipo = int(input("Selecciona el tipo de figura (1-Cuadrado / 2-Rectangulo / 3-Circulo): "))
        nombre = input("Entra el nombre de la figura seleccionada: ");       
        if tipo == 1:
            lado = int(input("Entra el valor del lado del cuadrado: "))
            figuras.append(Cuadrado(nombre, lado))
        elif tipo == 2:
            ladoa = int(input("Entra el valor del lado A del rectangulo: "))
            ladob = int(input("Entra el valor del lado B del rectangulo: "))
            figuras.append(Rectangulo(nombre, ladoa, ladob))
        elif tipo == 3:
            radio = int(input("Entra el valor del radio del circulo: "))
            figuras.append(Circulo(nombre, radio))
        else:
            print("El tipo seleccionado no es valido")
        
        opc = int(input("Desea entrar otra figura (1-Si / 0-No) ?: "))
    
    for f in figuras:
        print(f)
        
main()

