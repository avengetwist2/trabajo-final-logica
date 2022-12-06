import sys
import os
from sys import path
path.append("../../")
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QGraphicsPixmapItem, QListWidgetItem
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QPointF
from PyQt5.QtGui import QPixmap
# VISOR Y GENERADOR DE PDF
import webbrowser
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# IMPORTACION DE MODELOS Y CONTROLADORES
from src.controlladores.reservasController import ReservasController

# ESTA SECCION ES LA PANTALLA PRINCIPAL DEL USUARIO ADMINISTRADOR
class Reservas_realizadas(QDialog):
    def __init__(self, data_transferida=None):
        QDialog.__init__(self)
        #aqui se colocara el id de cada serserva cuando se seleccione en la lista
        self.id_reserva=None
        archivo = os.getcwd().split('src')[0] + r'\src\views\ui\reservas_realizadas.ui'
        uic.loadUi(archivo, self)
        self.data_transferida = data_transferida

        self.datos_reservas = ReservasController()

        id = data_transferida[0]
        reservas_data = self.datos_reservas.getReservasByPersonaId(id)

        for i in reservas_data:
            listWidgetItem = QListWidgetItem(str(f" {i[0]} - {i[1]} - {i[2]} - {i[3]} - {i[5]}"))
            self.list_reservas.addItem(listWidgetItem)

        self.list_reservas.itemSelectionChanged.connect(self.itemChanged)
        #self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)

        # ajusta el ancho y largo de la pantalla
        self.setGeometry(QRect(50, 50, 1000, 600))
        # carga la imagen de fondo
        pixmap = QPixmap(r'{0}\src\views\ui\img\img_reserva.png'.format(os.getcwd().split("src")[0]))
        self.imgfondo.setPixmap(pixmap)

        #print(self.list_reservas.get)

        # BOTONES
        self.btn_actualizar.clicked.connect(self.actualizar)
        self.btn_close.clicked.connect(self.cerrar)
        self.btn_regresar.clicked.connect(self.regresar)
        self.btn_cancelar.clicked.connect(self.cancelar_reserva)
        self.btn_imprimir.clicked.connect(self.imprimir_reserva)
        self.btn_actualizar.clicked.connect(self.repintar_tabla)


    def imprimir_reserva(self):
        # DATOS PARA GENERAR EL PDF
        if(self.id_reserva != None):
            #print(self.id_reserva)
            data = self.datos_reservas.getReservasColillasPago(self.id_reserva)[0]
            #print(data)
            nombre = str(data[0]) + ' - ' + str(data[9]) + ' - ' + str(data[11])
            # AQUI SE GENERA UN PDF TENIENDO EN CUENTA LA RESERVA SELECCIONADA
            w, h = A4
            c = canvas.Canvas(r"{0}\src\files\{1}.pdf".format(os.getcwd().split("src")[0], nombre), pagesize=A4)
            c.drawString(30, h - 50, "TIKET DE RESERVA")
            x = 120
            y = h - 45
            c.line(x, y, x + 100, y)

            c.drawString(30, h - 100, "Cliente :")
            c.drawString(130, h - 100, data[0])

            c.drawString(30, h - 120, "Correo :")
            c.drawString(130, h - 120, data[1])

            c.drawString(30, h - 140, "Celular :")
            c.drawString(130, h - 140, data[2])

            #c.drawString(30, h - 160, "nose :")
            #c.drawString(130, h - 160, str(data[3]))

            c.drawString(30, h - 180, "Pelicula :")
            c.drawString(130, h - 180, data[4])

            c.drawString(30, h - 200, "Genero :")
            c.drawString(130, h - 200, data[5])

            c.drawString(30, h - 220, "Idioma :")
            c.drawString(130, h - 220, data[6])

            c.drawString(30, h - 240, "Actor :")
            c.drawString(130, h - 240, data[7])

            #c.drawString(30, h - 300, "nose :")
            #c.drawString(130, h - 300, str(data[8]))

            c.drawString(30, h - 280, "Silla :")
            c.drawString(130, h - 280, data[9])

            c.drawString(30, h - 300, "Sala :")
            c.drawString(130, h - 300, data[10])

            c.drawString(30, h - 320, "Horario :")
            c.drawString(130, h - 320, data[11])

            c.drawString(30, h - 360, "Total a Pagar :")
            c.drawString(130, h - 360, str(data[12]))

            c.showPage()
            c.save()



            # ESTAS LINEAS DE CODIGO ABRE EL PDF GENERADO
            path = r"{0}\src\files\{1}.pdf".format(os.getcwd().split("src")[0], nombre)
            webbrowser.open_new(path)

        else:
            self.message.setText('Selecciona un Item')



    def cancelar_reserva(self):
        if(self.id_reserva != None):
            self.datos_reservas.borrarReserva(self.id_reserva)
            self.repintar_tabla()


    def repintar_tabla(self):
        # Borra la tabla
        self.list_reservas.clear()
        # los datos se vuelven a pintar
        id = self.data_transferida[0]
        reservas_data = self.datos_reservas.getReservasByPersonaId(id)

        for i in reservas_data:
            listWidgetItem = QListWidgetItem(str(f" {i[0]} - {i[1]} - {i[2]} - {i[3]} - {i[5]}"))
            self.list_reservas.addItem(listWidgetItem)

    def itemChanged(self):
        item = QListWidgetItem(self.list_reservas.currentItem())
        print(item.text().split('-')[4])
        self.id_reserva = item.text().split('-')[4]

    def regresar(self):
        self.hide()
    def cerrar(self):
        exit()

    def actualizar(self):
        print(self.data_transferida)
