#!/usr/bin/env python

class NumeroError(Exception):
    pass
    
class NegativoError (NumeroError):
    def __init__(self, valor):
        self.valor = valor
        
    def __str__(self):
        return "El numero {0} no puede ser negativo".format(self.valor)
        
class Numero:
    def __init__(self, num):
        self.setNumero(num)
        
    def setNumero(self, num):
        if num < 0:
            raise NegativoError(num)
        elif num > 100 and num < 200:
            raise NumeroError()
        elif num > 200:
            raise ArithmeticError()
        else:
            self.__num = num
        
    def __str__(self):
        return "{0}".format(self.__num)
        
def main():
    positivo = Numero(25)
    print(positivo)
    
    try:
        negativo = Numero(201)
    except NegativoError as e:
        print(e)
    except NumeroError:
        print "Ocurrio un error general"
    except Exception:
        print("No se de que tipo es el error")
    else:
        print(negativo)
    finally:
        print("Si se pudo")
        
    n1 = int(input("Entra un numero:"))
    n2 = int(input("Entra otro numero:"))
    
    try:
        print("n1 / n2 = ", n1/n2)
    except ZeroDivisionError:
        print("El segundo numero no puede ser 0")
    
    
main()
