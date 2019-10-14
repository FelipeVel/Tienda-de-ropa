import tkinter as tk

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
    
    def getPrenda(self):
        return "Camiseta"
    
class Pantalon(Prenda):
    
    def __init__(self, color):
        self.color = color
        
    def getPrecio(self):
        return 70000
    
    def getColor(self):
        return self.color
    
    def getPrenda(self):
        return "Pantalon"
    
class Zapatos(Prenda):
    
    def __init__(self, color):
        self.color = color
        
    def getPrecio(self):
        return 110000
    
    def getColor(self):
        return self.color
    
    def getPrenda(self):
        return "Zapatos"

carrito=[]

def añadirCamiseta():
    color=colores[v.get()]
    objeto = Camiseta(color)
    print("Se añadio una camiseta color "+color)
    carrito.append(objeto)
    
def añadirPantalon():
    color=colores[v.get()]
    objeto = Pantalon(color)
    print ("Se añadio un pantalon color "+color)
    carrito.append(objeto)
        
def añadirZapatos():
    color=colores[v.get()]
    objeto = Zapatos(color)
    print("Se añadieron unos zapatos color "+color)
    carrito.append(objeto)
 
def total():
    total = 0
    for i in carrito:
        total = total + i.getPrecio()
    print(str(total))
    factura = tk.Tk()
    for i in range(len(carrito)):
        tk.Label(factura,
                 text=carrito[i].getPrenda()+" "+str(carrito[i].getColor())+"\t"+str(carrito[i].getPrecio())).pack()
    tk.Label(factura,
             text="Total: "+str(total)).pack()
    carrito.clear()
    
root = tk.Tk()

v = tk.IntVar()
v.set(0)

colores = [
    "Rojo","Verde","Azul","Amarillo"
]

def ShowChoice():
    print(v.get())

tk.Label(root, 
         text="""Seleccione el color de su prenda:""",
         justify = tk.LEFT,
         padx = 20).pack()

for val, color in enumerate(colores):
    tk.Radiobutton(root, 
                  text=color,
                  padx = 20, 
                  variable=v,
                  value=val).pack(anchor=tk.W)
    

camisa = Button(root, text="Camiseta", command=añadirCamiseta)
camisa.pack(side=LEFT)
pantalon = Button(root, text="Pantalon", command=añadirPantalon)
pantalon.pack(side=LEFT)
zapatos = Button(root, text="Zapatos", command=añadirZapatos)
zapatos.pack(side=RIGHT)
comprar = Button(root, text="Finalizar compra", command=total)
comprar.pack(side=BOTTOM)


root.mainloop()