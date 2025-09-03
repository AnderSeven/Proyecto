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
        self.cargar_detalles()

    def obtener_siguiente_id(self):
        if not self.diccionario_detalle_ventas:
            return 1
        return max(self.diccionario_detalle_ventas.keys()) + 1

    def guardar_detalles(self):
        try:
            with open("detalle_ventas.txt", "w") as archivo:
                for detalle in self.diccionario_detalle_ventas.values():
                    linea = f"{detalle.id_detalle_ventas}:{detalle.id_venta}:{detalle._cantidad}:{detalle.id_producto}:{detalle._subtotal}\n"
                    archivo.write(linea)
        except Exception as ex:
            print(f"Ha ocurrido un error al guardar detalles de venta: {ex}")

    def cargar_detalles(self):
        try:
            with open("detalle_ventas.txt", "r") as archivo:
                for linea in archivo.readlines():
                    if linea.strip():
                        (id_det_str, id_ven_str, cant_str, id_prod_str, sub_str) = linea.strip().split(":")
                        detalle = DetalleVenta(int(id_det_str), int(id_ven_str), int(cant_str), int(id_prod_str), float(sub_str))
                        self.diccionario_detalle_ventas[detalle.id_detalle_ventas] = detalle
            print("Detalles de venta cargados desde detalle_ventas.txt")
        except FileNotFoundError:
            print("No se encontro el archivo detalle_ventas.txt, se creara uno nuevo al guardar")
        except Exception as ex:
            print(f"Ha ocurrido un error al cargar detalles de venta: {ex}")