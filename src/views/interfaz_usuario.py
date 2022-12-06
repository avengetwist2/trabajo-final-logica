import sys
import os
from sys import path
path.append("../../")
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QGraphicsPixmapItem
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QPointF
from PyQt5.QtGui import QPixmap

#INTERFACES
from src.views.sillas_cine import  Sillas_Cine
from src.views.reservar import Reservar
from src.views.reservas_realizadas import Reservas_realizadas

# ESTA SECCION ES LA PANTALLA PRINCIPAL DEL USUARIO
class SeccionUsuario(QDialog):
    def __init__(self, data_transferida=None):
        QDialog.__init__(self)
        archivo = os.getcwd().split('src')[0] + r'\src\views\ui\menu.ui'
        uic.loadUi(archivo, self)


        #self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)

        # ajusta el ancho y largo de la pantalla
        self.setGeometry(QRect(50, 50, 1000, 600))
        # carga la imagen de fondo
        pixmap = QPixmap(r'{0}\src\views\ui\img\menuimg.png'.format(os.getcwd().split("src")[0]))
        self.imgfondo.setPixmap(pixmap)



        #botones  btn_reservas
        #boton de ver disponibilidades
        #self.btn_reserva.clicked.connect(self.reservar)
        #self.btn_cancelar.clicked.connect(self.acceder_disponibilidad)
        self.btn_reservas.clicked.connect(self.acceder_reservas_realizadas)
        self.btn_mapa.clicked.connect(self.acceder_disponibilidad)
        self.btn_close.clicked.connect(self.cerrar)


        # PANTALLAS
        self.view_sillas_disponibles = Sillas_Cine(data_transferida)
        self.view_reservar = Reservar()
        self.view_reserva_realizadas = Reservas_realizadas(data_transferida)


    def acceder_disponibilidad(self):

        #self.hide()
        self.view_sillas_disponibles.show()

    def reservar(self):
        #self.showMinimized()
        self.view_sillas_disponibles.show()

    def acceder_reservas_realizadas(self):
        self.view_reserva_realizadas.show()



    def cerrar(self):
        exit()


