class detalle_ventas():
    def __init__(self, id_detalle_ventas, id_venta, cantidad, id_producto, subtotal, stock):
        self.id_detalle_ventas = id_detalle_ventas
        self.id_venta = id_venta
        self.cantidad = cantidad
        self.id_producto = id_producto
        self.subtotal = subtotal
        self.stock = stock