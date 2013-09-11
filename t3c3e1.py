#!/usr/bin/env python

class Estudiante:
    __nombre = ''
    __califs = []
    
    def setNombre(self, n):
        self.__nombre = n
        
    def getNombre(self):
        return self.__nombre
    
    def setCalif(self, c):
        if (c >= 0 and c < 101):
            self.__califs.append(c)
        
    def getCalif(self, index):
        return self.__califs[index-1]
        
    #Funcion de acceso
    def llenar(self):
        self.__nombre = raw_input("Dame el nombre del estudiante: ")
        count = int(input("Cantidad de calificaciones: "))
        for i in range(count):
            calif = int(input("Dame la calificacion: "))
            self.setCalif(calif)
    
    # Funcion de utilidad
    def __CalculaPromedio(self):
        suma = 0
        num = len(self.__califs)
        for i in range(num):
            suma += self.__califs[i]
        return suma/num
    
    #Funcion de acceso
    def imprime(self):
        promedio = self.__CalculaPromedio()
        print(self.__nombre, promedio)

#Programa principal
def main():
    e1 = Estudiante()
    e1.llenar()
    e1.imprime()
    
main()





