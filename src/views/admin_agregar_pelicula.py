import sys
import os
from sys import path
path.append("../../")
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QGraphicsPixmapItem
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QPointF
from PyQt5.QtGui import QPixmap

# importacion de modulo de la calse y el controlador
from src.controlladores.peliculasController import PeliculasController
from src.models.Peliculas import Pelicula


# ESTA SECCION ES LA PANTALLA PRINCIPAL DEL USUARIO ADMINISTRADOR
class Add_Pelicula(QDialog):
    def __init__(self, data_transferida=None):
        QDialog.__init__(self)
        archivo = os.getcwd().split('src')[0] + r'\src\views\ui\agregapelicula.ui'
        uic.loadUi(archivo, self)

        #self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)

        # ajusta el ancho y largo de la pantalla
        self.setGeometry(QRect(50, 50, 1000, 600))
        # carga la imagen de fondo
        pixmap = QPixmap(r'{0}\src\views\ui\img\imgagregar.png'.format(os.getcwd().split("src")[0]))
        self.imgfondo.setPixmap(pixmap)

        # botones
        self.btn_agregar.clicked.connect(self.registrar_pelicula)

    def registrar_pelicula(self):
        try:
            #toma los datos de los inputs de la interfaz
            perlicula = self.pelicula.text()
            duracion = self.duracion.text()
            genero = self.genero.text()
            #horario = self.nombre.text()
            idioma = self.idioma.text()
            actor = self.actor.text()


            if perlicula != '' or duracion != '' or genero != '' or idioma != '' or actor != '' :
                print('paso el condicional')
                # crea un objeto de la clase pelicula
                obj_pelicula = Pelicula(duracion,perlicula,actor,genero,idioma)

                # creamos una instancia de la clase controlladora de la pelicula
                controller_pelicula = PeliculasController()
                controller_pelicula.crearPeliculas(obj_pelicula)

                self.pelicula.setText('')
                self.duracion.setText('')
                self.genero.setText('')
                self.idioma.setText('')
                self.actor.setText('')
                self.message.setText('El registro fue exitoso')
            else:
                self.message.setText('Los campos no pueden estar vacios')
        except Exception as ex:
            print(ex)


