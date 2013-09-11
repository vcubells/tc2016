#!/usr/bin/env python





class Edificio:



    __pisos=[]

    __elevadores =[]



    def __init__(self,locales,elevadores,pisos):

        

        #llena la lista de elevadores

        con = elevadores

        for n in range(0,con):

            

            self.setElevadores(Elevador(1))

            print(self.__elevadores[n].__str__())

        

        #llena la lista de locales

        count = pisos

        for i in range(0,count):

            

            self.setPisos(Piso(locales))

            print(self.__pisos[i].__str__())

        

    def setPisos(self,L):

        self.__pisos.append(L)



    def setElevadores(self,e):

        self.__elevadores.append(e)



    def getElevadores(self):

        return self.__elevadores



    def getPisos(self):

        return self.__pisos

    





    def __str__(self):

        return " {0} locales".format(self.__locales)



class Piso:

    __locales=[]



    def __init__(self,locales):

    

        count = locales

        for i in range(0,count):

            

            self.setLocales(Local("20 watts ","23 grados ",0,0))

            print(self.__locales[i].__str__())

            

    def setLocales(self,lo):

        self.__locales.append(lo)

    def getLocales(self):

        return self.__locales

    

    def __str__(self):

        return "Siguiente piso"

    

class Elevador:

    def __init__(self, estado):

        self.__estado = estado

    def setEstado(self,e):

        self.__estado = e

    def __str__(self):

        return "El elevador esta {0}".format(self.__estado)





class Local:



    def __init__(self,luces,calefaccion,incendio,aspersores):

        self.__luces = Luces(luces)

        self.__calefaccion = Calefaccion(calefaccion)

        self.__incendio = Sensor("normal",incendio)

        self.__aspersores = Aspersores("normal",aspersores)



    def getIncendio(self):

        return self.__incendio



    def setAspersores(self,a):

        self.__aspersores = a

    def getLuces(self):

        return self.__luces

    

    def setLuces(self,lu):

        self.__luces = lu

        self.__calefaccion = lu #calefaccion prende y apaga dependiendo de las luces





    def __str__(self):

        return "Luces: {0} Calefaccion: {1} Incendio: {2} Aspersores: {3}".format(self.__luces.getEstado(),self.__calefaccion.getEstado(),self.__incendio.getEstado(),self.__aspersores.getEstado())

    

class Luces:



    def __init__(self,intensidad,estado=1):

        self.__intensidad = intensidad

        self.__estado = estado

    def setEstado(self,e):

        self.__estado = e

    def getEstado(self):

        return self.__estado





    def __str__(self):

        return "La intensidad es de {0} watts".format(self.__intensidad)



class Calefaccion:



    def __init__(self,temperatura,estado=1):

        self.__temperatura = temperatura

        self.__estado = estado

    def setEstado(self,e):

        self.__estado = e

    def getEstado(self):

        return self.__estado



    def __str__(self):

        return "La temperatura es de {0} ".format(self.__temperatura)



class Sensor:



    def __init__(self,umbral="normal",estado=0):

        self.__umbral = umbral

        self.__estado = estado                                     

    def setEstado(self,e):

        self.__estado = e

    def getEstado(self):

        return self.__estado

    def __str__(self):

        return "El umbral de humo alcanzado fue de: {0} ".format(self.__umbral)



class Aspersores:

    def __init__(self,presion,estado=0):

        self.__presion = presion

        self.__estado = estado

    def setEstado(self,e):

        self.__estado = e

    def getEstado(self):

        return self.__estado



def main():

    #locales,elevadores,pisos:

    l=9

    e=3

    p=2

    e=Edificio(l,e,p)



    #Si hay incendio en el piso uno local uno

    if(e.getPisos()[1].getLocales()[1].getIncendio()) == 1:

        e.getPisos()[1].getLocales()[1].setAspersores(1)

        e.getPisos()[1].getLocales()[1].setLuces(0)

        e.getElevadores()[1].setEstado(0)

        



    #Cuando se apaga el control de incendio

    if(e.getPisos()[1].getLocales()[1].getIncendio()) == 0:

        e.getPisos()[1].getLocales()[1].setAspersores(0)

        e.getPisos()[1].getLocales()[1].setLuces(1)

        e.getElevadores()[1].setEstado(1) 

    

    



main()

