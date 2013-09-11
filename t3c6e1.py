#!/usr/bin/env python

#!/usr/bin/env python
class Autor:
    """Clase que modela un autor"""
    # Metodo de inicializacion
    def __init__(self, nombre = '', apellidos = '', telefono = ''):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__telefono = telefono
        
    def __str__(self):
        return "{0} {1} {2}".format(self.__nombre, self.__apellidos, self.__telefono)
    

class Libro:
    """Clase que modela un Libro"""
    # Atributos miembros de la clase
    contador = 0
    
    # Metodo de inicializacion
    def __init__(self, isbn = '', pags = 0):
        # Atributos de datos
        self.__isbn = isbn
        self.__autores = []     #Lista de autores
        self.__pags = pags
        self.__class__.contador += 1 # Variable de clase
        
    def setAutor(self, autor):
        self.__autores.append(autor)
        
    def __str__(self):
        cad = ''
        if len(self.__autores) == 0:
            cad = 'Autor desconocido'
        else:
            for a in self.__autores:
                cad = cad + ', ' + a.__str__() 
        return "El libro " + self.__isbn + "fue escrito por " + cad
    
    @classmethod 
    def instances(clase):
        print("Llevamos {0} libros".format(clase.contador)) 
    

def main():
    # Creacion de autores
    a1 = Autor('Juana', 'Bacallao')
    a2 = Autor('Albertina', 'Storni', '78387383')
    a3 = Autor('Mario', 'Vargas Llosa')
    a4 = Autor('Gabriel', 'Garcia Marquez')
    
    l1 = Libro()
    l1.setAutor(a1)
    l1.setAutor(a2)    
    print(l1.__doc__)
    Libro.instances()
    print(l1)
    
    l2 = Libro("5678")
    l2.setAutor(a3)
    l2.setAutor(a4)
    l2.setAutor(a1)
    print(l2.__doc__)
    l2.instances()
    print(l2)
        
    l3 = Libro(pags = 500)
    print(l3.__doc__)
    Libro.instances()
    print(l3)
    

main()




