from src.config.conexion import Conexion

class ReservasController:
    def __init__(self, Obj_reserva)-> None:
        self.Obj_reserva = Obj_reserva

    def getReservasBy_Sala_Horario_Pelicula(self, id):
        try:
            conn = Conexion()
            query = "SELECT personas.nombre, personas.correo, personas.telefono, reservas.* FROM reservas, personas WHERE personas.id = reservas.id_persona AND sala = {0} AND horario ='{1}' AND reservas.id_pelicula = {2} ".format(self.Obj_reserva.getSala(), self.Obj_reserva.getHorario(), id)
            usuario = conn.run_query(query)
            if usuario != None:
                return usuario.fetchall()

        except Exception as ex:
            print('error en controlador de reserva',ex)
            return  ex

    def crearReservas_Sala_Horario_Peliculas(self, id):
        try:
            conn = Conexion()
            query = "INSERT INTO reservas (sala, asiento, horario, id_persona) VALUES({0}, '{1}', '{2}', {3}, {4})".format(self.Obj_reserva.getSala(), self.Obj_reserva.getAsiento(), self.Obj_reserva.getHorario(), self.Obj_reserva.getIdPersona(), id)
            reserva = conn.run_query(query)

            return reserva

        except Exception as ex:
            print('error en controlador de reserva',ex)
            return  ex












"""   
class test:
    def __init__(self):
        self.sala = 1
        self.asiento = "A4"
        self.hoario = "10AM"
        self.idPersona = 2

    def getSala(self):
        return self.sala
    def getAsiento(self):
        return self.asiento
    def getHorario(self):
        return self.hoario
    def getIdPersona(self):
        return self.idPersona

te = test()

query = ReservasController(te)
print(query.getReservasBy_Sala_Horario_Pelicula(1))

"""