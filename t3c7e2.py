#!/usr/bin/env python

class Producto:
    """Clase que modela un producto"""
    
    def __init__(self, desc = 'Desconocido', precio = 0.0, stock = 0):
        self.__descripcion = desc
        self.__precio = precio
        self.__stock = stock
        
    def getStock(self):
        return self.__stock
    
    def setStock(self, nuevoStock):
        self.__stock = nuevoStock
        
    def getPrecio(self):
        return self.__precio
        
    def actualizaStock(self, valor):
        self.__stock -= valor
        
    def hayStock(self, valor):
        return (self.__stock >= valor)
        
    def __str__(self):
        return "{0} {1} {2}".format(self.__descripcion, self.__precio, self.__stock)
    

class Componente:
    """Clase que modela un componente"""
    
    def __init__(self, prod, cant = 0):
        self.__producto = prod
        self.__cantidad = cant
        
    def __str__(self):
        return "{0} : {1}".format(self.__producto.__str__(), self.__cantidad)
        
class Platillo:
    """Representacion de un platillo"""
    
    def __init__(self, descripcion='Sin nombre'):
        self.__descripcion = descripcion
        self.__precio = 0.0
        self.__componentes =[]
        
    def addComponente(self, prod, cant):
        if prod.hayStock(cant):
            c = Componente(prod, cant)
            self.__componentes.append(c)
            prod.actualizaStock(cant)
            self.__precio += prod.getPrecio() * cant
        else:
            print("No se puede adiconar el componente porque no hay stock disponible")
        
    def __str__(self):
        return "{0} {1}".format(self.__descripcion, self.__precio)
        
    def imprime(self):
        print(self)
        print("Componentes:")
        for c in self.__componentes:
            print(c)

def main():
    
    #Lista de platillos
    menu = []
    
    p1 = Producto('Tortilla', 1, 100)
    
    enchiladas = Platillo("Enchiladas")
    
    enchiladas.addComponente(p1, 3)
    
    enchiladas.imprime()
    
main()