#!/usr/bin/env python

class Actividad:
    
    def __init__(self, nombre = '', optimista = 0, probable = 0, pesimista = 0, sucesoOrigen = None, sucesoDestino = None):
        self.__nombre = nombre
        self.__optimista = optimista
        self.__pesimista = pesimista
        self.__probable = probable
        self.__tiempoPERT = 0
        self.__sucesoOrigen = sucesoOrigen
        self.__sucesoDestino = sucesoDestino
        self.__holguraTotal = 0
        self.__holguraIndependiente = 0
        self.__holguraLibre = 0
        self.__fechaComienzoTemprana = 0
        self.__fechaComienzoTardia = 0
        self.__fechaFinTemprana = 0
        self.__fechaFinTardia = 0
        
        self.calculaTiempoPert()
    
    def getNombre(self):
        return self.__nombre
    
    def getTiempoPERT(self):
        return self.__tiempoPERT
    
    def getSucesoOrigen(self):
        return self.__sucesoOrigen
    
    def getSucesoDestino(self):
        return self.__sucesoDestino
    
    def getHolguraTotal(self):
        return self.__holguraTotal
    
    def getHolguraLibre(self):
        return self.__holguraLibre
    
    def getHolguraIndependiente(self):
        return self.__holguraIndependiente
    
    def getFechaComienzoTemprana(self):
        return self.__fechaComienzoTemprana
    
    def getFechaComienzoTardia(self):
        return self.__fechaComienzoTardia
    
    def getFechaFinTemprana(self):
        return self.__fechaFinTemprana
    
    def getFechaFinTardia(self):
        return self.__fechaFinTardia
    
    def setSucesoOrigen(self, suceso):
        self.__sucesoOrigen = suceso
        
    def setSucesoDestino(self, suceso):
        self.__sucesoDestino = suceso
        
    def calculaTiempoPert(self):
        self.__tiempoPERT = (self.__pesimista + 4 * self.__probable + self.__optimista) / 6
    
    def calculaHolguraTotal(self):
        self.__holguraTotal = self.__sucesoDestino.getTiempoLate() - self.__sucesoOrigen.getTiempoEarly() - self.__tiempoPERT

    def calculaHolguraLibre(self):
        self.__holguraLibre = self.__sucesoDestino.getTiempoEarly() - self.__sucesoOrigen.getTiempoEarly() - self.__tiempoPERT
        
    def calculaHolguraIndependiente(self):
        self.__holguraIndependiente = self.__sucesoDestino.getTiempoEarly() - self.__sucesoOrigen.getTiempoLate() - self.__tiempoPERT      
    
    def esCritica(self):
        return (self.__holguraTotal == 0)
    
    def calculaFechaComienzoTemprana(self):
        self.__fechaComienzoTemprana = self.__sucesoOrigen.getTiempoEarly()
    
    def calculaFechaComienzoTardia(self):
        self.__fechaComienzoTardia = self.__sucesoDestino.getTiempoLate() - self.__tiempoPERT
    
    def calculaFechaFinTemprana(self):
        self.__fechaFinTemprana = self.__sucesoOrigen.getTiempoEarly() + self.__tiempoPERT
    
    def calculaFechaFinTardia(self):
        self.__fechaFinTardia = self.__sucesoDestino.getTiempoLate()
    
    def calcular(self):
        self.calculaHolguraTotal()
        self.calculaHolguraLibre()
        self.calculaHolguraIndependiente()
        self.calculaFechaComienzoTemprana()
        self.calculaFechaComienzoTardia()
        self.calculaFechaFinTemprana()
        self.calculaFechaFinTardia()
        
        
class Suceso:
    
    def __init__(self, nombre = 1, tiempoEarly = 0, tiempoLate = 0 ):
        self.__nombre = nombre
        self.__actividadesLlegan = []
        self.__actividadesSalen = []
        self.__tiempoEarly = tiempoEarly
        self.__tiempoLate = tiempoLate
        self.__holgura = 0
        
    def getNombre(self):
        return self.__nombre
    
    def getTiempoEarly(self):
        return self.__tiempoEarly
    
    def getTiempoLate(self):
        return self.__tiempoLate
    
    def getHolgura(self):
        return self.__holgura
    
    def adicionaActividadLlega(self, actividad):
        self.__actividadesLlegan.append(actividad)
    
    def adicionaActividadSale(self, actividad):
        self.__actividadesSalen.append(actividad)
        
    def calculaTiempoEarly(self):
        if len(self.__actividadesLlegan) > 0:
            maximo = 0
            for actividad in self.__actividadesLlegan:
                suma = 0
                suma = actividad.getTiempoPERT() + actividad.getSucesoOrigen().getTiempoEarly()
                if suma > maximo:
                    maximo = suma
            self.__tiempoEarly = maximo
         
    def calculaTiempoLate(self):
        if len(self.__actividadesSalen) > 0:        
            minimo = 1000000
            resta = 0
            for actividad in self.__actividadesSalen:
                resta = actividad.getSucesoDestino().getTiempoLate() - actividad.getTiempoPERT()
                if resta < minimo:
                    minimo = resta
            self.__tiempoLate = minimo
        else:
            self.__tiempoLate = self.__tiempoEarly
        
    def calculaHolgura(self):
        self.__holgura = self.__tiempoLate - self.__tiempoEarly
    
    def esCritico(self):
        return (self.__holgura == 0)
        
class Proyecto:
    
    def __init__(self, nombre = 'Indefinido'):
        self.__nombre = nombre
        self.__actividades = []
        self.__sucesos = []
    
    def getNombre(self):
        return self.__nombre
    
    def adicionaActividad(self, actividad):
        self.__actividades.append(actividad)
        
    def adicionaSuceso(self, suceso):
        self.__sucesos.append(suceso)
        
    def obtieneSucesosCriticos(self):
        for suceso in self.__sucesos:
            if suceso.esCritico():
                print(" {0} ".format(suceso.getNombre()))

    def obtieneActividadesCriticas(self):
        for actividad in self.__actividades:
            if actividad.esCritica():
                print(" {0} ".format(actividad.getNombre()))
                
    def calculaDuracionTotal(self):
        no_sucesos = len(self.__sucesos)
        duracionTotal = self.__sucesos[no_sucesos - 1].getTiempoLate()
        return duracionTotal
    
    def __calculaTiemposEarlySucesos(self):
        for suceso in self.__sucesos:
            suceso.calculaTiempoEarly()
            
    def __calculaTiemposLateSucesos(self):
        self.__sucesos.reverse()
        for suceso in self.__sucesos:
            suceso.calculaTiempoLate()
            
        self.__sucesos.reverse()
    
    def __calculaHolgurasSucesos(self):
        for suceso in self.__sucesos:
            suceso.calculaHolgura()
            
    def __calculaHolgurasFechasActividades(self):
        for actividad in self.__actividades:
            actividad.calcular()
            
    def calcular(self):
        self.__calculaTiemposEarlySucesos()
        self.__calculaTiemposLateSucesos()
        self.__calculaHolgurasSucesos()
        self.__calculaHolgurasFechasActividades()
        
    def __str__(self):
        cadena = "Actividad,TP,HT,HL,HI,FCE,FCL,FFE,FFL,Critica"
        print(cadena)
        for actividad in self.__actividades:
            cadena = "{0},{1},{2},{3},{4},{5},{6},{6},{8},{9}".format(
                actividad.getNombre(),
                actividad.getTiempoPERT(),
                actividad.getHolguraTotal(),
                actividad.getHolguraLibre(),
                actividad.getHolguraIndependiente(),
                actividad.getFechaComienzoTemprana(),
                actividad.getFechaComienzoTardia(),
                actividad.getFechaFinTemprana(),
                actividad.getFechaFinTardia(),
                actividad.esCritica()
            )
            print(cadena)
            
        cadena = "Suceso,TE,TL,H,Critico"
        print(cadena)
        for suceso in self.__sucesos:
            cadena = "{0},{1},{2},{3},{4}".format(
                suceso.getNombre(),
                suceso.getTiempoEarly(),
                suceso.getTiempoLate(),
                suceso.getHolgura(),
                suceso.esCritico()
            )
            print(cadena)
            
        return "Duracion Total = {0}".format(self.calculaDuracionTotal())
    
def examen2P():
    
    proyecto = Proyecto()
    
    S1 = Suceso(1)
    S2 = Suceso(2)
    S3 = Suceso(3)
    S4 = Suceso(4)
    S5 = Suceso(5)
    S6 = Suceso(6)
    S7 = Suceso(7)
    S8 = Suceso(8)
    S9 = Suceso(9)
    S10 = Suceso(10)
    S11 = Suceso(11)
    S12 = Suceso(12)
    
    A = Actividad('A', 1, 1, 1, S1, S2)
    B = Actividad('B', 1, 2, 3, S1, S6)
    C = Actividad('C', 2, 3, 4, S1, S5)
    D = Actividad('D', 2, 4, 6, S2, S3)
    E = Actividad('E', 1, 3, 5, S2, S6)
    F = Actividad('F', 1, 2, 3, S5, S6)
    G = Actividad('G', 0, 1, 2, S5, S8)
    H = Actividad('H', 5, 7, 9, S3, S4)
    I = Actividad('I', 6, 8, 10, S3, S7)
    J = Actividad('J', 5, 7, 15, S6, S7)
    K = Actividad('K', 6, 7, 8, S6, S9)
    L = Actividad('L', 3, 5, 7, S8, S9)
    M = Actividad('M', 1, 1, 1, S4, S10)
    N = Actividad('N', 1, 2, 3, S7, S10)
    O = Actividad('O', 2, 3, 4, S9, S11)
    P = Actividad('P', 3, 4, 5, S10, S11)
    Q = Actividad('Q', 1, 2, 3, S11, S12)
    
    S1.adicionaActividadSale(A)
    S1.adicionaActividadSale(B)
    S1.adicionaActividadSale(C)
    
    S2.adicionaActividadSale(D)
    S2.adicionaActividadSale(E)
    S2.adicionaActividadLlega(A)
    
    S3.adicionaActividadSale(H)
    S3.adicionaActividadSale(I)
    S3.adicionaActividadLlega(D)
    
    S4.adicionaActividadSale(M)
    S4.adicionaActividadLlega(H)
    
    S5.adicionaActividadSale(F)
    S5.adicionaActividadSale(G)
    S5.adicionaActividadLlega(C)
    
    S6.adicionaActividadSale(J)
    S6.adicionaActividadSale(K)
    S6.adicionaActividadLlega(B)
    S6.adicionaActividadLlega(E)
    S6.adicionaActividadLlega(F)
    
    S7.adicionaActividadSale(N)
    S7.adicionaActividadLlega(I)
    S7.adicionaActividadLlega(J)
    
    S8.adicionaActividadSale(L)
    S8.adicionaActividadLlega(G)
    
    S9.adicionaActividadSale(O)
    S9.adicionaActividadLlega(L)
    S9.adicionaActividadLlega(K)
    
    S10.adicionaActividadSale(P)
    S10.adicionaActividadLlega(M)
    S10.adicionaActividadLlega(N)
    
    S11.adicionaActividadSale(Q)
    S11.adicionaActividadLlega(P)
    S11.adicionaActividadLlega(O)
    
    S12.adicionaActividadLlega(Q)
    
    proyecto.adicionaActividad(A)
    proyecto.adicionaActividad(B)
    proyecto.adicionaActividad(C)
    proyecto.adicionaActividad(D)
    proyecto.adicionaActividad(E)
    proyecto.adicionaActividad(F)
    proyecto.adicionaActividad(G)
    proyecto.adicionaActividad(H)
    proyecto.adicionaActividad(I)
    proyecto.adicionaActividad(J)
    proyecto.adicionaActividad(K)
    proyecto.adicionaActividad(L)
    proyecto.adicionaActividad(M)
    proyecto.adicionaActividad(N)
    proyecto.adicionaActividad(O)
    proyecto.adicionaActividad(P)
    proyecto.adicionaActividad(Q)
    
    proyecto.adicionaSuceso(S1)
    proyecto.adicionaSuceso(S2)
    proyecto.adicionaSuceso(S5)
    proyecto.adicionaSuceso(S6)
    proyecto.adicionaSuceso(S3)
    proyecto.adicionaSuceso(S8)
    proyecto.adicionaSuceso(S4)
    proyecto.adicionaSuceso(S7)
    proyecto.adicionaSuceso(S9)
    proyecto.adicionaSuceso(S10)
    proyecto.adicionaSuceso(S11)
    proyecto.adicionaSuceso(S12)
    
    proyecto.calcular()
    
    print(proyecto)
    
    proyecto.obtieneActividadesCriticas()
    
def examenFinal():
    
    proyecto = Proyecto()
    
    S1 = Suceso(1)
    S2 = Suceso(2)
    S3 = Suceso(3)
    S4 = Suceso(4)
    S5 = Suceso(5)
    S6 = Suceso(6)
    S7 = Suceso(7)
    S8 = Suceso(8)
    
    A = Actividad('A', 1, 1, 2, S1, S2)
    B = Actividad('B', 2, 4, 6, S2, S3)
    C = Actividad('C', 3, 5, 7, S2, S4)
    D = Actividad('D', 2, 3, 4, S3, S5)
    E = Actividad('E', 1, 2, 3, S3, S6)
    F = Actividad('F', 1, 2, 3, S4, S5)
    G = Actividad('G', 2, 4, 5, S4, S7)
    H = Actividad('H', 2, 3, 3, S5, S8)
    I = Actividad('I', 1, 1, 2, S6, S7)
    J = Actividad('J', 2, 4, 6, S7, S8)
    
    S1.adicionaActividadSale(A)
    
    S2.adicionaActividadSale(B)
    S2.adicionaActividadSale(C)
    S2.adicionaActividadLlega(A)
    
    S3.adicionaActividadSale(D)
    S3.adicionaActividadSale(E)
    S3.adicionaActividadLlega(B)
    
    S4.adicionaActividadSale(F)
    S4.adicionaActividadLlega(G)
    S4.adicionaActividadLlega(C)
    
    S5.adicionaActividadSale(H)
    S5.adicionaActividadLlega(D)
    S5.adicionaActividadLlega(F)
    
    S6.adicionaActividadSale(I)
    S6.adicionaActividadLlega(E)
    
    S7.adicionaActividadSale(J)
    S7.adicionaActividadLlega(I)
    S7.adicionaActividadLlega(G)
    
    S8.adicionaActividadLlega(H)
    S8.adicionaActividadLlega(J)
    
    proyecto.adicionaActividad(A)
    proyecto.adicionaActividad(B)
    proyecto.adicionaActividad(C)
    proyecto.adicionaActividad(D)
    proyecto.adicionaActividad(E)
    proyecto.adicionaActividad(F)
    proyecto.adicionaActividad(G)
    proyecto.adicionaActividad(H)
    proyecto.adicionaActividad(I)
    proyecto.adicionaActividad(J)
    
    proyecto.adicionaSuceso(S1)
    proyecto.adicionaSuceso(S2)
    proyecto.adicionaSuceso(S3)
    proyecto.adicionaSuceso(S4)
    proyecto.adicionaSuceso(S5)
    proyecto.adicionaSuceso(S6)
    proyecto.adicionaSuceso(S7)
    proyecto.adicionaSuceso(S8)

    
    proyecto.calcular()
    
    print(proyecto)
    
    proyecto.obtieneActividadesCriticas()  

def examenFinal2():
    
    proyecto = Proyecto()
    
    S1 = Suceso(1)
    S2 = Suceso(2)
    S3 = Suceso(3)
    S4 = Suceso(4)
    S5 = Suceso(5)
    S6 = Suceso(6)
    S7 = Suceso(7)
    S8 = Suceso(8)
    S9 = Suceso(9)
    
    A = Actividad('A', 3, 5, 8, S1, S3)
    B = Actividad('B', 2, 3, 5, S1, S2)
    C = Actividad('C', 2, 4, 5, S1, S5)
    D = Actividad('D', 2, 3, 6, S2, S3)
    E = Actividad('E', 2, 4, 8, S3, S4)
    F = Actividad('F', 3, 6, 9, S4, S7)
    G = Actividad('G', 2, 5, 8, S5, S6)
    H = Actividad('H', 4, 6, 9, S6, S7)
    I = Actividad('I', 3, 4, 8, S7, S8)
    J = Actividad('J', 1, 2, 6, S8, S9)
    Fict1 = Actividad('Fict1', 0, 0, 0, S5, S3)
    Fict2 = Actividad('Fict2', 0, 0, 0, S4, S6)
    
    S1.adicionaActividadSale(A)
    S1.adicionaActividadSale(B)
    S1.adicionaActividadSale(C)
    
    S2.adicionaActividadSale(D)
    S2.adicionaActividadLlega(B)
    
    S5.adicionaActividadSale(G)
    S5.adicionaActividadSale(Fict1)
    S5.adicionaActividadLlega(C)

    S3.adicionaActividadSale(E)
    S3.adicionaActividadLlega(A)
    S3.adicionaActividadLlega(D)
    S3.adicionaActividadLlega(Fict1)
    
    S4.adicionaActividadSale(F)
    S4.adicionaActividadSale(Fict2)
    S4.adicionaActividadLlega(E)
    
    S6.adicionaActividadSale(H)
    S6.adicionaActividadLlega(Fict2)
    S6.adicionaActividadLlega(G)
    
    S7.adicionaActividadSale(I)
    S7.adicionaActividadLlega(H)
    S7.adicionaActividadLlega(F)
    
    S8.adicionaActividadSale(J)
    S8.adicionaActividadLlega(I)
    
    S9.adicionaActividadLlega(J)
     
    proyecto.adicionaActividad(A)
    proyecto.adicionaActividad(B)
    proyecto.adicionaActividad(C)
    proyecto.adicionaActividad(D)
    proyecto.adicionaActividad(Fict1)
    proyecto.adicionaActividad(E)
    proyecto.adicionaActividad(F)
    proyecto.adicionaActividad(G)
    proyecto.adicionaActividad(Fict2)
    proyecto.adicionaActividad(H)
    proyecto.adicionaActividad(I)
    proyecto.adicionaActividad(J)
    
    proyecto.adicionaSuceso(S1)
    proyecto.adicionaSuceso(S2)
    proyecto.adicionaSuceso(S5)
    proyecto.adicionaSuceso(S3)
    proyecto.adicionaSuceso(S4)
    proyecto.adicionaSuceso(S6)
    proyecto.adicionaSuceso(S7)
    proyecto.adicionaSuceso(S8)
    proyecto.adicionaSuceso(S9)

    
    proyecto.calcular()
    
    print(proyecto)
    
    proyecto.obtieneActividadesCriticas()  


def main():
    #examen2P()
    #examenFinal()
    examenFinal2()
    
main()
    
    
    