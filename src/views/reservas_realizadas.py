import sys
import os
from sys import path
path.append("../../")
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QGraphicsPixmapItem, QListWidgetItem
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QPointF
from PyQt5.QtGui import QPixmap

# IMPORTACION DE MODELOS Y CONTROLADORES
from src.controlladores.reservasController import ReservasController

# ESTA SECCION ES LA PANTALLA PRINCIPAL DEL USUARIO ADMINISTRADOR
class Reservas_realizadas(QDialog):
    def __init__(self, data_transferida=None):
        QDialog.__init__(self)
        archivo = os.getcwd().split('src')[0] + r'\src\views\ui\reservas_realizadas.ui'
        uic.loadUi(archivo, self)
        self.data_transferida = data_transferida

        #print(self.data_transferida )
        datos_reservas = ReservasController()

        id = data_transferida[0]
        reservas_data = datos_reservas.getReservasByPersonaId(id)

        for i in reservas_data:
            listWidgetItem = QListWidgetItem(str(f" {i[0]} - {i[1]} - {i[2]} - {i[3]}"))
            self.list_reservas.addItem(listWidgetItem)

        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)

        # ajusta el ancho y largo de la pantalla
        #self.setGeometry(QRect(50, 50, 1000, 600))
        # carga la imagen de fondo
        #pixmap = QPixmap(r'{0}\src\views\ui\img\imgregistro2.png'.format(os.getcwd().split("src")[0]))
        #self.imgfondo.setPixmap(pixmap)

        # BOTONES
        self.btn_actualizar.clicked.connect(self.actualizar)



    def actualizar(self):

        print(self.data_transferida)

        """ 
       
        """