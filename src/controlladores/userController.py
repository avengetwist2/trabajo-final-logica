from src.config.conexion import Conexion

class Account:
    def __init__(self, Obj_usuario)-> None:
        self.Obj_usuario=Obj_usuario

    def login(self):
        try:
            conn = Conexion()
            query = " SELECT * FROM personas WHERE correo = '{0}' ".format(self.Obj_usuario.getCorreo())
            usuario = conn.run_query(query)
            data = usuario.fetchall()
            #print(data)
            #print(len(data))
            if len(data) > 0:
                #print('paso el primer filtro')
                #print(data)
                if data[0][4] == self.Obj_usuario.getPassword():
                    return [True, data]
                else:
                    return [False, 'contraseña incorrecta']
            else:
                return [False, 'usuario no existe']

        except Exception as ex:
            print(ex)

    def register(self):
        try:
            conn = Conexion()
            query = "INSERT INTO personas(nombre, correo, telefono, password, rol) VALUES('{0}', '{1}', '{2}', '{3}', {4})"\
                .format(self.Obj_usuario.getNombre(),self.Obj_usuario.getCorreo(),self.Obj_usuario.getTelefono(),self.Obj_usuario.getPassword(),self.Obj_usuario.getRol())
            usuario = conn.run_query(query)
            #print(usuario)
            return 'usuario creado'
        except Exception as ex:
            print(ex)








"""   
###### pruebas
class User():
    def __init__(self):
        self.nombre = 'prii'
        self.correo = 'prii@gmail.com'
        self.telefono = '3126815066'
        self.password = '123'
        self.rol = 2
    def getNombre(self):
        return self.nombre
    def getCorreo(self):
        return self.correo
    def getTelefono(self):
        return self.telefono
    def getPassword(self):
        return self.password
    def getRol(self):
        return self.rol

usuario = User()

cuenta = Account(usuario)
retorno = cuenta.login()
print(retorno)


"""
