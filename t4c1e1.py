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
    figura = Figura("Figura")
    print(figura)
        
    rect = Rectangulo("Rectangulo", 10, 5)
    print(rect)
    
    cuad = Cuadrado("Cuadrado", 5)
    print(cuad)
    
    circu = Circulo("Circulo", 5)
    circu.setNombre("Circulo modificado")
    print(circu)
        
main()