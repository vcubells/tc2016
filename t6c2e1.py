#!/usr/bin/env python

class CadenaVaciaError(Exception):
    def __init__(self, campo):
        self.__campo = campo
        
    def __str__(self):
        return "El campo {0} no puede ser vacio".format(self.__campo)

class RangoError(Exception):
    def __init__(self, campo, inferior, superior):
        self.__campo = campo
        self.__inferior = inferior
        self.__superior = superior
        
    def __str__(self):
        return "El campo {0} debe estar en el rango [{1}..{2}]".format(self.__campo, self.__inferior, self.__superior)

class Estudiante:
    def __init__(self, nombre, apellidos, edad, matricula):
        self.setNombre(nombre)
        self.setApellidos(apellidos)
        self.setEdad(edad)
        self.setMatricula(matricula)
        self.__materias = []
        
    def setNombre(self, nombre):
        if nombre == '':
            raise CadenaVaciaError('Nombre')
        else:
            self.__nombre = nombre
            
    def setApellidos(self, apellidos):
        if apellidos == '':
            raise CadenaVaciaError('Apellidos')
        else:
            self.__apellidos = apellidos
            
    def setMatricula(self, matricula):
        if matricula == '':
            raise CadenaVaciaError('Matricula')
        else:
            self.__matricula = matricula
            
    def setEdad(self, edad):
        if edad < 17 or edad > 30:
            raise RangoError('Edad', 17, 30)
        else:
            self.__edad = edad
            
    def setMateria(self, materia):
        self.__materias.append(materia)
    
    def __str__(self):
        cad = 'Materias: '
        for i in self.__materias:
            cad += i.__str__()
        
        return "{0} {1} {2} {3} {4}".format(self.__matricula, self.__nombre, self.__apellidos, self.__edad, cad)

class Materia:
    def __init__(self, codigo, nombre, calif):
        self.setNombre(nombre)
        self.setCodigo(codigo)
        self.setCalificacion(calif)
        
    def setNombre(self, nombre):
        if nombre == '':
            raise CadenaVaciaError('Nombre')
        else:
            self.__nombre = nombre
            
    def setCodigo(self, codigo):
        if codigo == '':
            raise CadenaVaciaError('Codigo')
        else:
            self.__codigo = codigo
            
    def setCalificacion(self, calif):
        if calif < 0 or calif > 100:
            raise RangoError('Calificacion', 0, 100)
        else:
            self.__calif = calif
    
    def __str__(self):
        return "{0} {1} {2}".format(self.__codigo, self.__nombre, self.__calif)
        
def main():
    try:
        poo = Materia('TC2016', ' Programacion Orientada a Objetos', 100)
        bd = Materia('TC1020', ' Bases de datos', 90)
        pa = Materia('', ' Programacion Avanzada', 50)
    
        javier = Estudiante('Javier', 'Jobs', 20, 'A01010101')
        javier.setMateria(poo)
        javier.setMateria(bd)
    
        bill = Estudiante('Bill', 'Gates', 30, 'A02020202')
        bill.setMateria(pa)
    
        print(javier)
        print(bill)
    except RangoError as e:
        print(e)
    except CadenaVaciaError as e:
        print(e)
    
main()