
#from src.controlladores.reservasController import ReservasController

class ReservaModel:
    def __init__(self, horario, sala, asiento=None, persona=None):
        self.__horario__ = horario
        self.__sala__ = sala
        self.__asiento__ = asiento
    def getHorario(self):
        return self.__horario__
    def getSala(self):
        return self.__sala__
    def getAsiento(self):
        return self.__asiento__


"""
#crear objeto de reserva para poder hacer la busqueda
objeto_Reserva = ReservaModel('10AM',1)
#creamos un objeto del controlador de reservas  y le pasamos un modelo de datos de reservas
asientos_ocupados = ReservasController(objeto_Reserva)
print(asientos_ocupados.getReservasBySalaAndHorario())
"""