class detalle_compras():
    def __init__(self, id_detalle_compra, id_venta, cantidad, id_producto, subtotal, fecha_caducidad):
        self.id_detalle_compra = id_detalle_compra
        self.id_venta = id_venta
        self.cantidad = cantidad
        self.id_producto = id_producto
        self.subtotal = subtotal
        self.fecha_caducidad = fecha_caducidad