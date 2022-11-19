class Pelicula:

    def __init__(self,duracion, nombre, actor, genero, idioma):
        self.__duracion__ = duracion
        self.__nombre__ = nombre
        self.__actor__ = actor
        self.__genero__ = genero
        self.__idioma__ = idioma


    def getDuracion(self):
         return self.__duracion__

    def getNombre(self):
        return self.__nombre__

    def getActor(self):
        return self.__actor__

    def getgenero(self):
        return self.__genero__

    def getIdioma(self):
        return self.__idioma__

