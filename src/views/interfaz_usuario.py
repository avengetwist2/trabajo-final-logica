import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog
from PyQt5 import uic
from PyQt5.QtCore import Qt, QPoint



# ESTA SECCION ES LA PANTALLA PRINCIPAL DEL USUARIO
class SeccionUsuario(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        archivo = os.getcwd().split('src')[0] + r'\src\views\ui\RegistroIngreso.ui'
        uic.loadUi(archivo, self)



