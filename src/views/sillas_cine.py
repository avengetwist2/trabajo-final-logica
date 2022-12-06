import sys
import os
from sys import path
path.append("../../")
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QGraphicsPixmapItem
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QPointF
from PyQt5.QtGui import QPixmap

from src.models.reservaModel import ReservaModel
from src.controlladores.reservasController import ReservasController
from src.controlladores.peliculasController import PeliculasController


# ESTA SECCION ES LA PANTALLA PRINCIPAL DEL USUARIO
class Sillas_Cine(QDialog):
    def __init__(self, data_transferida=None):
        QDialog.__init__(self)
        self.data_transferida = data_transferida
        #print(data_transferida[1])
        archivo = os.getcwd().split('src')[0] + r'\src\views\ui\sillas_cine.ui'
        uic.loadUi(archivo, self)
        #self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)


        # ajusta el ancho y largo de la pantalla
        self.setGeometry(QRect(50, 50, 1000, 600))
        # carga la imagen de fondo
        pixmap = QPixmap(r'{0}\src\views\ui\img\CINEEEEE.png'.format(os.getcwd().split("src")[0]))
        self.lbl_img.setPixmap(pixmap)

        # label
        self.lbl_nombre.setText(data_transferida[1])

        #BOTONES
        # nombre boton cerrar ventana -> btn_close
        self.btn_close.clicked.connect(self.cerrarVentana)
        self.btn_actualizar.clicked.connect(self.redibujarTabla)
        self.btn_regresar.clicked.connect(self.regresar)

        #COMBO BOX
        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        # obtencion de datos para combobox de pelicula
        peliculas = PeliculasController()
        peli = []
        if peliculas.getPeliculas() != None :
            for i in peliculas.getPeliculas():
                peli.append(i[1])
        #colocar los datos en el comboBox
        self.combo_peli.addItems(peli)
        #print(peliculas.getPeliculas())
        #XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        # obtencion de datos para combobox de salas
        salas = PeliculasController()
        sala = []
        if salas.getSalas() != None:
            for i in salas.getSalas():
                sala.append(i[1])
        # colocar los datos en el comboBox
        self.combo_sala.addItems(sala)

        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        # obtencion de datos para combobox de horarios
        horarios = PeliculasController()
        hora = []
        if horarios.getHorarios() != None:
            for i in horarios.getHorarios():
                hora.append(i[1])
        # colocar los datos en el comboBox
        self.combo_horarios.addItems(hora)

        # se carga tabla inicial
        self.redibujarTabla()


    def redibujarTabla(self):
        #self.tbl_principal.
        # tabla
        # self.tbl_principal
        self.tbl_principal.setColumnCount(7)
        self.tbl_principal.setRowCount(6)

        # redimensionar el tamaño de las columnas
        self.tbl_principal.setColumnWidth(0, 74)
        self.tbl_principal.setColumnWidth(1, 74)
        self.tbl_principal.setColumnWidth(2, 74)
        self.tbl_principal.setColumnWidth(3, 74)
        self.tbl_principal.setColumnWidth(4, 75)
        self.tbl_principal.setColumnWidth(5, 75)
        self.tbl_principal.setColumnWidth(6, 75)

        self.columnas = self.optencion_de_datos()[0]
        self.listaDatos = self.optencion_de_datos()[1]



        # iteracion que sierve para crear la columna
        for fila, lista in enumerate(self.listaDatos):
            for columna, elemento in enumerate(lista):
                self.tbl_principal.setItem(fila, columna, QtWidgets.QTableWidgetItem(elemento))
                if self.optencion_de_datos()[2] != None:
                    for el in self.optencion_de_datos()[2]:
                        # print(el)
                        if (elemento == el[5]):
                            # print(str(letras[fila]) + str(columna))
                            # print(self.optencion_de_datos()[2])
                            self.tbl_principal.item(fila, columna).setBackground(QtGui.QColor('red'))

        # evento clic que toma el valor del item clickeado
        self.tbl_principal.cellDoubleClicked.connect(lambda: self.guardar_reserva(self.tbl_principal.currentItem()))

    def cerrarVentana(self):
        exit()

    def regresar(self):
        self.hide()

    def guardar_reserva(self, param):
        # INPUTS LINE_EDIT
        sala = (self.combo_sala.currentIndex() + 1)
        horario = (self.combo_horarios.currentIndex() + 1)
        pelicula = (self.combo_peli.currentIndex() + 1)

        obj_reserva = ReservaModel(horario,sala,param.text(),self.data_transferida[0],pelicula)
        crear_reserva = ReservasController(obj_reserva)
        crear_reserva.crearReservas_Sala_Horario_Peliculas()

        print(param.text())
        print(sala, horario, pelicula)
        #print(param.text())
        self.redibujarTabla()


    def optencion_de_datos(self):
        # INPUTS LINE_EDIT
        sala = (self.combo_sala.currentIndex() + 1)
        horario = (self.combo_horarios.currentIndex() + 1)
        pelicula = (self.combo_peli.currentIndex() + 1)

        #print(sala, horario, pelicula)

        #crear objeto de reserva para poder hacer la busqueda
        objeto_Reserva = ReservaModel(horario,sala)
        #creamos un objeto del controlador de reservas  y le pasamos un modelo de datos de reservas
        asientos_ocupados = ReservasController(objeto_Reserva)
        #print(asientos_ocupados.getReservasBy_Sala_Horario_Pelicula(pelicula))

        #letras para organizar los asientos del cine
        letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        #arreglo de asientos posibles teniendo en cuenta las letras y la cantidad de columnas
        data = []
        # for que itera y hace la agrupacion de las letras con los numeros
        for letra in letras:
            dat = []
            for i in range(9):
                dat.append(str(letra) + str(i))
            data.append(dat)

        #print(data)
        return [letras, data, asientos_ocupados.getReservasBy_Sala_Horario_Pelicula(pelicula)]


