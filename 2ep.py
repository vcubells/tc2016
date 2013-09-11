#!/usr/bin/env python

class Controlador:
    def __init__(self, estado = 0, local = None, tipo = 0):
        self.__estado = estado
        self.__local = local
        self.__tipo = tipo
        
    def getTipo(self):
        return self.__tipo
    
    def setEstado(self, estado):
        self.__estado = estado
        
    def getLocal(self):
        return self.__local
    
    def setLocal(self, local):
        self.__local = local
        
    def getEstado(self):
        return self.__estado
    
    def Encender(self):
        self.__estado = 1
    
    def Apagar(self):
        self.__estado = 0
    
    def __str__(self):
        return "Estado = {0}".format(self.__estado)
        
        
class Luces (Controlador):
    def __init__(self, estado, intensidad = 450):
        Controlador.__init__(self, estado, tipo = 2)
        self.__intensidad = intensidad
            
    def setIntensidad(self, intensidad):
        self.__intensidad = intensidad
            
    def getIntensidad(self):
        return self.__intensidad
    
    def Apagar(self):
        Controlador.Apagar(self)
        self.getLocal().ApagarCalefaccion()
        
    def Encender(self):
        Controlador.Encender(self)
        self.getLocal().EncenderCalefaccion()
        
    def __str__(self):
        n = Controlador.__str__(self)
        return "{0}, Intensidad = {1} Watts".format(n, self.__intensidad)
            
class Calefaccion (Controlador):
    def __init__(self, estado, temperatura = 450):
        Controlador.__init__(self, estado, tipo = 3)
        self.__temperatura = temperatura
            
    def setTemperatura(self, temperatura):
        self.__temperatura = temperatura
            
    def getTemperatura(self):
        return self.__temperatura
        
    def __str__(self):
        n = Controlador.__str__(self)
        return "{0}, Temperatura = {1} oC".format(n, self.__temperatura)          
            
class Incendio (Controlador):
    def __init__(self, estado, umbral = 0):
        Controlador.__init__(self, estado, tipo = 0)
        self.__umbral = umbral
        self.__maximo = 10
            
    def setUmbral(self, umbral):
        self.__umbral = umbral
        if self.__umbral > self.__maximo:
            self.Encender()
            
    def getUmbral(self):
        return self.__umbral
    
    def Apagar(self):
        Controlador.Apagar(self)
        self.getLocal().NoHayIncendio()
        
    def Encender(self):
        Controlador.Encender(self)
        self.getLocal().HayIncendio()
        
    def __str__(self):
        n = Controlador.__str__(self)
        return "{0}, Umbral = {1} ".format(n, self.__umbral)
            
class Aspersor (Controlador):
    def __init__(self, estado, presion = 20):
        Controlador.__init__(self, estado, tipo = 1)
        self.__presion = presion
            
    def setPresion(self, presion):
        self.__presion = presion
            
    def getPresion(self):
        return self.__presion
        
    def __str__(self):
        n = Controlador.__str__(self)
        return "{0}, Presion de agua = {1} ".format(n, self.__presion)
            
class Elevador (Controlador):
    def __init__(self, numero = 1):
        Controlador.__init__(self, 1, tipo = 4)
        self.__numero = numero
        
    def getNumero(self):
        return self.__numero
    
    def setNumero(self, numero):
        self.__numero = numero
        
    def __str__(self):
        n = Controlador.__str__(self)
        return "{0}, Elevador {1} ".format(n, self.__numero)

class Local:
    def __init__(self, numero = 0, edificio = None):
        self.__numero = numero
        self.__controladores = []
        self.__edificio = edificio
        
    def setNumero(self, numero):
        self.__numero = numero
        
    def getNumero(self):
        return self.__numero
    
    def addControlador(self, controlador):
        controlador.setLocal(self)
        self.__controladores.append(controlador)
    
    def NoHayIncendio(self):
        for c in self.__controladores:
            if c.getTipo() == 1:
                c.Apagar()
        
    def HayIncendio(self):
        for c in self.__controladores:
            if c.getTipo() == 2:
                c.Apagar()
            elif c.getTipo() == 1:
                c.Encender()
                
        self.__edificio.HayIncendio()
    
    def ApagarCalefaccion(self):
        for c in self.__controladores:
            if c.getTipo() == 3:
                c.Apagar()    
    
    def EncenderCalefaccion(self):
        for c in self.__controladores:
            if c.getTipo() == 3:
                c.Encender()
                
    def __str__(self):
        print("Local {0}".format(self.__numero));
        for c in self.__controladores:
            print(c)
            
        return ""
    
class Piso:
    def __init__(self, numero = 0):
        self.__numero = numero
        self.__locales = []
        
    def setNumero(self, numero):
        self.__numero = numero
        
    def getNumero(self):
        return self.__numero
    
    def addLocal(self, local):
        self.__locales.append(local)
    
    def __str__(self):
        print("Piso {0}".format(self.__numero))
        for l in self.__locales:
            print(l)
            
        return ""
    
class Edificio:
    def __init__(self):
        self.__pisos = []
        self.__elevadores = []
        
    def addPiso(self, piso):
        self.__pisos.append(piso)
    
    def addElevador(self, elevador):
        self.__elevadores.append(elevador)
    
    def HayIncendio(self):
        for e in self.__elevadores:
            e.Apagar()
                
    def __str__(self):

        for e in self.__elevadores:
            print(e)
        
        for p in self.__pisos:
            print(p)
            
        return ""
    
def main():
    #Crear controladores
    i1 = Incendio(0, 20)
    i2 = Incendio(0, 15)
    i3 = Incendio(0, 10)
    i4 = Incendio(0, 25)
    i5 = Incendio(0, 28)
    
    a1 = Aspersor(0, 18)
    a2 = Aspersor(0, 90)
    a3 = Aspersor(0, 30)
    a4 = Aspersor(0, 100)
    a5 = Aspersor(0, 55)
    
    l1 = Luces(0, 60)
    l2 = Luces(0, 80)
    l3 = Luces(0, 40)
    l4 = Luces(0, 20)
    l5 = Luces(0, 100)
    
    c1 = Calefaccion(0, 18)
    c2 = Calefaccion(0, 22)
    c3 = Calefaccion(0, 35)
    c4 = Calefaccion(0, 2)
    
    #Crear Edificio
    e = Edificio()
    
    #Crear Locales
    l11 = Local(11, e)
    l11.addControlador(i1)
    l11.addControlador(a1)
    l11.addControlador(l1)
    l11.addControlador(c1)
    l11.addControlador(i5)
    
    l12 = Local(12, e)
    l12.addControlador(i2)
    l12.addControlador(a2)
    l12.addControlador(l2)
    l12.addControlador(c2)

    l21 = Local(21, e)
    l21.addControlador(i3)
    l21.addControlador(a3)
    l21.addControlador(l3)
    l21.addControlador(c3)

    l31 = Local(31, e)
    l31.addControlador(i4)
    l31.addControlador(a4)
    l31.addControlador(l4)
    l31.addControlador(c4)
    
    #Crear Pisos
    p1 = Piso(1)
    p1.addLocal(l11)
    p1.addLocal(l12)
    
    p2 = Piso(2)
    p2.addLocal(l21)
    
    p3 = Piso(3)
    p3.addLocal(l31)
    
    e.addPiso(p1)
    e.addPiso(p2)
    e.addPiso(p3)
    
    #Crear elevadores
    el1 = Elevador(1)
    el2 = Elevador(2)
    
    e.addElevador(el1)
    e.addElevador(el2)
    
    #Imprimir el reporte
    print(e)
    
    l1.Encender()
    print("Se encendieron las luces de Local 11")
    print(e)
    
    i1.setUmbral(50)
    
    print("Se activo la alarma incendio en Local 11")
    print(e)
    
main()