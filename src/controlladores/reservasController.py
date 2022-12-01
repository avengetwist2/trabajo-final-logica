from sys import path
path.append("../../")
from src.config.conexion import Conexion

class ReservasController:
    def __init__(self, Obj_reserva=None)-> None:
        self.Obj_reserva = Obj_reserva

    def getReservasBy_Sala_Horario_Pelicula(self, id):
        try:
            conn = Conexion()
            query = "SELECT personas.nombre, personas.correo, personas.telefono, reservas.* FROM reservas, personas WHERE personas.id = reservas.id_persona AND sala = {0} AND horario ={1} AND reservas.id_pelicula = {2} ".format(self.Obj_reserva.getSala(), self.Obj_reserva.getHorario(), id)
            usuario = conn.run_query(query)
            if usuario != None:
                return usuario.fetchall()

        except Exception as ex:
            print('error en controlador de reserva',ex)
            return  ex

    def crearReservas_Sala_Horario_Peliculas(self):
        try:
            conn = Conexion()
            comprobacion = "SELECT * FROM reservas  WHERE sala = {0} AND asiento = '{1}' AND horario = {2} AND id_persona = {3} AND id_pelicula = {4} ".format(
                self.Obj_reserva.getSala(), self.Obj_reserva.getAsiento(), self.Obj_reserva.getHorario(),
                self.Obj_reserva.getIdPersona(), self.Obj_reserva.getPelicula())
            comp = conn.run_query(comprobacion)

            data = comp.fetchall()
            print(len(data))

            if len(data) == 0:
                query = "INSERT INTO reservas (sala, asiento, horario, id_persona, id_pelicula) VALUES({0}, '{1}', '{2}', {3}, {4})".format(self.Obj_reserva.getSala(), self.Obj_reserva.getAsiento(), self.Obj_reserva.getHorario(), self.Obj_reserva.getIdPersona(), self.Obj_reserva.getPelicula())
                reserva = conn.run_query(query)

                return reserva

        except Exception as ex:
            print('error en controlador de reserva',ex)
            return  ex

    def borrarReservas_Sala_Horario_Peliculas(self):
        try:
            conn = Conexion()

            query = "DELETE FROM reservas  WHERE sala = {0} AND asiento = '{1}' AND horario = {2} AND id_persona = {3} AND id_pelicula = {4} ".format(self.Obj_reserva.getSala(), self.Obj_reserva.getAsiento(), self.Obj_reserva.getHorario(), self.Obj_reserva.getIdPersona(), self.Obj_reserva.getPelicula())
            reserva = conn.run_query(query)

            return reserva

        except Exception as ex:
            print('error en controlador de reserva',ex)
            return  ex

    def getReservasByPersonaId(self, id):
        try:
            conn = Conexion()
            tomar_reservas = "SELECT peliculas.nombre, peliculas.genero, reservas.asiento, salas_cine.nombre, horarios.nombre FROM reservas, peliculas, salas_cine, horarios WHERE horarios.id = reservas.horario AND salas_cine.id = reservas.sala AND peliculas.id = reservas.id_pelicula AND id_persona = {0}".format(id)
            comp = conn.run_query(tomar_reservas)

            data = comp.fetchall()

            return data

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
print(query.getReservasByPersonaId(1))

"""