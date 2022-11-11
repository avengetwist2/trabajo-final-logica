class Reserva:
    def __init__(self, sala, asiento,horario, persona):
        self.__horario = horario
        self.__sala = sala
        self.__asiento = asiento
        self.__persona = persona

    def getHorario(self):
        return self.__horario
    def getSala(self):
        return self.__sala
    def getAsiento(self):
        return self.__asiento

    def getPersona(self):
        return self.__persona


