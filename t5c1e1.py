#!/usr/bin/env python

import pygtk
import gtk

class GUI:
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.show()
        
    def main(self):
        gtk.main()
        
def main():
    gui = GUI()
    gui.main()
    
main()