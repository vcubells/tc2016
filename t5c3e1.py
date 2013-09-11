#!/usr/bin/env python

# example-start buttons buttons.py

import pygtk
pygtk.require('2.0')
import gtk

class Auto:
    def __init__(self, placas='', modelo=0, marca='Indefinida'):
        self.__placas = placas
        self.__modelo = modelo
        self.__marca = marca
        
    def getPlacas(self):
        return self.__placas
    
    def getModelo(self):
        return self.__modelo
    
    def getMarca(self):
        return self.__marca
    
    def setPlacas(self, placa):
        self.__placas = placa
        
    def setModelo(self, m):
        self.__modelo = m
        
    def setMarca(self, mar):
        self.__marca = mar
        
class EntraAuto:
    def __init__(self, autos):
        self.__autos = autos
        
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("Entrar un auto")
        
        table = gtk.Table(4, 2, gtk.TRUE)
        
        label1 = gtk.Label('Placa:')
        label2 = gtk.Label('Modelo:')
        label3 = gtk.Label('Marca:')
        
        table.attach(label1, 0,1,0,1 )
        table.attach(label2, 0,1,1,2 )
        table.attach(label3, 0,1,2,3)
        
        self.placa = gtk.Entry()
        self.modelo = gtk.Entry()
        self.marca = gtk.Entry()
        
        table.attach(self.placa, 1,2,0,1 )
        table.attach(self.modelo, 1,2,1,2 )
        table.attach(self.marca, 1,2,2,3 )

        bAdicionar = gtk.Button('Adicionar')
        table.attach(bAdicionar, 1,2,3,4)
        
        bAdicionar.connect("clicked", self.adicionarAuto)
        
        caja = gtk.HBox(gtk.FALSE, 0)
        
        label4 = gtk.Label("Autos:")
        caja.pack_start(label4, gtk.FALSE, gtk.FALSE, 3)
        
        self.contador = gtk.Label("0")
        caja.pack_start(self.contador, gtk.FALSE, gtk.FALSE, 3)
        
        table.attach(caja, 0,1,3,4)
        
        self.window.add(table)
        
        self.window.set_border_width(10)
        self.window.connect("destroy", lambda wid: gtk.main_quit())

        label1.show()
        label2.show()
        label3.show()
        
        self.placa.show()
        self.modelo.show()
        self.marca.show()
        
        bAdicionar.show()
        
        label4.show()
        self.contador.show()
        caja.show()
        
        table.show()
        
        self.window.show()
        
    def adicionarAuto(self, widget, data=None):
        auto = Auto(self.placa.get_text(), self.modelo.get_text(), self.marca.get_text())
        self.__autos.append(auto)
        
        #Limpiar los textbox
        #self.placa.set_text('')
        #self.modelo.set_text('')
        #self.marca.set_text('')
        
        #self.contador.set_text(str(len(self.__autos)))
        gtk.main_quit()

def main():
    autos = []
    
    EntraAuto(autos)

    gtk.main()
    
    print(len(autos))

main()





