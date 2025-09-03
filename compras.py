from datetime import date
from detalle_compras import DetalleCompra
class Compra():
    def __init__(self, id_compra, fecha_ingreso, id_empleado, nit, total):
        self.id_compra = id_compra
        self._fecha_ingreso = fecha_ingreso
        self.id_empleado = id_empleado
        self.nit = nit
        self._total = total
class quick_sorts_compras():
    def quick_sort_id(self, lista):
        if len(lista) <= 1: return lista
        pivote = lista[0]
        menores = [x for x in lista[1:] if x.id_compra < pivote.id_compra]
        iguales = [x for x in lista if x.id_compra == pivote.id_compra]
        mayores = [x for x in lista[1:] if x.id_compra > pivote.id_compra]
        return self.quick_sort_id(menores) + iguales + self.quick_sort_id(mayores)

    def quick_sort_total(self, lista):
        if len(lista) <= 1: return lista
        pivote = lista[0]
        menores = [x for x in lista[1:] if x._total < pivote._total]
        iguales = [x for x in lista if x._total == pivote._total]
        mayores = [x for x in lista[1:] if x._total > pivote._total]
        return self.quick_sort_total(menores) + iguales + self.quick_sort_total(mayores)
class registro_compras():
    def __init__(self):
        self.diccionario_compras = {}
        self.cargar_compras()
        self.sorter = quick_sorts_compras()

    def obtener_siguiente_id(self):
        if not self.diccionario_compras:
            return 1
        return max(self.diccionario_compras.keys()) + 1

    def registrar_compras(self, registro_empleados, registro_proveedores, registro_productos, registro_dc):
        id_compra = self.obtener_siguiente_id()
        print(f"Iniciando nueva compra con ID: {id_compra}")

        s = False
        while s == False:
            try:
                id_empleado = int(input("Ingrese su ID de empleado (admin): "))
                if id_empleado in registro_empleados.diccionario_empleados:
                    s = True
                else:
                    print("Error, el empleado no existe")
            except Exception as ex:
                print(f"Ha ocurrido un error: {ex}")
        
        s = False
        while s == False:
            try:
                nit_proveedor = int(input("Ingrese el NIT del proveedor: "))
                if nit_proveedor in registro_proveedores.diccionario_proveedores:
                    s = True
                else:
                    print("Error, el proveedor no existe")
            except Exception as ex:
                print(f"Ha ocurrido un error: {ex}")

        total_compra = 0.0
        id_detalle_actual = registro_dc.obtener_siguiente_id()
        print("--- Ingrese los productos de la compra ---")
        while True:
            try:
                id_producto = int(input("Ingrese el ID del producto (o 0 para finalizar): "))
                if id_producto == 0:
                    break
                
                if id_producto in registro_productos.diccionario_productos:
                    producto_obj = registro_productos.diccionario_productos[id_producto]
                    cantidad_comprada = int(input(f"Ingrese la cantidad comprada de '{producto_obj._nombre}': "))
                    costo_unitario = float(input(f"Ingrese el costo por unidad de '{producto_obj._nombre}': "))

                    if cantidad_comprada > 0 and costo_unitario >= 0:
                        producto_obj._stock += cantidad_comprada
                        subtotal = costo_unitario * cantidad_comprada
                        total_compra += subtotal
                        
                        detalle = DetalleCompra(id_detalle_actual, id_compra, cantidad_comprada, id_producto, subtotal)
                        registro_dc.diccionario_detalle_compra[id_detalle_actual] = detalle
                        id_detalle_actual += 1
                        print(f"'{producto_obj._nombre}' x{cantidad_comprada} agregado a la compra.")
                    else:
                        print("La cantidad y el costo deben ser positivos.")
                else:
                    print("Error, producto no encontrado")
            except Exception as ex:
                print(f"Ha ocurrido un error: {ex}")

        fecha_actual = date.today().isoformat()
        nueva_compra = Compra(id_compra, fecha_actual, id_empleado, nit_proveedor, total_compra)
        self.diccionario_compras[id_compra] = nueva_compra
        print(f"\nCompra #{id_compra} registrada con exito. Total: Q{total_compra:.2f}")

        registro_productos.guardar_productos()
        registro_dc.guardar_detalles()
        self.guardar_compras()
        print("Datos de compras y productos guardados en el archivo")

    def guardar_compras(self):
        try:
            with open("compras.txt", "w") as archivo:
                for compra in self.diccionario_compras.values():
                    linea = f"{compra.id_compra}:{compra._fecha_ingreso}:{compra.id_empleado}:{compra.nit}:{compra._total}\n"
                    archivo.write(linea)
        except Exception as ex:
            print(f"Ha ocurrido un error al guardar compras: {ex}")

    def cargar_compras(self):
        try:
            with open("compras.txt", "r") as archivo:
                for linea in archivo.readlines():
                    if linea.strip():
                        (id_compra_str, fecha, id_emp_str, nit_str, total_str) = linea.strip().split(":")
                        self.diccionario_compras[int(id_compra_str)] = Compra(int(id_compra_str), fecha, int(id_emp_str), int(nit_str), float(total_str))
            print("Compras cargadas desde compras.txt")
        except FileNotFoundError:
            print("No se encontro el archivo compras.txt, se creara uno nuevo al guardar")
        except Exception as ex:
            print(f"Ha ocurrido un error al cargar compras: {ex}")

    def mostrar_compras(self):
        print("\n---Compras---")
        if not self.diccionario_compras:
            print("No hay compras registradas.")
        else:
            lista_compras = list(self.diccionario_compras.values())
            print("Como desea ordenar la lista?")
            print("1. Por ID de Compra (menor a mayor)")
            print("2. Por Total (menor a mayor)")
            try:
                opcion = int(input("Elija una opcion: "))
                match opcion:
                    case 1:
                        lista_ordenada = self.sorter.quick_sort_id(lista_compras)
                    case 2:
                        lista_ordenada = self.sorter.quick_sort_total(lista_compras)
                    case _:
                        print("Opcion invalida, se mostrara sin ordenar")
                        lista_ordenada = lista_compras
                for compra in lista_ordenada:
                    print(f"ID Compra: {compra.id_compra} | Fecha: {compra._fecha_ingreso} | Empleado ID: {compra.id_empleado} | Proveedor NIT: {compra.nit} | Total: Q{compra._total:.2f}")
            except Exception as ex:
                print(f"Ha ocurrido un error: {ex}")

    def modificar_compra(self, registro_productos, registro_dc):
        print("\n---Anular Compra---")
        if not self.diccionario_compras:
            print("No hay compras para anular.")
        else:
            s = False
            while s == False:
                try:
                    id_compra = int(input("Ingrese el ID de la compra que desea anular: "))
                    if id_compra in self.diccionario_compras:
                        s = True
                    else:
                        print("Error, la compra no existe, intente de nuevo")
                except Exception as ex:
                    print(f"Ha ocurrido un error: {ex}")
            
            compra_a_anular = self.diccionario_compras[id_compra]
            
            if compra_a_anular._total > 0:
                print(f"Anulando Compra #{id_compra}. Total original: Q{compra_a_anular._total:.2f}")
                
                for detalle in registro_dc.diccionario_detalle_compra.values():
                    if detalle.id_compra == id_compra:
                        producto_obj = registro_productos.diccionario_productos.get(detalle.id_producto)
                        if producto_obj and producto_obj._stock >= detalle._cantidad:
                            producto_obj._stock -= detalle._cantidad
                            print(f"Restadas {detalle._cantidad} unidades del stock de '{producto_obj._nombre}'")
                
                compra_a_anular._total = 0.0
                self.guardar_compras()
                registro_productos.guardar_productos()
                print("Compra anulada con exito. El stock ha sido actualizado.")
            else:
                print("Esta compra ya ha sido anulada.")