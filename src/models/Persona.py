

class Persona:

    def __init__(self, nombre, correo, telefono, rol, password):
        self.nombre=nombre
        self.correo=correo
        self.telefono=telefono
        self.rol=rol
        self.password=password
@
    def __str__(self):
        return [self.nombre, self.correo, self.telefono, self.rol]