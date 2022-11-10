

class Persona:
    def __init__(self, nombre, correo, telefono, rol, password):
        self.__nombre=nombre
        self.__correo=correo
        self.__telefono=telefono
        self.__rol=rol
        self.__password=password

    # aqui van los metodos de acceso a los atributos
    def getNombre(self):
        return self.__nombre
    def getCorreo(self):
        return self.__correo
    def getTelefono(self):
        return self.__telefono
    def getRol(self):
        return self.__rol
    def getPassword(self):
        return self.__password















