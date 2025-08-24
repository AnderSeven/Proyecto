class Venta():
    def __init__(self, id_venta, fecha, id_empleado, nit, total):
        self.id_venta = id_venta
        self._fecha = fecha
        self.id_empleado = id_empleado
        self.nit = nit
        self._total = total