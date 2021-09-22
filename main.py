import xml.etree.ElementTree as ET
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMessageBox, QFileDialog

from Informacion import Informacion
from Productos import LineasDeProduccion
from Productos import ObtenerProductos
from Productos import FabricarProductos

from ListaProductos import ListaProductos
ListaDeProductos = ListaProductos()

from ListaNormal import ListaNormal2
from ListaNormal import ListaNormal
ComponentesC = ListaNormal()
ListaLineasProduccion = ListaNormal()
ListaDeMovimientos = ListaNormal()
Productos = ListaNormal()
HacerProductosArchivo =  ListaNormal()

from ConfigLineas import ListaConfigLineas
ConfiguracionLineas = ListaConfigLineas()

import sys, os

class Interfaz(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(867, 450)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        Form.setStyleSheet("color: rgb(255, 255, 0);\nbackground-color: rgb(45, 109, 49);")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(410, 80, 441, 301))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 80, 381, 301))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(80, 30, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.listView = QtWidgets.QLabel(self.groupBox_2)
        self.listView.setGeometry(QtCore.QRect(20, 100, 341, 191))
        self.listView.setStyleSheet("border-style: solid;\nborder-width: 5px;\nborder-color: rgb(0, 0, 127);")
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.listView.setFont(font)
        self.listView.setObjectName("listView")
        pixmap = QPixmap('Maquina.jpg')
        self.listView.setPixmap(pixmap)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border-style: solid;\nborder-width: 5px;\nborder-color: rgb(0, 0, 127);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(175, 10, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("border-style: solid;\nborder-width: 5px;\nborder-color: rgb(0, 0, 127);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 390, 191, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("border-style: solid;\nborder-width: 5px;\nborder-color: rgb(0, 0, 127);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(390, 10, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("border-style: solid;\nborder-width: 5px;\nborder-color: rgb(0, 0, 127);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(600, 10, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("border-style: solid;\nborder-width: 5px;\nborder-color: rgb(0, 0, 127);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(770, 10, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("border-style: solid;\nborder-width: 5px;\nborder-color: rgb(0, 0, 127);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(522, 390, 112, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("border-style: solid;\nborder-width: 5px;\nborder-color: rgb(0, 0, 127);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(210, 390, 220, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("border-style: solid;\nborder-width: 5px;\nborder-color: rgb(0, 0, 127);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem('Seleccione Producto')
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(640, 390, 210, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("border-style: solid;\nborder-width: 5px;\nborder-color: rgb(0, 0, 127);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem('Seleccione Reporte')

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.ConfigurarMaquina)
        self.pushButton_2.clicked.connect(self.CargarProductos)
        self.pushButton_3.clicked.connect(self.CrearProducto)
        self.pushButton_4.clicked.connect(self.CrearTodosLosProductos)
        self.pushButton_5.clicked.connect(self.Informacion)
        self.pushButton_6.clicked.connect(self.Salir)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def ConfigurarMaquina(self):
        buscar = QFileDialog.getOpenFileName(filter="Archivo (*.xml)")[0]
        mytree = ET.parse(buscar)
        myroot = mytree.getroot()

        for x in myroot:
            for j in x:
                for a1 in j.findall('Numero'):
                    for a2 in j.findall('CantidadComponentes'):
                        for a3 in j.findall('TiempoEnsamblaje'):
                            ConfiguracionLineas.Insertar(int(a1.text), int(a2.text), int(a3.text))

        aux = ConfiguracionLineas.Primero
        while aux != None:
            max = aux.Ncomponentes
            ListaPrueba = ListaNormal()
            for columnas in range(1, (max + 1)):
                ListaPrueba.Insertar('C' + str(columnas))
            ComponentesC.Insertar(ListaPrueba)
            ListaPrueba = ListaNormal()
            aux = aux.siguiente
        
        aux2 = ConfiguracionLineas.Primero
        aux3 = ComponentesC.Primero
        while aux2 != None:            
            ListaLineasProduccion.Insertar(LineasDeProduccion(aux3.objeto, aux2.tiempo, ('L' + str(aux2.numero))))#, ''))
            aux2 = aux2.siguiente
            aux3 = aux3.siguiente

        for x in myroot:
            for j in x:
                for b1 in j.findall('nombre'):
                    for b2 in j.findall('elaboracion'):
                        ListaDeProductos.Insertar(b1.text, b2.text)

        aux4 = ListaDeProductos.Primero
        while aux4 != None:
            self.comboBox.addItem(aux4.nombre)
            Movimientos = ListaNormal()
            elaborar = aux4.elaboracion
            elaborar += ' '
            temporal = ''
            for a in elaborar:
                if a == ' ':                    
                    Movimientos.Insertar(temporal)
                    temporal = ''
                else:
                    temporal += a
            ListaDeMovimientos.Insertar(Movimientos)
            Movimientos = ListaNormal()
            aux4 = aux4.siguiente

        aux5 = ListaDeProductos.Primero
        aux6 = ListaDeMovimientos.Primero
        while aux5 != None:
            Productos.Insertar(ObtenerProductos(aux5.nombre, aux6.objeto, ListaNormal2(), 1))
            aux5 = aux5.siguiente
            aux6 = aux6.siguiente

        return ListaLineasProduccion, Productos

    def CargarProductos(self):
        buscar = QFileDialog.getOpenFileName(filter="Archivo (*.xml)")[0]
        mytree = ET.parse(buscar)
        myroot2 = mytree.getroot()

        ProductosArchivo = ListaNormal()

        for x in myroot2:
            for j in x:                
                ProductosArchivo.Insertar(j.text)        
        
        for x in myroot2.findall('Nombre'):            
            HacerProductosArchivo.Insertar(FabricarProductos(x.text, ProductosArchivo))

        return HacerProductosArchivo

    def CrearProducto(self, nombre):
        nombre = self.comboBox.currentText()
        aux = Productos.Primero
        while aux != None:
            if nombre == aux.objeto.getNombre():
                movimientos = aux.objeto.getProceso()
                proceso = aux.objeto.getElaboracion()
            aux = aux.siguiente

        t = 1
        lasL = ListaLineasProduccion.Primero
        proc = proceso.Primero
        lineaposicion = 1
        tiempoespera = 0

        while proc != None:
            while lasL != None:

                lasC = lasL.objeto.getListaC().Primero
                t = lasL.objeto.getTiempo()
                if lasL.anterior != None:
                    tt = lasL.anterior.objeto.getTiempo()
                else:
                    tt = 0
                
                while lasC != None:
                    
                    if (str(lasL.objeto.getListaL()) + str(lasC.objeto)) == proc.objeto:
                        movimientos.Insertar(lasL.objeto.getListaL(), lasC.objeto, 'Mover a: ' + (str(lasL.objeto.getListaL()) + str(lasC.objeto)) + ' en el Tiempo' + str(t), t)
                        #print('se movio a', lasL.objeto.getListaL(), lasC.objeto, lasL.objeto.getTiempo())
                        
                        if lineaposicion == 1:
                            tiempoespera = 0                            
                        elif lineaposicion <= proceso.Tamaño:
                            if proceso.Tamaño - lineaposicion == 1:
                                tiempoespera = -1                                
                            elif lineaposicion == proceso.Tamaño:
                                tiempoespera = int(lasL.objeto.getTiempo())
                            else:
                                tiempoespera = int(lasL.objeto.getTiempo())

                        if tiempoespera > 0:                           
                            if proc.objeto[-1] > proc.anterior.objeto[-1]:
                                if lineaposicion == proceso.Tamaño:
                                    if t > tt:
                                        t += 1
                                        movimientos.Insertar(lasL.objeto.getListaL(), lasC.objeto, 'Esperar: ' + (str(lasL.objeto.getListaL()) + str(lasC.objeto)) + ' en el Tiempo' + str(t), t)
                                        t += int(lasL.objeto.getTiempo())
                                        movimientos.Insertar(lasL.objeto.getListaL(), lasC.objeto, 'Ensamblar: ' + (str(lasL.objeto.getListaL()) + str(lasC.objeto)) + ' en el Tiempo' + str(t), t)
                                    else:
                                        t += int(lasL.objeto.getTiempo())
                                        movimientos.Insertar(lasL.objeto.getListaL(), lasC.objeto, 'Ensamblar: ' + (str(lasL.objeto.getListaL()) + str(lasC.objeto)) + ' en el Tiempo' + str(t), t)
                                else:
                                    t += int(lasL.objeto.getTiempo())
                                    movimientos.Insertar(lasL.objeto.getListaL(), lasC.objeto, 'Ensamblar: ' + (str(lasL.objeto.getListaL()) + str(lasC.objeto)) + ' en el Tiempo' + str(t), t)
                            elif proc.objeto[-1] < proc.anterior.objeto and t > tt:
                                t += 1
                                movimientos.Insertar(lasL.objeto.getListaL(), lasC.objeto, 'Esperar: ' + (str(lasL.objeto.getListaL()) + str(lasC.objeto)) + ' en el Tiempo' + str(t), t)
                                t += int(lasL.objeto.getTiempo())
                                movimientos.Insertar(lasL.objeto.getListaL(), lasC.objeto, 'Ensamblar: ' + (str(lasL.objeto.getListaL()) + str(lasC.objeto)) + ' en el Tiempo' + str(t), t)
                            else:
                                if proc.objeto[-1] < proc.anterior.objeto and lineaposicion == proceso.Tamaño:
                                    t += 1
                                    movimientos.Insertar(lasL.objeto.getListaL(), lasC.objeto, 'Esperar: ' + (str(lasL.objeto.getListaL()) + str(lasC.objeto)) + ' en el Tiempo' + str(t), t)
                                    t += int(lasL.objeto.getTiempo())
                                    movimientos.Insertar(lasL.objeto.getListaL(), lasC.objeto, 'Ensamblar: ' + (str(lasL.objeto.getListaL()) + str(lasC.objeto)) + ' en el Tiempo' + str(t), t)
                                else:
                                    t += int(lasL.objeto.getTiempo())
                                    movimientos.Insertar(lasL.objeto.getListaL(), lasC.objeto, 'Ensamblar: ' + (str(lasL.objeto.getListaL()) + str(lasC.objeto)) + ' en el Tiempo' + str(t), t)
                        elif tiempoespera == -1:
                            t += int(lasL.objeto.getTiempo())
                            movimientos.Insertar(lasL.objeto.getListaL(), lasC.objeto, 'Ensamblar: ' + (str(lasL.objeto.getListaL()) + str(lasC.objeto)) + ' en el Tiempo' + str(t), t)
                            t += 1
                            movimientos.Insertar(lasL.objeto.getListaL(), lasC.objeto, 'Esperar: ' + (str(lasL.objeto.getListaL()) + str(lasC.objeto)) + ' en el Tiempo' + str(t), t)
                        else:
                            t += int(lasL.objeto.getTiempo())
                            movimientos.Insertar(lasL.objeto.getListaL(), lasC.objeto, 'Ensamblar: ' + (str(lasL.objeto.getListaL()) + str(lasC.objeto)) + ' en el Tiempo' + str(t), t)

                        
                        lasL.objeto.setTiempo(t)
                        #print(proc.objeto[0] + str(int(proc.objeto[1])))
                        #extra = proc.objeto[-2] + str(int(proc.objeto[-1]) + 1)
                        #print(extra)
                        #lasL.objeto.setSobrante(extra)

                        break
                    else:
                        bandera = ListaNormal2()                        
                        if proc.objeto.find(lasL.objeto.getListaL()) != -1:
                            #print(lasL.objeto.getListaL(), lasC.objeto, proc.objeto.find(lasL.objeto.getListaL()))
                            bandera.Insertar(lasL.objeto.getListaL(), lasC.objeto, 'Mover a: ' + (str(lasL.objeto.getListaL()) + str(lasC.objeto)) + ' en el Tiempo' + str(t), t)
                            if movimientos.Tamaño == 0:
                                #print('se movio a', lasL.objeto.getListaL(), lasC.objeto, lasL.objeto.getTiempo())
                                movimientos.Insertar(lasL.objeto.getListaL(), lasC.objeto, 'Mover a: ' + (str(lasL.objeto.getListaL()) + str(lasC.objeto)) + ' en el Tiempo' + str(t), t)
                                t += 1
                            else:
                                auxiliar = bandera.Primero
                                while auxiliar != None:                                    
                                    if auxiliar.C.find(lasC.objeto) == -1:                                        
                                        movimientos.Insertar(lasL.objeto.getListaL(), lasC.objeto, 'Mover a: ' + (str(lasL.objeto.getListaL()) + str(lasC.objeto)) + ' en el Tiempo' + str(t), t)
                                        t += 1
                                    auxiliar = auxiliar.siguiente
                                
                    lasC = lasC.siguiente
                lasL = lasL.siguiente
            lasL = ListaLineasProduccion.Primero
            lineaposicion += 1
            proc = proc.siguiente

        lineaposicion = 1
        t = 1
        proc = Productos.Primero     
        aux = Productos.Primero

        #self.Grapho(nombre)

        movimientos.Mostrar()
        print('--')
        proceso.Mostrar()
        print('--')
        self.Grapho(nombre)

    def Grapho(self, nombre):
        aux = Productos.Primero
        while aux != None:
            if aux.objeto.getNombre() == nombre:
                proceso = aux.objeto.getElaboracion()
            aux = aux.siguiente

        archivo = open(nombre + '.dot', 'w')
        archivo.write('digraph ' + nombre + ' { ')
        archivo.write( 'bgcolor = "#0000FF" \n')
        archivo.write(  'node[shape = "circle" fillcolor = "#FFFF00" style = filled] \n')
        archivo.write(  'fontsize = "20" \n')
        archivo.write('label = ' + nombre + '\n')

        proc = proceso.Primero
        while proc != None:
            if proc.siguiente != None:
                archivo.write('rank = same { ' + proc.objeto + '->' + proc.siguiente.objeto + ' }\n')
            proc = proc.siguiente

        archivo.write('}')
        archivo.close()
        os.system('cmd /c "dot.exe -Tpng ' + (nombre + '.dot') + ' -o ' + (nombre + '.png') + '"')
        os.startfile(nombre + '.png')

    def XML(self, nombre):
        aux = Productos.Primero
        while aux != None:
            if aux.objeto.getNombre() == nombre:
                proceso = aux.objeto.getProceso()
            aux = aux.siguiente

    def CrearTodosLosProductos(self):
        print('B4')

    def Informacion(self):
        print('B5')
        self.Form2 = QtWidgets.QWidget()
        self.ui2 = Informacion()
        self.ui2.setupUi(self.Form2)
        self.Form2.show()
    
    def Salir(self):
        sys.exit()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", " Digital Intelligence, S. A. "))
        self.groupBox.setTitle(_translate("Form", "PROCESO"))
        self.groupBox_2.setTitle(_translate("Form", "PRODUCTO"))
        self.label.setText(_translate("Form", "NOMBRE"))
        self.label_2.setText(_translate("Form", "Maquinaria"))
        self.pushButton.setText(_translate("Form", "CONFIGURAR\nMAQUINA"))
        self.pushButton_2.setText(_translate("Form", "CARGAR TODOS \nLOS PRODUCTOS"))
        self.pushButton_3.setText(_translate("Form", "CREAR PRODUCTO"))
        self.pushButton_4.setText(_translate("Form", "CREAR TODOS LOS\nPRODUCTOS"))
        self.pushButton_5.setText(_translate("Form", "INFORMACION"))
        self.pushButton_6.setText(_translate("Form", "SALIR"))
        self.pushButton_7.setText(_translate("Form", "REPORTES"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Interfaz()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())