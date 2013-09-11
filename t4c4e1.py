#!/usr/bin/env python

class Persona:
    def __init__(self, nombre = 'Desconocido', edad = 0):
        self.__nombre = nombre
        self.__edad = edad
        
    def getEdad(self):
        return self.__edad
        
    def __str__(self):
        return "{0} de {1}".format(self.__nombre, self.__edad)
        
        
    def __lt__(self, otro):
        return (self.__edad < otro.__edad)
        
    def __add__(self, otro):
        return Persona('Total', self.__edad + otro.__edad)

    def __iadd__(self, otro):
         self.__edad += otro.__edad
         return self
        
    def __lshift__(self, otro):
        self.__edad = self.__edad << 1

        
def main():
    
    juan = Persona('Juan', 25)
    maria = Persona('Maria', 30)
    
    personas = []
    personas.append(juan)
    personas.append(maria)
    personas.append(Persona(edad = 55))
    personas.append(Persona(edad = 15))
    
    lp = len(personas) - 1
    for i in range(lp):
        for j in range(lp):
            if (personas[i] > personas[j]):
                temp = personas[i]
                personas[i] = personas[j]
                personas[j] = temp
                
   
    for p in personas:
        print(p)
    
    
    
    suma = Persona()
    
    for p in personas:
        suma += p
    
    print ("Edad promedio: " + str(( suma.getEdad() / len(personas))))
    
    
main()