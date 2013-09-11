#!/usr/bin/env python

class Filosofo:
    __nombre = "Platon"
    __edad = 200
    
    def Pensar(self):
        print("Estoy pensando")
        
    def Comer(self,comida):
        print("Estoy comiendo ", comida, " y soy", self.__nombre)
    
    def setNombre(self, n):
        self.__nombre = n
        
    def setEdad(self, e):
            self.__edad = e
            
    def getNombre(self):
        return self.__nombre
    
    def getEdad(self):
        return self.__edad
    
#Programa principal
Pedir numero de filosofos
Almacenarlo en una variable
    for( range(n))
        pedir nombre
        pedir edad
        pedir que come el filosofo
        Crear objeto filosofo Filosofo()
        f.setNombre()
        f.setEdad()
        f.Comer()
    

        
f1 = Filosofo()
f1.__edad = 50
f1.Pensar()
f1.Comer("pescado")
f2 = Filosofo()
f2.setNombre("Pepito")
f2.Comer("pizza")
