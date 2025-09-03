from datetime import date
class Venta():
    def __init__(self, id_venta, fecha, id_empleado, nit, total):
        self.id_venta = id_venta
        self._fecha = fecha
        self.id_empleado = id_empleado
        self.nit = nit
        self._total = total

class registro_ventas():
    def __init__(self):
        self.diccionario_ventas = {}
        self.cargar_ventas()

    def registrar_ventas(self, registro_empleados, registro_clientes, registro_productos):
        s = False
        while s == False:
            try:
                id_venta = int(input("Ingrese el id de la venta: "))
                if id_venta in self.diccionario_ventas:
                    print("El id ya este en uso, intente de nuevo")
                else:
                    s = True
            except Exception as ex:
                print(f"Ha ocurrido un error: {ex}")
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
                        if producto_obj._stock > 0:
                            producto_obj._stock -= 1
                            total += producto_obj._precio
                            print(f"'{producto_obj._nombre}' agregado, quedan: {producto_obj._stock}")
                        else:
                            print(f"No hay stock disponible de {producto_obj._nombre}")
                    else:
                        print("Error, producto no encontrado")
            except Exception as ex:
                print(f"Ha ocurrido un error: {ex}")
        fecha = date.today().isoformat()
        nueva_venta = Venta(id_venta, fecha, id_empleado, nit, total)
        self.diccionario_ventas[id_venta] = nueva_venta
        print(f"Venta #{id_venta} registrada con exito. Total: Q{total:.2f}")
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
                        nit = int(nit_val) if nit_val.isdigit() else nit_val
                        self.diccionario_ventas[int(id_venta_str)] = Venta(int(id_venta_str), fecha, int(id_empleado_str), nit, float(total_str))
            print("Ventas cargadas desde ventas.txt")
        except FileNotFoundError:
            print("No se encontro el archivo ventas.txt, se creara uno nuevo al guardar")
        except Exception as ex:
            print(f"Ha ocurrido un error al cargar ventas: {ex}")