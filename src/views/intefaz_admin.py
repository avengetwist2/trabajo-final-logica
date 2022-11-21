import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog
from PyQt5 import uic
from PyQt5.QtCore import Qt, QPoint


# ESTA SECCION ES LA PANTALLA PRINCIPAL DEL USUARIO ADMINISTRADOR
class SeccionAdministrador(QDialog):
    def __init__(self):
        QDialog.__init__(self, data_transferida=None)

        self.data_transferida = data_transferida
        archivo = os.getcwd().split('src')[0] + r'\src\views\ui\admin.ui'
        uic.loadUi(archivo, self)
