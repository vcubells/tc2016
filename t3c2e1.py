#!/usr/bin/env python

class Reloj:
    __hora = 0
    __min = 0
    __seg = 0
    __nombre = ''
    __diferencia = 0
    
    def setHora(self, h):
        if (h < 0 or h > 23):
            self.__hora = 0
        else:
            self.__hora = h
    
    def setMin(self, m):
        if (m < 0 or m > 59):
            self.__min = 0
        else:
            self.__min = h
      
    def setSeg(self, s):
        if (s < 0 or s > 59):
            self.__seg = 0
        else:
            self.__seg = h
            
    def setNombre(self, n):
        self.__nombre = n
          
    def setDiferencia(self, d):
        self.__diferencia = d
        
    def getHora(self):
        return self.__hora
    
    def getMin(self):
        return self.__min
    
    def getSeg(self):
        return self.__seg
    
    def getNombre(self):
        return self.__nombre
    
    def getDiferencia(self):
        return self.__diferencia
    
    def estableceHora(self, h, m, s):
        self.__hora = h + self.__diferencia
        if (self.__hora < 0):
            self.__hora += 24
        self.__min = m
        self.__seg = s
        self.imprime()
        
    def imprime(self):
        print(self.__nombre, " : ", self.__hora, " : ", self.__min, " : ", self.__seg)
    
def main():
    # Crear objeto de hora local
    mexico = Reloj()
    mexico.setNombre("Mexico")
    mexico.setHora(11)
    
    # Objeto que representa una ciudad
    ensenada = Reloj()
    ensenada.setNombre("Ensenada")
    ensenada.setDiferencia(-2)
    
    # Objeto que represeta otra ciudad
    paris = Reloj()
    paris.setNombre("Paris")
    paris.setDiferencia(5)
    
    # Cambiar la hora local y actualizar los relojes
    for i in range(1, 10, 2):
        mexico.estableceHora(i,30,45)
        hora = mexico.getHora()
        minutos = mexico.getMin()
        seg = mexico.getSeg()
        
        ensenada.estableceHora(hora, minutos, seg)
        paris.estableceHora(hora, minutos, seg)

        
main()