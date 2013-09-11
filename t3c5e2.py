#!/usr/bin/env python

class Procesador:
    """Procesador"""
    
    def __init__(self, socket = 45, vel = 2.4):
        self.__socket = socket
        self.__velocidad = vel
        
    def __str__(self):
        return "{0} : de {1} nm a {2} GHz".format(self.__doc__, self.__socket, self.__velocidad)

        

class Motherboard:
    """Motherboard"""
   
    def __init__(self, frec = 133, proc = 1, slots = 4):
        self.__frecuencia = frec
        self.__micros = proc
        self.__slots = slots
        
    def __str__(self):
        return "{0} : bus de {1} MHz, {2} procesadores, {3} slots".format(self.__doc__, self.__frecuencia, self.__micros, self.__slots)
 
    

class Memoria:
    """Memoria"""
    
    def __init__(self, cap = 1000, pines = 172):
        self.__capacidad = cap
        self.__pines = pines
        
    def __str__(self):
        return "{0} : RAM de {1} MB y {2} pines".format(self.__doc__, self.__capacidad, self.__pines)
 

class Mouse:
    """Mouse"""
    
    def __init__(self, conector = 'USB', botones = 3):
        self.__conector = conector
        self.__botones = botones
        
    def __str__(self):
        return "{0} : {1} de {2} botones".format(self.__doc__, self.__conector, self.__botones)
 

class Monitor:
    """Monitor"""
    
    def __init__(self, tipo = 'LCD', tam = 21, res = '1024 x 768'):
        self.__tipo = tipo
        self.__tam = tam
        self.__resolucion = res
        
    def __str__(self):
        return "{0} : {1} de {2}', {3} ".format(self.__doc__, self.__tipo, self.__tam, self.__resolucion)
 

class Teclado:
    """Teclado"""
    
    def __init__(self, conector = 'USB', teclas = 96):
        self.__conector = conector
        self.__teclas = teclas
        
    def __str__(self):
        return "{0} : {1} de {2} teclas".format(self.__doc__, self.__conector, self.__teclas)
 

class HDD:
    """HDD"""
    
    def __init__(self, tipo = 'HDD', cap = 500, rpm = 5400):
        self.__tipo = tipo
        self.__capacidad = cap
        self.__rpm = rpm
        
    def __str__(self):
        return "{0} : {1} de {2}, {3} GB".format(self.__doc__, self.__tipo, self.__rpm, self.__capacidad)

class Chasis:
    """Chasis"""
    
    def __init__(self, potencia = 450, ff = 'ATX'):
        self.__potencia = potencia
        self.__factor = ff
        
    def __str__(self):
        return "{0} : {2} de {1} Watts".format(self.__doc__, self.__potencia, self.__factor)

class PC:
    """PC"""
    
    def __init__(self, ch, mb, pr, mem, mou, mon, tec, hd):
        self.__chasis = ch
        self.__motherboard = mb
        self.__procesador = pr
        self.__memoria = mem
        self.__monitor = mon
        self.__mouse = mou
        self.__teclado = tec
        self.__hdd = hd
    
    
    def printf(self):
        print("---------------------")
        print("Composicion de la PC:")
        print("---------------------")
        print(self.__chasis)
        print(self.__motherboard)
        print(self.__procesador)
        print(self.__memoria)
        print(self.__hdd)
        print(self.__monitor)
        print(self.__teclado)
        print(self.__mouse)
    
def main():
    ch = Chasis()
    pr = Procesador()
    mem = Memoria()
    mon = Monitor()
    mou = Mouse()
    tec = Teclado()
    hdd = HDD()
    mb = Motherboard()
    
    pc = PC(ch, mb, pr, mem, mou, mon, tec, hdd)
    pc.printf()

main()

