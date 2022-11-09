

class Persona:
    def __init__(self, nombre, correo, telefono, rol, password):
        self.__nombre=nombre
        self.correo=correo
        self.telefono=telefono
        self.rol=rol
        self.password=password

    # aqui van los metodos de acceso a los atributos
    def getNombre(self):
        return self.__nombre


    # aqui van los metodos para cambiar el valor de los atributos
    def setNombre(self, nombre):
        self.__nombre = nombre


    def __toString__(self):
        return f"""
        nombre = {self.__nombre}
        correo = {self.correo}
        password = {self.password}
        """







"""
tomarNombre = Persona("brayan","brayan@gmail.com","3124567", "admin", "123")
print(tomarNombre.getNombre())
tomarNombre.setNombre('juan')
print(tomarNombre.getNombre())

"""







