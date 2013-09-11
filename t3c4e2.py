#!/usr/bin/env python

class Libro:
    """Clase que modela un Libro"""
    # Atributos miembros de la clase
    contador = 0
    
    # Metodo de inicializacion
    def __init__(self, isbn = '', autor = '', pags = 0):
        # Atributos de datos
        self.__isbn = isbn
        self.__autor = autor
        self.__pags = pags
        self.__class__.contador += 1 # Variable de clase
        
    def __str__(self):
        return "El libro " + self.__isbn + "fue escrito por " + self.__autor
    
    @classmethod 
    def instances(clase):
        print("Llevamos {0} libros".format(clase.contador)) 
    
    def __del__(self):
        print("Me acaban de destruir")

def main():
    l1 = Libro()
    print(l1.__doc__)
    Libro.instances()
    print(l1)
    
    l2 = Libro("5678", "Juan Perez")
    print(l2.__doc__)
    l2.instances()
    print(l2)
    
    l3 = Libro(pags = 500, autor = "Josefa")
    print(l3.__doc__)
    Libro.instances()
    print(l3)
    

main()


