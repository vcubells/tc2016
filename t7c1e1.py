#!/usr/bin/env python
def leer(nombres, archivo):
    try:
        f = open(archivo, 'r')        
        nombres = f.readlines()
        imprime_lista(nombres)
    except IOError:
        print ("Error al leer el archivo")
    finally:
        f.close()
        
def crear(nombres, archivo, modo):
    opc = 's'
    while (opc == 's'):
        nombres.append(raw_input("Entra un nombre: "))
        opc = raw_input("Quieres entrar otro nombre (s/n)?: ")
    
    #Almacenar lista en archivo
    try:
        f = open(archivo, modo)
    
        #f.writelines(nombres)
        for n in nombres:
            f.write("{0}\n".format(n))
    except IOError:
        print("Error I/O con el archivo")
    finally:
        f.close()
        
def imprime_lista(lista):
    for i in lista:
        print(i)
        
def main():
    
    nombres = []
    
    archivo = raw_input("Dame el nombre del archivo: ")
    operacion = raw_input("""Que quieres hacer:?
                          \n l -leer archivo existente
                          \n c -crear un nuevo archivo
                          \n a - adicionar nuevos nombres : """)
    if (operacion == 'l'):
        leer(nombres, archivo)
    elif (operacion == 'c'):
        crear(nombres, archivo, 'w')
    elif (operacion == 'a'):
        crear(nombres, archivo, 'a')
    else:
        print("Opcion no valida")
        
    
        
    
    
main()

