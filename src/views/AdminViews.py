import sys
import os
from sys import path
path.append("../../")
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QWidget
from PyQt5 import uic
from PyQt5.QtCore import Qt, QPoint, QFile, QIODevice
# para que funcione la importacion src.....

# CLASES CREADAS PARA EL USO DE MVC
from src.models.Persona import Persona
from src.controlladores.userController import Account

#INTERFACES
from src.views.intefaz_admin import  SeccionAdministrador
from src.views.interfaz_usuario import SeccionUsuario





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
        # nombre boton iniciar secion -> btn_login
        self.btn_login.clicked.connect(self.login)
        # nombre boton cerrar ventana -> btn_close
        self.btn_close.clicked.connect(self.cerrarVentana)
        # nombre boton registro  -> btn_registro

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
# PAQUETE DE ESTILOS EN EL ARCHIVO QRC
import src.views.ui.resource_rc
import src.views.ui.resource


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    principal = Principal()
    principal.show()
    app.exec_()

