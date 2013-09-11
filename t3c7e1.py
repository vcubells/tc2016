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
    # Crear inventario de componentes
    
    #Lista de Chasis
    
    chasis = []
    
    ch1 = Chasis()
    ch2 = Chasis(250, 'AT')
    ch3 = Chasis(700)
    
    chasis.append(ch1)
    chasis.append(ch2)
    chasis.append(ch3)
    
    #Lista de Procesadores
    
    procesadores = []
    
    pr1 = Procesador()
    pr2 = Procesador(32, 1.6)
    pr3 = Procesador(32, 3.0)
    
    procesadores.append(pr1)
    procesadores.append(pr2)
    procesadores.append(pr3)
    
    
    #Lista de Memoria
    
    memorias = []
    
    m1 = Memoria()
    m2 = Memoria(2000, 168)
    m3 = Memoria(512, 72)
    
    memorias.append(m1)
    memorias.append(m2)
    memorias.append(m3)
    
    #Lista de Monitores
    
    monitores = []
    
    mn1 = Monitor()
    mn2 = Monitor('CRT', 17, '800 x 600')
    mn3 = Monitor(tam=27)
    
    monitores.append(mn1)
    monitores.append(mn2)
    monitores.append(mn3)
    
    #Lista de Mouse
    
    ratones = []
    
    mou1 = Mouse()
    mou2 = Mouse('mini DIM', 2)
    mou3 = Mouse(botones = 2)
    
    ratones.append(mou1)
    ratones.append(mou2)
    ratones.append(mou3)
    
    #Lista de Teclados
    
    teclados = []
    
    t1 = Teclado()
    t2 = Teclado('mini DIM', 114)
    t3 = Teclado(teclas = 86)
    
    teclados.append(t1)
    teclados.append(t2)
    teclados.append(t3)
    
    #Lista de HDD
    
    discos = []
    
    h1 = HDD()
    h2 = HDD('HDD', 500, 7200)
    h3 = HDD('SSD', 250, 0)
    
    discos.append(h1)
    discos.append(h2)
    discos.append(h3)
    
    #Lista de Motherboards
    
    boards = []
    
    mb1 = Motherboard()
    mb2 = Motherboard(1033, 2, 8)
    mb3 = Motherboard(1066, 4, 16)
    
    boards.append(mb1)
    boards.append(mb2)
    boards.append(mb3)
    
    # Lista de ventas
    
    ventas = []
    
    for i in range(0,3):   
        pc = PC(chasis[i],boards[i], procesadores[i], memorias[i], ratones[i], monitores[i], teclados[i], discos[i])
        ventas.append(pc)
        
    pc = PC(Chasis(), Motherboard(), Procesador(), Memoria(), Mouse(), Monitor(), Teclado(), HDD())
    ventas.append(pc)
    
    pc = PC(ch1, mb3, p2, m1, mou3, mn2, t1, hd3)
    #Generar reporte de ventas
    for i in ventas:
        i.printf()

main()



