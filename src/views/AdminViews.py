import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog
from PyQt5 import uic
from PyQt5.QtCore import Qt, QPoint
# CLASES CREADAS PARA EL USO DE MVC
from src.models.Persona import Persona
from src.controlladores.userController import Account



class Principal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.logg = uic.loadUi("login.ui", self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)

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






# ESTA SECCION ES LA PANTALLA PRINCIPAL DEL USUARIO
class SeccionUsuario(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("usuario.ui", self)


# ESTA SECCION ES LA PANTALLA PRINCIPAL DEL USUARIO ADMINISTRADOR
class SeccionAdministrador(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("admin.ui", self)





app = QApplication(sys.argv)
principal = Principal()
principal.show()
app.exec_()