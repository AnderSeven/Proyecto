class DetalleCompra():
    def __init__(self, id_detalle_compra, id_compra, cantidad, id_producto, subtotal):
        self.id_detalle_compra = id_detalle_compra
        self.id_compra = id_compra
        self._cantidad = cantidad
        self.id_producto = id_producto
        self._subtotal = subtotal

class registro_detalle_compra():
    def __init__(self):
        self.diccionario_detalle_compra = {}
        self.cargar_detalles()

    def obtener_siguiente_id(self):
        if not self.diccionario_detalle_compra:
            return 1
        return max(self.diccionario_detalle_compra.keys()) + 1

    def guardar_detalles(self):
        try:
            with open("detalle_compras.txt", "w") as archivo:
                for detalle in self.diccionario_detalle_compra.values():
                    linea = f"{detalle.id_detalle_compra}:{detalle.id_compra}:{detalle._cantidad}:{detalle.id_producto}:{detalle._subtotal}\n"
                    archivo.write(linea)
        except Exception as ex:
            print(f"Ha ocurrido un error al guardar detalles de compra: {ex}")

    def cargar_detalles(self):
        try:
            with open("detalle_compras.txt", "r") as archivo:
                for linea in archivo.readlines():
                    if linea.strip():
                        (id_det_str, id_compra_str, cant_str, id_prod_str, sub_str) = linea.strip().split(":")
                        detalle = DetalleCompra(int(id_det_str), int(id_compra_str), int(cant_str), int(id_prod_str), float(sub_str))
                        self.diccionario_detalle_compra[detalle.id_detalle_compra] = detalle
            print("Detalles de compra cargados desde detalle_compras.txt")
        except FileNotFoundError:
            print("No se encontro el archivo detalle_compras.txt, se creara uno nuevo al guardar")
        except Exception as ex:
            print(f"Ha ocurrido un error al cargar detalles de compra: {ex}")