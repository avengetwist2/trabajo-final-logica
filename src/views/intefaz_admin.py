import sys
import os
from sys import path
path.append("../../")
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QGraphicsPixmapItem
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QPointF
from PyQt5.QtGui import QPixmap

from src.views.admin_agregar_pelicula import Add_Pelicula
from src.views.admin_modificar_pelicula import Modificar_Pelicula


# ESTA SECCION ES LA PANTALLA PRINCIPAL DEL USUARIO ADMINISTRADOR
class SeccionAdministrador(QDialog):
    def __init__(self, data_transferida=None):
        QDialog.__init__(self)
        archivo = os.getcwd().split('src')[0] + r'\src\views\ui\menuadmin.ui'
        uic.loadUi(archivo, self)
        #imgmenuadmin

        #self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)

        # ajusta el ancho y largo de la pantalla
        self.setGeometry(QRect(50, 50, 1000, 600))
        # carga la imagen de fondo
        pixmap = QPixmap(r'{0}\src\views\ui\img\imgmenuadmin.png'.format(os.getcwd().split("src")[0]))
        self.imgfondo.setPixmap(pixmap)

        # pantallas
        self.view_agregar_pelicula = Add_Pelicula()
        self.view_modificar_pelicula = Modificar_Pelicula()

        # Botones
        self.btn_agregar.clicked.connect(self.abrir_registro)
        self.btn_modfilm.clicked.connect(self.abrir_modificar)

    def abrir_registro(self):
        self.view_agregar_pelicula.show()

    def abrir_modificar(self):
        self.view_modificar_pelicula.show()
