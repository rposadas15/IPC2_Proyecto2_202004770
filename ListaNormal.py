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

    def ComboBox(self, comboBox):
        aux = self.Primero
        while aux != None:
            comboBox.addItem(aux.objeto)
            aux = aux.siguiente