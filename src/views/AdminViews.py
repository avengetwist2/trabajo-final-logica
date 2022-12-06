import sys
import os
from sys import path
path.append("../")
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QGraphicsPixmapItem
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QPointF
from PyQt5.QtGui import QPixmap
# para que funcione la importacion src.....

# CLASES CREADAS PARA EL USO DE MVC
from src.models.Persona import Persona
from src.controlladores.userController import Account

#INTERFACES
from src.views.intefaz_admin import  SeccionAdministrador
from src.views.interfaz_usuario import SeccionUsuario
from src.views.registro import Registro





class Principal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        archivo = os.getcwd().split('src')[0] + r'\src\views\ui\ingresoRegistro.ui'
        self.logg = uic.loadUi(archivo, self)
        #self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)

        # ajusta el ancho y largo de la pantalla
        self.setGeometry(QRect(50, 50, 1000, 600))
        # carga la imagen de fondo
        pixmap = QPixmap(r'{0}\src\views\ui\img\paginicial.png'.format(os.getcwd().split("src")[0]))
        self.imgfondo.setPixmap(pixmap)

        # botones
        # nombre boton iniciar secion -> btn_login
        self.btn_login.clicked.connect(self.login)
        # nombre boton cerrar ventana -> btn_close
        self.btn_close.clicked.connect(self.cerrarVentana)
        # nombre boton registro  -> btn_registro
        self.btn_registro.clicked.connect(self.registrarse)

        # pantallas
        self.view_registro = Registro()

    def cerrarVentana(self):
        self.close()

    def login(self):
        # email
        mail = self.email.text()
        # password
        password = self.password.text()



        if mail != '' or password != '':
            # objeto persona
            usr = Persona('', mail, '', '', password)
            # validacion
            logg = Account(usr)
            isValid = logg.login()[0]


            if isValid:
                # validacion de rol
                self.logg.hide()
                rol = logg.login()[1][0][5]
                data_transferir = logg.login()[1][0]
                # si es usuario pasara
                if rol == 1:
                    self.view_usuario = SeccionUsuario(data_transferir)
                    self.view_usuario.show()
                    self.hide()
                # si es usuario administrador
                elif rol == 2:
                    self.view_admin = SeccionAdministrador()
                    self.view_admin.show()
                    self.hide()
            else:
                self.message.setText(logg.login()[1])
        else:
            print('campos vacios')
            self.message.setText('los campos deben estar llenos')

    def registrarse(self):
        #self.hide()
        self.view_registro.show()

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    principal = Principal()
    principal.show()
    app.exec_()

