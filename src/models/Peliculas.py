class Pelicula:
    def __init__(self,duracion, nombre, actor, genero, idioma):
        self.__duracion = duracion
        self.__nombre = nombre
        self.__actor = actor
        self.__genero = genero
        self.__idioma = idioma


    def getDuracion(self):
         return self.__duracion

    def getNombre(self):
        return self.__nombre

    def getActor(self):
        return self.__actor

    def getgenero(self):
        return self.__genero

    def getIdioma(self):
        return self.__idioma

