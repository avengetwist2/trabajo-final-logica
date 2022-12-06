import sys
import os
from sys import path
path.append("../../")
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QGraphicsPixmapItem
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QPointF
from PyQt5.QtGui import QPixmap

# IMPORTACION DE MODELOS Y CONTROLADORES
from src.models.Persona import Persona
from src.controlladores.userController import Account

# ESTA SECCION ES LA PANTALLA PRINCIPAL DEL USUARIO ADMINISTRADOR
class Registro(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        archivo = os.getcwd().split('src')[0] + r'\src\views\ui\registarse.ui'
        uic.loadUi(archivo, self)

        #self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)

        # ajusta el ancho y largo de la pantalla
        self.setGeometry(QRect(50, 50, 1000, 600))
        # carga la imagen de fondo
        pixmap = QPixmap(r'{0}\src\views\ui\img\imgregistroo.png'.format(os.getcwd().split("src")[0]))
        self.imgfondo.setPixmap(pixmap)


        # BOTONES
        self.btn_close.clicked.connect(self.cerrarVentana)
        self.btn_regresar.clicked.connect(self.regresar)
        self.btn_registarse.clicked.connect(self.registrar)

        # PANTALLAS
        #self.principal = Principal()



    def cerrarVentana(self):
        exit()

    def regresar(self):
        self.hide()


    def registrar(self):
        nombre = self.nombre.text()
        telefono = self.telefono.text()
        correo = self.correo.text()
        rol = self.rol.text()
        password = self.password.text()

        if nombre != '' and telefono != '' and correo != '' and rol != '' and password != '':
            # modelo de persona
            persona = Persona(nombre, correo, telefono, rol, password)
            # registro
            registro = Account(persona)
            registro.register()


            self.messagee.setText('El usuario fue registrado exitosamente')
            self.nombre.setText('')
            self.telefono.setText('')
            self.correo.setText('')
            self.rol.setText('')
            self.password.setText('')
        else:
            self.messagee.setText('Los campos deben estar llenos')

