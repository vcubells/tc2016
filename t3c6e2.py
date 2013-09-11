#!/usr/bin/env python

#!/usr/bin/env python
class Autor:
    """Clase que modela un autor"""
    # Metodo de inicializacion
    def __init__(self, nombre = '', apellidos = '', telefono = ''):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__telefono = telefono
    
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def getApellidos(self):
        return self.__apellidos
    
    def setApellidos(self, apellidos):
        self.__apellidos = apellidos
        
    def getTelefono(self):
        return self.__telefono
    
    def setTelefono(self, telef):
        self.__telefono = telef
        
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
    
    def getAutor(self, index):
        if (index >= 0 and index < len(self.__autores)):
            return self.__autores[index]
        else:
            return "No existe autor con ese id"        
        
    def setAutor(self, autor):
        self.__autores.append(autor)
    
    def getAutores(self):
        return self.__autores
    
    def setAutores(self, autores):
        self.__autores = autores
    
    def getISBN(self):
        return self.__isbn
    
    def setISBN(self, isbn):
        self.__isbn = isbn
        
    def getPaginas(self):
        return self.__pags
    
    def setPaginas(self, paginas):
        self.__pags = paginas
    
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
    # Colecciones de objetos
    autores = []
    libros = []
    
    #Llenar la lista de autores
    cond = 1
    while cond != 0:
        nombre = input("Entra el nombre del autor: ")
        apellidos = input("Entra los apellidos del autor: ")
        telefono = input("Entra el telefono del autor: " )
        autor = Autor(nombre, apellidos, telefono)
        autores.append(autor)
        
        #Desea continuar?
        cond = int(input("Desea adicionar otro autor? 0 (no) / 1 (si): "))
   
    
    #Llenar la lista de libros
    cond = 1
    while cond != 0:
        isbn = input("Entra el ISBN: ")
        pags = int(input("Entra el numero de pags: "))
                
        libro = Libro(isbn, pags)
        
        #Adicionar autores al libro
        cond2 = 1
        while cond2 != 0:
            print("---- Selecciona un autor ----- ")
            contador = 0
            for a in autores:
                print(contador, a)
                contador += 1

            opc = -1

            num_autores = len(autores) - 1
            
            while (opc < 0 or opc > num_autores ):
                opc = int(input("Selecciona el id del autor: "))

            libro.setAutor(autores[opc])
            
            #Desea adicionar otro autor?
            cond2 = int(input("Desea adicionar otro autor al libro? 0 (no) / 1 (si): "))
        
        libros.append(libro)
        
        #Desea adicionar otro libro?
        cond = int(input("Desea adicionar otro libro? 0 (no) / 1 (si): "))   
    
    #Generar reportes
    
    #Listado de libros con toda su informacion
    print(" ////// Listado de libros con autores \\\\\\")
    for l in libros:
        print(l)
        
    #Listado de libros de un autor
    nombre = input("Nombre del autor a buscar: ");
    print("***** Libros escritos por {0} ********* ".format(nombre))
    
    for l in libros:
        for a in l.getAutores():
            if a.getNombre() == nombre:
                print(l)
                
                
                

    l.setISBN(l)
    Libro.setISBN()
    
    l.instances(l.__class__())
    Libro.instances(Libro)
    
main()






