class DetalleCompra():
    def __init__(self, id_detalle_compra, id_compra, cantidad, id_producto, subtotal, fecha_caducidad):
        self.id_detalle_compra = id_detalle_compra
        self.id_compra = id_compra
        self.cantidad = cantidad
        self.id_producto = id_producto
        self.subtotal = subtotal
        self.fecha_caducidad = fecha_caducidad