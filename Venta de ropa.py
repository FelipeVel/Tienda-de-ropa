from tkinter import *

class Prenda:
        
    def getPrecio(self):
        pass
        
    def getColor(self):
        pass
        
class Camiseta(Prenda):
    
    def __init__(self, color):
        self.color = color
        
    def getPrecio(self):
        return 25000
    
    def getColor(self):
        return self.color
    
class Pantalon(Prenda):
    
    def __init__(self, color):
        self.color = color
        
    def getPrecio(self):
        return 70000
    
    def getColor(self):
        return self.color
    
class Zapatos(Prenda):
    
    def __init__(self, color):
        self.color = color
        
    def getPrecio(self):
        return 110000
    
    def getColor(self):
        return self.color
    
class Ventana:
    
    def __init__(self, master):
        frame = Frame(master)
        master.title("Tienda de ropa")
        frame.pack()
        color= StringVar()
        self.carrito = list()
        self.azul = Radiobutton (frame, text="Azul", variable=color, value="Azul")
        self.azul.pack()
        self.rojo = Radiobutton (frame, text="Rojo", variable=color, value="Rojo")
        self.rojo.pack()
        self.verde = Radiobutton (frame, text="Verde", variable=color, value="Verde")
        self.verde.pack()
        self.negro = Radiobutton (frame, text="Negro", variable=color, value="Negro")
        self.negro.pack()
        self.camisa = Button(frame, text="Camiseta", command=self.añadir("Camiseta", color))
        self.camisa.pack(side=LEFT)
        self.pantalon = Button(frame, text="Pantalon", command=self.añadir("Pantalon", color))
        self.pantalon.pack(side=LEFT)
        self.zapatos = Button(frame, text="Zapatos", command=self.añadir("Zapatos", color))
        self.zapatos.pack(side=RIGHT)
        self.comprar = Button(frame, text="Finalizar compra", command=self.total())
        self.comprar.pack(side=BOTTOM)
        
    def añadir(self, prenda, color):
        if prenda=="Camiseta" :
            objeto = Camiseta(color)
            print("Se añadio una camiseta color"+color)
        elif prenda == "Pantalon":
            objeto = Pantalon(color)
            print ("Se añadio un pantalon color "+color)
        elif prenda == "Zapatos" :
            objeto = Zapatos(color)
            print("Se añadieron unos zapatos color "+color)
        
        self.carrito.append(objeto)
        
    def total(self):
        total = 0
        for i in self.carrito:
            total = total + i.getPrecio()
        return total
    
'''--------------------------------------------------------------------'''

root = Tk()
app = Ventana(root)
root.mainloop()