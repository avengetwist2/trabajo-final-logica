class Pelicula:
    def _init_(self,duracion, nombre, actor, genero, idioma):
        self.duracion = duracion
        self.nombre = nombre
        self.actor = actor
        self.genero = genero
        self.idioma = idioma
    def _str_(self):
        return (self.duracion, self.nombre, self.genero, self.idioma)
        duracion(self.duracion)
        nombre(self.nombre)
        genero(self.genero)
        idioma(self.idioma)