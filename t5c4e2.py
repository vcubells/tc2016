#!/usr/bin/env python

# example-start buttons buttons.py

import pygtk
pygtk.require('2.0')
import gtk
        
class Colores:
    def __init__(self):
        
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("Seleccion de colores")
        
        caja = gtk.HBox(gtk.FALSE, 0)

        self.label = gtk.Label('')

        bSeleccionar = gtk.Button('Selecciona color...')
        
        bSeleccionar.connect("clicked", self.seleccionarColor)
        
        caja.pack_start(self.label, gtk.FALSE, gtk.FALSE, 3)
        caja.pack_start(bSeleccionar, gtk.FALSE, gtk.FALSE, 3)
        
        self.window.add(caja)
        
        self.window.set_border_width(10)
        self.window.connect("destroy", lambda wid: gtk.main_quit())

        self.label.show()      
        bSeleccionar.show()
        caja.show()
        
        self.window.show()
        
    def seleccionarColor(self, widget, data=None):
        select = gtk.ColorSelectionDialog('Seleccionar color')
        resp = select.run()
        if resp:
            color = select.colorsel.get_current_color()
            self.label.set_text(color.to_string())
            data = self.label.get_style().copy()
            data.fg[gtk.STATE_NORMAL] = color
            self.label.set_style(data)
        select.hide()

def main():
    
    Colores()
    gtk.main()


main()







