class DetalleVenta():
    def __init__(self, id_detalle_ventas, id_venta, cantidad, id_producto, subtotal):
        self.id_detalle_ventas = id_detalle_ventas
        self.id_venta = id_venta
        self._cantidad = cantidad
        self.id_producto = id_producto
        self._subtotal = subtotal

class registro_detalle_ventas():
    def __init__(self):
        self.diccionario_detalle_ventas = {}