import pygtk
pygtk.require("2.0")
import gtk
import time

class GUI:
    def __init__(self):
        self.__lista=[]
        
        self.ventana=gtk.Window()
        self.ventana.connect("delete_event",self.terminar)
        self.ventana.set_border_width(20)
        self.barra=gtk.ProgressBar()
        
        self.spin=gtk.SpinButton(gtk.Adjustment(upper=100000,step_incr=1))
        self.boton=gtk.Button("Ejecutar")
        self.caja=gtk.VBox(True,5)

        self.boton.connect("clicked",self.ejecutar)
        
        

        self.caja.pack_start(self.spin)
        self.caja.pack_start(self.boton)
        self.caja.pack_start(self.barra)
        self.ventana.add(self.caja)

        self.spin.show()
        self.boton.show()
        self.barra.show()
        self.caja.show()
        self.ventana.show()

    def main(self):
        gtk.main()
    def terminar(self,Widget,data=None):
        gtk.main_quit()

    def ejecutar(self,Widget,data=None):
        longitud=self.spin.get_value_as_int()
        self.__lista=[0]*longitud
        self.barra.set_pulse_step(float(1.0/longitud))
        self.busqueda(longitud)

    def busqueda(self,longitud):
	fraction = float(1.0/longitud)
	acum = 0.0
        for cont in range(0,longitud):
	    acum += fraction
            self.barra.set_fraction(acum)
	    time.sleep(1)
	    #self.barra.pulse()
        

def main():
    i=GUI()
    i.main()

main()
