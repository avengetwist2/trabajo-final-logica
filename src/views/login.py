from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtGui import QPixmap

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from sys import path
path.append("../../")

from src.models.Persona import Persona
from src.controlladores.userController import Account



""" 
class AnotherWindow(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(557, 487)
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(90, 140, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Frame)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 270, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.pushButton.setText(_translate("Frame", "PushButton"))
        self.pushButton_2.setText(_translate("Frame", "PushButton"))
   
    def __init__(self):
        super().__init__()

        #layout = QVBoxLayout()
        layout1 = QtWidgets.QFrame() #QVBoxLayout()
        self.widget = QtWidgets.QWidget()
        self.widget.setGeometry(QtCore.QRect(0, 0, 370, 480))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 370, 480))
        self.label.setText('holaaaaaaaaaaaaaaaaaaaaaaaa')

        pixmap = QPixmap('background.png')
        self.label.setPixmap(pixmap)

        #layout.addWidget(self.label)
        #layout.addWidget(self.widget)

        #self.setLayout(layout)
        """











class Ui_Form(object):

    #def __init__(self):
        #self.w = AnotherWindow()
        #pass

    def cerrarVentana(self, form):
        form.close()

    def funcionLogin(self):
        #email
        mail = self.lineEdit.text()
        #password
        password = self.lineEdit_2.text()
        #objeto persona
        usr = Persona('', mail,'','',password)
        #validacion
        logg = Account(usr)
        isValid = logg.login()[0]
        print(isValid)
        print(logg.login()[1])







    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(359, 467)
        Form.setWindowFlag(Form.windowType().FramelessWindowHint, True)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 370, 480))
        self.widget.setStyleSheet("QPushButton#pushButton{    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#pushButton:hover{    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#pushButton:pressed{    \n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(105, 118, 132, 200);\n"
"}\n"
"\n"
"QPushButton#pushButton_2, #pushButton_3, #pushButton_4, #pushButton_5{    \n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color:rgba(85, 98, 112, 255);\n"
"}\n"
"QPushButton#pushButton_2:hover, #pushButton_3:hover, #pushButton_4:hover, #pushButton_5:hover{    \n"
"    color:rgba(155, 168, 182, 220);\n"
"}\n"
"QPushButton#pushButton_2:pressed, #pushButton_3:pressed, #pushButton_4:pressed, #pushButton_5:pressed{    \n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    color:rgba(115, 128, 142, 255);\n"
"}")

        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 370, 480))

        pixmap = QPixmap('background.png')
        self.label.setPixmap(pixmap)
        #self.label.setStyleSheet("border-image: url(:/images/background.png);\n"
#"border-radius:20px;")


        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(0, -10, 381, 481))
        self.label_2.setStyleSheet("border-image: url(:/archivo/background.png);\n"
"border-radius: 20px;")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/archivo/background.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(40, 60, 280, 390))
        self.label_3.setStyleSheet("background-color:rgba(0, 0, 0, 100);\n"
"border-radius:15px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(135, 95, 90, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(255, 255, 255, 210);")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 165, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 230, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(80, 310, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.funcionLogin)


        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(100, 370, 191, 21))
        self.label_5.setStyleSheet("color:rgba(255, 255, 255, 140);")
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(294, 30, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color:rgb(255, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: self.cerrarVentana(Form)) #.connect(self.cerrarVentana)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Log In"))
        self.lineEdit.setPlaceholderText(_translate("Form", "  Email"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "  Password"))
        self.pushButton.setText(_translate("Form", "L o g  I n"))
        self.label_5.setText(_translate("Form", "Registrar usuario o administrador"))
        self.pushButton_2.setText(_translate("Form", "X"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
