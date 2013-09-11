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
    def __init__(self, isbn = '', autor = 0, pags = 0):
        # Atributos de datos
        self.__isbn = isbn
        self.__autor = autor
        self.__pags = pags
        self.__class__.contador += 1 # Variable de clase
        
    def __str__(self):
        cad = ''
        if self.__autor == 0 :
            cad = 'Autor desconocido'
        else:
            cad = self.__autor.__str__();
        return "El libro " + self.__isbn + "fue escrito por " + cad
    
    @classmethod 
    def instances(clase):
        print("Llevamos {0} libros".format(clase.contador)) 
    

def main():
    # Creacion de autores
    a1 = Autor('Juana', 'Bacallao')
    a2 = Autor('Albertina', 'Storni', '78387383')
    
    l1 = Libro(autor = a2)
    print(l1.__doc__)
    Libro.instances()
    print(l1)
    
    l2 = Libro("5678", a1)
    print(l2.__doc__)
    l2.instances()
    print(l2)
        
    l3 = Libro(pags = 500, autor = a2)
    print(l3.__doc__)
    Libro.instances()
    print(l3)
    

main()


