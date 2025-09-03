from datetime import date
from detalle_ventas import DetalleVenta
class Venta():
    def __init__(self, id_venta, fecha, id_empleado, nit, total):
        self.id_venta = id_venta
        self._fecha = fecha
        self.id_empleado = id_empleado
        self.nit = nit
        self._total = total

class quick_sorts_ventas():
    def quick_sort_id(self, lista):
        if len(lista) <= 1: return lista
        pivote = lista[0]
        menores = [x for x in lista[1:] if x.id_venta < pivote.id_venta]
        iguales = [x for x in lista if x.id_venta == pivote.id_venta]
        mayores = [x for x in lista[1:] if x.id_venta > pivote.id_venta]
        return self.quick_sort_id(menores) + iguales + self.quick_sort_id(mayores)

    def quick_sort_total(self, lista):
        if len(lista) <= 1: return lista
        pivote = lista[0]
        menores = [x for x in lista[1:] if x._total < pivote._total]
        iguales = [x for x in lista if x._total == pivote._total]
        mayores = [x for x in lista[1:] if x._total > pivote._total]
        return self.quick_sort_total(menores) + iguales + self.quick_sort_total(mayores)

class registro_ventas():
    def __init__(self):
        self.diccionario_ventas = {}
        self.cargar_ventas()
        self.sorter = quick_sorts_ventas()

    def obtener_siguiente_id(self):
        if not self.diccionario_ventas:
            return 1
        return max(self.diccionario_ventas.keys()) + 1

    def registrar_ventas(self, registro_empleados, registro_clientes, registro_productos, registro_dv):
        id_venta = self.obtener_siguiente_id()
        print(f"Iniciando nueva venta con ID: {id_venta}")
        s = False
        while s == False:
            id_empleado = int(input("Ingrese el id del empleado: "))
            if id_empleado in registro_empleados.diccionario_empleados:
                s = True
            else:
                print("Error, el empleado no existe")
        s = False
        while s == False:
            nit2 = input("Ingrese el nit del cliente (o 'cf' para Consumidor Final): ").strip().lower()
            if nit2 == "cf":
                nit = "C/F"
                s = True
            else:
                try:
                    nit = int(nit2)
                    if nit in registro_clientes.diccionario_clientes:
                        s = True
                    else:
                        print("Cliente no encontrado.")
                        registrar_nuevo = input("Desea registrarlo ahora? (s/n): ").strip().lower()
                        if registrar_nuevo == 's':
                            nombre = input("Ingrese el nombre del cliente: ").strip()
                            direccion = input("Ingrese la direccion del cliente: ").strip()
                            telefono = input("Ingrese el telefono del cliente: ").strip()
                            correo = input("Ingrese el correo del cliente: ").strip()
                            registro_clientes.registrar_un_solo_cliente(nit, nombre, direccion, telefono, correo)
                            s = True
                except Exception as ex:
                    print(f"Ha ocurrido un error: {ex}")

        total = 0.0
        id_detalle_actual = registro_dv.obtener_siguiente_id()
        print("---Ingrese los productos de la venta---")
        s = False
        while s == False:
            try:
                id_producto = int(input("Ingrese el id del producto (o cero para finalizar): "))
                if id_producto == 0:
                    s = True
                else:
                    if id_producto in registro_productos.diccionario_productos:
                        producto_obj = registro_productos.diccionario_productos[id_producto]
                        cantidad_a_vender = int(input(f"Ingrese la cantidad de '{producto_obj._nombre}': "))
                        
                        if cantidad_a_vender > 0 and cantidad_a_vender <= producto_obj._stock:
                            producto_obj._stock -= cantidad_a_vender
                            subtotal = producto_obj._precio * cantidad_a_vender
                            total += subtotal
                            
                            detalle = DetalleVenta(id_detalle_actual, id_venta, cantidad_a_vender, id_producto, subtotal)
                            registro_dv.diccionario_detalle_ventas[id_detalle_actual] = detalle
                            id_detalle_actual += 1

                            print(f"'{producto_obj._nombre}' x{cantidad_a_vender} agregado. Subtotal: Q{subtotal:.2f}")
                        else:
                            print(f"Cantidad invalida o no hay suficiente stock. Disponibles: {producto_obj._stock}")
                    else:
                        print("Error, producto no encontrado")
            except Exception as ex:
                print(f"Ha ocurrido un error: {ex}")
        fecha = date.today().isoformat()
        nueva_venta = Venta(id_venta, fecha, id_empleado, nit, total)
        self.diccionario_ventas[id_venta] = nueva_venta
        print(f"Venta #{id_venta} registrada con exito. Total: Q{total:.2f}")
        
        registro_productos.guardar_productos()
        registro_dv.guardar_detalles()
        self.guardar_ventas()
        print("Datos de ventas guardados en el archivo")

    def guardar_ventas(self):
        try:
            with open("ventas.txt", "w") as archivo:
                for venta in self.diccionario_ventas.values():
                    linea = f"{venta.id_venta}:{venta._fecha}:{venta.id_empleado}:{venta.nit}:{venta._total}\n"
                    archivo.write(linea)
        except Exception as ex:
            print(f"Ha ocurrido un error al guardar ventas: {ex}")

    def cargar_ventas(self):
        try:
            with open("ventas.txt", "r") as archivo:
                for linea in archivo.readlines():
                    if linea.strip():
                        (id_venta_str, fecha, id_empleado_str, nit_val, total_str) = linea.strip().split(":")
                        # El nit puede ser 'C/F' o un numero
                        nit = int(nit_val) if nit_val.isdigit() else nit_val
                        self.diccionario_ventas[int(id_venta_str)] = Venta(int(id_venta_str), fecha, int(id_empleado_str), nit, float(total_str))
            print("Ventas cargadas desde ventas.txt")
        except FileNotFoundError:
            print("No se encontro el archivo ventas.txt, se creara uno nuevo al guardar")
        except Exception as ex:
            print(f"Ha ocurrido un error al cargar ventas: {ex}")

    def mostrar_ventas(self):
        print("\n---Ventas---")
        if not self.diccionario_ventas:
            print("No hay ventas registradas.")
        else:
            lista_ventas = list(self.diccionario_ventas.values())
            print("Como desea ordenar la lista?")
            print("1. Por ID de Venta (menor a mayor)")
            print("2. Por Total (menor a mayor)")
            try:
                opcion = int(input("Elija una opcion: "))
                match opcion:
                    case 1:
                        lista_ordenada = self.sorter.quick_sort_id(lista_ventas)
                    case 2:
                        lista_ordenada = self.sorter.quick_sort_total(lista_ventas)
                    case _:
                        print("Opcion invalida, se mostrara sin ordenar")
                        lista_ordenada = lista_ventas
                for venta in lista_ordenada:
                    print(f"ID Venta: {venta.id_venta} | Fecha: {venta._fecha} | Empleado ID: {venta.id_empleado} | Cliente NIT: {venta.nit} | Total: Q{venta._total:.2f}")
            except Exception as ex:
                print(f"Ha ocurrido un error: {ex}")