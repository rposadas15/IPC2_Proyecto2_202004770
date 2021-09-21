class LineasDeProduccion:

    def __init__(self, ListaC, tiempo, ListaL, proceso, totaltiempoProduccion, exceso):
        self.ListaC = ListaC
        self.tiempo = tiempo
        self.ListaL = ListaL
        self.proceso = proceso
        self.totaltiempoProduccion = totaltiempoProduccion
        self.exceso = exceso

    #Get
    def getListaC(self):
        return self.ListaC

    def getTiempo(self):
        return self.tiempo

    def getListaL(self):
        return self.ListaL

    def getProceso(self):
        return self.proceso

    def getTotaltiempoProduccion(self):
        return self.totaltiempoProduccion

    def getExceso(self):
        return self.exceso

    #Set
    def setListaC(self, ListaC):
        self.ListaC = ListaC

    def setTiempo(self, tiempo):
        self.tiempo = tiempo

    def setListaL(self, ListaL):
        self.ListaL = ListaL

    def setProceso(self, proceso):
        self.proceso = proceso

    def setTotaltiempoProduccion(self, totaltiempoProduccion):
        self.totaltiempoProduccion += totaltiempoProduccion

    def setExceso(self, exceso):
        self.exceso = exceso

class ObtenerProductos:

    def __init__(self, nombre, elaboracion):
        self.nombre = nombre        
        self.elaboracion = elaboracion

    #Get
    def getNombre(self):
        return self.nombre
    
    def getElaboracion(self):
        return self.elaboracion

    #Set
    def setNombre(self, nombre):
        self.nombre = nombre

    def setElaboracion(self, elaboracion):
        self.elaboracion = elaboracion

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