class DetalleCompra():
    def __init__(self, id_detalle_compra, id_compra, cantidad, id_producto, subtotal, fecha_caducidad):
        self.id_detalle_compra = id_detalle_compra
        self.id_compra = id_compra
        self._cantidad = cantidad
        self.id_producto = id_producto
        self._subtotal = subtotal
        self._fecha_caducidad = fecha_caducidad