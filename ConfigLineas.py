class NodoConfigLineas:

    def __init__(self, numero, Ncomponentes, tiempo):
        self.numero = numero
        self.Ncomponentes = Ncomponentes
        self.tiempo = tiempo
        self.siguiente = None
        self.anterior = None

class ListaConfigLineas:

    def __init__(self):
        self.Primero = None
        self.Ultimo = None
        self.Tamaño = 0

    def Insertar(self, a, b, c):
        if self.Primero == None:
            self.Primero = self.Ultimo = NodoConfigLineas(a, b, c)
        else:
            aux = self.Ultimo
            self.Ultimo = aux.siguiente = NodoConfigLineas(a, b, c)
            self.Ultimo.anterior = aux
        self.Tamaño += 1

    def Mostrar(self):        
        aux = self.Primero
        while aux:
            print(aux.numero, aux.Ncomponentes, aux.tiempo)
            aux = aux.siguiente