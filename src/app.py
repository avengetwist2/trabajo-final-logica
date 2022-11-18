import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QWidget
from PyQt5 import uic
from PyQt5.QtCore import Qt, QPoint, QFile, QIODevice
# para que funcione la importacion src.....
from sys import path
path.append("../../")
# CLASES CREADAS PARA EL USO DE MVC
from models.Persona import Persona
from controlladores.userController import Account

#INTERFACES
from views.intefaz_admin import  SeccionAdministrador
from views.interfaz_usuario import SeccionUsuario

# PAQUETE DE ESTILOS EN EL ARCHIVO QRC
import views.ui.resource_rc
import views.ui.resource



class Principal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        archivo = os.getcwd().split('src')[0] + r'\src\views\ui\login.ui'
        self.logg = uic.loadUi(archivo, self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)

        f = QFile(':/res')
        if not f.open(QIODevice.ReadOnly):
            raise IOError('file open error')
        print(str(f.readAll(), 'utf-8'))
        f.close()

        # botones
        self.btn_login.clicked.connect(self.login)
        self.btn_close.clicked.connect(self.cerrarVentana)

        # pantallas
        self.view_usuario = SeccionUsuario()
        self.view_admin = SeccionAdministrador()

    def cerrarVentana(self):
        self.close()

    def login(self):
        # email
        mail = self.email.text()
        # password
        password = self.password.text()
        # objeto persona
        usr = Persona('', mail, '', '', password)
        # validacion
        logg = Account(usr)
        isValid = logg.login()[0]
        print(isValid)
        print(logg.login()[1])

        if isValid:
            # validacion de rol
            self.logg.hide()
            rol = logg.login()[1][0][5]
            # si es usuario pasara
            if rol == 1:
                self.view_usuario.exec_()
            # si es usuario administrador
            elif rol == 2:
                self.view_admin.exec_()
        else:
            self.message.setText(logg.login()[1])
            print(logg.login()[1])
"""  
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
"""


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    principal = Principal()
    principal.show()
    app.exec_()

