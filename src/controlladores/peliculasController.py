from src.config.conexion import Conexion

class PeliculasController:
    def getPeliculas(self):
        try:
            conn = Conexion()
            query = "SELECT * FROM peliculas"
            usuario = conn.run_query(query)
            return usuario.fetchall()

        except Exception as ex:
            print('error en controlador de Peliculas',ex)
            return  ex

    def crearPeliculas(self, Obj_pelicula):
        try:
            conn = Conexion()
            query = "INSERT INTO peliculas (nombre, genero, idioma, actor, duracion) VALUES('{0}', '{1}', '{2}', '{3}', {4})".format(Obj_reserva.getNombre(), Obj_reserva.getgenero(), Obj_reserva.getIdioma(), Obj_reserva.getActor(), Obj_reserva.getDuracion())
            reserva = conn.run_query(query)
            return reserva

        except Exception as ex:
            print('error en controlador de reserva',ex)
            return  ex

    def borrarPeliculas(self, id):
        try:
            conn = Conexion()
            query = "DELETE FROM peliculas WHERE id = {0}".format(id)
            reserva = conn.run_query(query)
            return reserva

        except Exception as ex:
            print('error en controlador de reserva', ex)
            return ex

    def getSalas(self):
        try:
            conn = Conexion()
            query = "SELECT * FROM salas_cine "
            reserva = conn.run_query(query)
            return reserva

        except Exception as ex:
            print('error en controlador de reserva', ex)
            return ex

    def getHorarios(self):
        try:
            conn = Conexion()
            query = "SELECT * FROM horarios "
            reserva = conn.run_query(query)
            return reserva

        except Exception as ex:
            print('error en controlador de reserva', ex)
            return ex