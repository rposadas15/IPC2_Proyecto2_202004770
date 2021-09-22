class NodoProductos:

    def __init__(self, nombre, eleboracion):
        self.nombre = nombre
        self.elaboracion = eleboracion
        self.siguiente = None
        self.anterior = None

class ListaProductos:

    def __init__(self):
        self.Primero = None
        self.Ultimo = None
        self.Tamaño = 0

    def Insertar(self, a, b):
        if self.Primero == None:            
            self.Primero = self.Ultimo = NodoProductos(a, b)
        else:
            aux = self.Ultimo
            self.Ultimo = aux.siguiente = NodoProductos(a, b)
            self.Ultimo.anterior = aux
        self.Tamaño += 1

    def Mostrar(self):
        aux = self.Primero
        while aux != None:
            print(aux.nombre, aux.elaboracion)
            aux = aux.siguiente