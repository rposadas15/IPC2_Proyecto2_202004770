class NodoListaNormal:

    def __init__(self, objeto):
        self.objeto = objeto
        self.siguiente = None
        self.anterior = None

class ListaNormal:

    def __init__(self):
        self.Primero = None
        self.Ultimo = None
        self.Tamaño = 0

    def Insertar(self, a):
        if self.Primero == None:            
            self.Primero = self.Ultimo = NodoListaNormal(a)
        else:
            aux = self.Ultimo
            self.Ultimo = aux.siguiente = NodoListaNormal(a)
            self.Ultimo.anterior = aux
        self.Tamaño += 1

    def Mostrar(self):
        aux = self.Primero
        while aux != None:
            print(aux.objeto)
            aux = aux.siguiente

class NodoListaNormal2:

    def __init__(self, L, C, frase, tiempo):
        self.L = L
        self.C = C
        self.frase = frase
        self.tiempo = tiempo
        self.siguiente = None
        self.anterior = None

class ListaNormal2:

    def __init__(self):
        self.Primero = None
        self.Ultimo = None
        self.Tamaño = 0

    def Insertar(self, a, b, c, d):
        if self.Primero == None:            
            self.Primero = self.Ultimo = NodoListaNormal2(a, b, c, d)
        else:
            aux = self.Ultimo
            self.Ultimo = aux.siguiente = NodoListaNormal2(a, b, c, d)
            self.Ultimo.anterior = aux
        self.Tamaño += 1

    def Mostrar(self):
        aux = self.Primero
        while aux != None:
            print(aux.L, aux.C, aux.frase, aux.tiempo)
            aux = aux.siguiente