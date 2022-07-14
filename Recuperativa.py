# Guia Recuperativa Unidad 2 Programacion Avanzada - Matias Fonseca.
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Ventana_Principal(Gtk.Window):
    def __init__(self):
        super().__init__(title= "Guia Recuperativa Unidad 2")

        self.contenedor = Gtk.Box(spacing = 20)
        self.contenedor.set_orientation(Gtk.Orientation.VERTICAL)
        self.add(self.contenedor)

        self.etiqueta = Gtk.Label(label= "Entrada 1")
        self.contenedor.add(self.etiqueta)

        self.entrada = Gtk.Entry()
        self.entrada.connect("activate", self.mostrar_resultado)
        self.contenedor.add(self.entrada)

        self.etiqueta_1 = Gtk.Label(label= "Entrada 2")
        self.contenedor.add(self.etiqueta_1)

        self.entrada_1 = Gtk.Entry()
        self.entrada_1.connect("activate", self.mostrar_resultado)
        self.contenedor.add(self.entrada_1)

        self.etiqueta_2 = Gtk.Label(label= "Resultado")
        self.contenedor.add(self.etiqueta_2)

        self.resultado = Gtk.Label()
        self.contenedor.add(self.resultado)

        self.boton = Gtk.Button(label= "Aceptar")
        self.boton.connect("clicked", self.aceptar)
        self.contenedor.add(self.boton)
        
        self.boton_1 = Gtk.Button(label="Guardar")
        self.boton_1.connect("clicked", self.guardar)
        self.contenedor.add(self.boton_1)

        self.boton_2 = Gtk.Button(label="Reiniciar")
        self.boton_2.connect("clicked", self.reiniciar)
        self.contenedor.add(self.boton_2)
        
        self.show_all()

    def obtener_vocales(self, cadena):
        vocales = 'aeiouAEIOU'

        return [c for c in cadena if c in vocales]
    
    def mostrar_resultado(self, enter=None):
        
        cadena = self.entrada.get_text()

        if cadena.isalpha() == True:
            cadena = self.obtener_vocales(cadena)
            cadena = len(cadena)
        else:
            try:
                cadena = int(cadena)
            except ValueError:
                print("Ingrese netamente letras o numeros")

        cadena_1 = self.entrada_1.get_text()

        if cadena_1.isalpha() == True:
            cadena_1 = self.obtener_vocales(cadena_1)
            cadena_1 = len(cadena_1)
        else:
            try:
                cadena_1 = int(cadena_1)
            except ValueError:
                print("Ingrese netamente letras o numeros")

        self.resultado.set_label(str(cadena + cadena_1))

    def aceptar(self, btn=None):
        print("Hola")
        entrada = self.entrada.get_text()
        entrada_1 = self.entrada_1.get_text()
        resultado = self.resultado.get_label()

        dialogo_aceptar = Gtk.MessageDialog(
            transient_for = self,
            flags = 0,
            title = "Datos ingresados",
            message_type = Gtk.MessageType.INFO,
            buttons = Gtk.ButtonsType.OK,
            text = "El usuario tecleo: \n"
                   f"Entrada 1: {entrada} \n"
                   f"Entrada 2: {entrada_1} \n"
                   f"Resultado: {resultado} \n"
            )   
        respuesta = dialogo_aceptar.run()

        if respuesta == Gtk.ResponseType.OK:
            dialogo_aceptar.destroy()

        dialogo_aceptar.destroy()

    def guardar(self, btn=None):
        pass

    def reiniciar(self, btn=None):
        dialogo_reiniciar = Gtk.MessageDialog(
            transient_for = self,
            flags = 0,
            title = "¿Limpiar las entradas de texto?",
            message_type = Gtk.MessageType.WARNING,
            buttons = Gtk.ButtonsType.OK_CANCEL,
            text = "Si las limpia, va a tener que escribir de nuevo."            
        )
        respuesta = dialogo_reiniciar.run()
        
        if respuesta == Gtk.ResponseType.OK:
            self.entrada.set_text(" ")
            self.entrada_1.set_text(" ")
            self.resultado.set_label(" ")
        if respuesta == Gtk.ResponseType.CANCEL:
            dialogo_reiniciar.destroy()
        
        dialogo_reiniciar.destroy()

if __name__ == "__main__":
    ventana = Ventana_Principal()
    ventana.set_border_width(10)
    ventana.maximize()
    ventana.connect("destroy", Gtk.main_quit)
    ventana.show_all()
    Gtk.main()