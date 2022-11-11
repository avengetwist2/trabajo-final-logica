from src.config.conexion import Conexion

class ReservasController:
    def __init__(self, Obj_reserva)-> None:
        self.Obj_reserva=Obj_reserva

    def getReservasBySalaAndHorario(self):
        try:
            conn = Conexion()
            query = "SELECT personas.nombre, personas.correo, personas.telefono, reservas.* FROM reservas, personas WHERE personas.id = reservas.id_persona AND sala = {0} AND horario ='{1}' ".format(self.Obj_reserva.getSala(), self.Obj_reserva.getHorario())
            usuario = conn.run_query(query)
            if usuario != None:
                return usuario.fetchall()

        except Exception as ex:
            print('error en controlador de reserva',ex)
            return  ex


"""   
class test:
    def __init__(self):
        self.sala = 1
        self.reserva = "10AM"
    def getSala(self):
        return self.sala
    def getHorario(self):
        return self.reserva

te = test()

query = ReservasController(te)
print(query.getReservasBySalaAndHorario())

"""