class Compra():
    def __init__(self, id_compra, fecha_ingreso, id_empleado, nit, total):
        self.id_compra = id_compra
        self._fecha_ingreso = fecha_ingreso
        self.id_empleado = id_empleado
        self.nit = nit
        self._total = total

class registro_compras():
    def __init__(self):
        self.diccionario_compras = {}