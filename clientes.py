class Cliente():
    def __init__(self, nit, nombre, direccion, telefono, correo):
        self.nit = nit
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono
        self._correo = correo

class registro_clientes():
    def __init__(self):
        self.diccionario_clientes = {}