class Producto():
    def __init__(self, id_producto, nombre, precio, id_categoria, total_compras, total_ventas, stock):
        self.id_producto = id_producto
        self.id_categoria = id_categoria
        self._nombre = nombre
        self._precio = precio
        self._total_compras = total_compras
        self._total_ventas = total_ventas
        self._stock = stock