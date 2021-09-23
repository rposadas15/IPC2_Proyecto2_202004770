class LineasDeProduccion:

    def __init__(self, ListaC, tiempo, ListaL):
        self.ListaC = ListaC
        self.tiempo = tiempo
        self.ListaL = ListaL

    #Get
    def getListaC(self):
        return self.ListaC

    def getTiempo(self):
        return self.tiempo

    def getListaL(self):
        return self.ListaL

    #Set
    def setListaC(self, ListaC):
        self.ListaC = ListaC

    def setTiempo(self, tiempo):
        self.tiempo = tiempo

    def setListaL(self, ListaL):
        self.ListaL = ListaL

class ObtenerProductos:

    def __init__(self, nombre, elaboracion, proceso, tiempo):
        self.nombre = nombre        
        self.elaboracion = elaboracion
        self.proceso = proceso
        self.tiempo = tiempo

    #Get
    def getNombre(self):
        return self.nombre
    
    def getElaboracion(self):
        return self.elaboracion

    def getProceso(self):
        return self.proceso

    def getTiempo(self):
        return self.tiempo

    #Set
    def setNombre(self, nombre):
        self.nombre = nombre

    def setElaboracion(self, elaboracion):
        self.elaboracion = elaboracion

    def setProceso(self, proceso):
        self.proceso = proceso

    def setTiempo(self, tiempo):
        self.tiempo = tiempo

class FabricarProductos:

    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos

    #Get
    def getNombre(self):
        return self.nombre
    
    def getProductos(self):
        return self.productos

    #Set
    def setNombre(self, nombre):
        self.nombre = nombre

    def setProductos(self, productos):
        self.productos = productos