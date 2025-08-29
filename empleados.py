class Empleado():
    def __init__(self, id_empleado, nombre, direccion, telefono, correo, puesto):
        self.id_empleado = id_empleado
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono
        self._correo = correo
        self._puesto = puesto

class registro_empleados():
    def __init__(self):
        self.diccionario_empleados = {}