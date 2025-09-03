from empleados import Empleado
class Admin(Empleado):
    def __init__(self, id_empleado, nombre, direccion, telefono, correo):
        Empleado.__init__(self, id_empleado, nombre, direccion, telefono, correo, puesto = "Admin")