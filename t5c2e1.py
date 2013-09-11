#!/usr/bin/env python

# example-start buttons buttons.py

import pygtk
pygtk.require('2.0')
import gtk


class GUI:
    
    def callback(self, widget, data=None):
        self.text.set_editable(widget.get_active())
            

    def callback_left(self, widget, data=None):
        
        self.__lista[self.__pos] = self.text.get_text()
        
        if self.__pos == 0:
            self.__pos = len(self.__lista) - 1
        else:
            self.__pos -= 1
            
        self.label.set_text(self.__lista[self.__pos])
        self.text.set_text(self.__lista[self.__pos])
    
    def callback_right(self, widget, data=None):
        self.__lista[self.__pos] = self.text.get_text()
        
        if self.__pos == len(self.__lista) - 1:
            self.__pos = 0
        else:
            self.__pos += 1
            
        self.label.set_text(self.__lista[self.__pos])
        self.text.set_text(self.__lista[self.__pos])

    def __init__(self):
        
        self.__lista = ["Juana", "Josefa", "Maria", "Juan", "Jose"]
        self.__pos = 0
        
        # Create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

        self.window.set_title("Visualizar elementos de la lista")

        # It's a good idea to do this for all windows.
        self.window.connect("destroy", lambda wid: gtk.main_quit())
        self.window.connect("delete_event", lambda a1,a2:gtk.main_quit())

        # Sets the border width of the window.
        self.window.set_border_width(10)
        
        
        # Create box for xpm and label
        box = gtk.VBox(gtk.FALSE, 0)
        box.set_border_width(2)

        # Create a label for the button
        self.label = gtk.Label(self.__lista[self.__pos])
        
        self.text = gtk.Entry()
        self.text.set_text(self.__lista[self.__pos]) 

        # Crear un boton con flecha a la izquierda
        bleft = gtk.Button()
        left = gtk.Arrow(gtk.ARROW_LEFT, gtk.SHADOW_OUT)
        bleft.add(left)

        # Connect the "clicked" signal of the button to our callback
        bleft.connect("clicked", self.callback_left)

        # Crear un boton con flecha a la derecha
        bright = gtk.Button()
        right = gtk.Arrow(gtk.ARROW_RIGHT, gtk.SHADOW_IN)
        bright.add(right)

        # Connect the "clicked" signal of the button to our callback
        bright.connect("clicked", self.callback_right)
    
        # Pack into the box
        box.pack_start(self.label, gtk.FALSE, gtk.FALSE, 3)
        box.pack_start(self.text, gtk.FALSE, gtk.FALSE, 3)
        box.pack_start(bleft, gtk.FALSE, gtk.FALSE, 3)
        box.pack_start(bright, gtk.FALSE, gtk.FALSE, 3)
        
        # Create  button
        button = gtk.CheckButton("Editable")

        # When the button is toggled, we call the "callback" method
        # with a pointer to "button" as its argument
        button.connect("toggled", self.callback, "check button 1")
        
        button.set_active(gtk.TRUE)
        
        button.show()
        # Insert button 1
        box.pack_start(button, gtk.FALSE, gtk.FALSE, 2)

        left.show()
        right.show()
        bleft.show()
        bright.show()
        
        self.label.show()
        self.text.show()
        box.show()

        self.window.add(box)

        self.window.show()

def main():
    gtk.main()
    return 0     

if __name__ == "__main__":
    GUI()
    main()



