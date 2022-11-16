from src.config.conexion import Conexion

class PeliculasController:
    def __init__(self, Obj_pelicula)-> None:
        self.Obj_pelicula = Obj_pelicula

    def getPeliculas(self):
        try:
            conn = Conexion()
            query = "SELECT * FROM peliculas"
            usuario = conn.run_query(query)
            return usuario.fetchall()

        except Exception as ex:
            print('error en controlador de Peliculas',ex)
            return  ex

    def crearPeliculas(self):
        try:
            conn = Conexion()
            query = "INSERT INTO peliculas (nombre, genero, idioma, actor, duracion) VALUES('{0}', '{1}', '{2}', '{3}', {4})".format(self.Obj_reserva.getNombre(), self.Obj_reserva.getgenero(), self.Obj_reserva.getIdioma(), self.Obj_reserva.getActor(), self.Obj_reserva.getDuracion())
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