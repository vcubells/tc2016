#!/usr/bin/env python

class Estudiante:
    """Clase estudiante"""

    count = 0;
    
    def __init__(self, nombre = None):
        self.__nombre = nombre
        self.__califs = []
        self.__class__.count += 1
        
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
        self.__nombre = input("Dame el nombre del estudiante: ")
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
    
    #Funcion con significado especial
    def __str__(self):
        promedio = self.__CalculaPromedio()
        return  "El promedio de {0} es {1} y soy un {2}".format(self.__nombre, promedio, self.__class__)
        
    def __del__(self):
        print("Me acaban de destruir")


#Programa principal
def main():
    nombre = input("Dame el nombre del estudiante: ")
    count = int(input("Cantidad de calificaciones: "))
    e1 = Estudiante(nombre)

    for i in range(count):
        calif = int(input("Dame la calificacion: "))
        e1.setCalif(calif)
    
    # e1.llenar()
    e1.__nombre = "josefa"

    print(e1)
    print(e1.count)
    e2 = Estudiante()
    print(e1.count)
    
main()





