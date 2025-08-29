class Proveedor():
    def __init__(self, nit, nombre, direccion, telefono, correo, empresa):
        self.nit = nit
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono
        self._correo = correo
        self._empresa = empresa

class registro_proveedores():
    def __init__(self):
        self.diccionario_proveedores = {}