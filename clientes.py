class Cliente():
    def __init__(self, nit, nombre, direccion, telefono, correo):
        self.nit = nit
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono
        self._correo = correo

class quick_sorts_clientes():
    def quick_sort_nit(self, lista):
        if len(lista) <= 1:
            return lista
        pivote = lista[0]
        menores = [x for x in lista[1:] if x.nit < pivote.nit]
        iguales = [x for x in lista if x.nit == pivote.nit]
        mayores = [x for x in lista[1:] if x.nit > pivote.nit]
        return self.quick_sort_nit(menores) + iguales + self.quick_sort_nit(mayores)

    def quick_sort_nombre(self, lista):
        if len(lista) <= 1:
            return lista
        pivote = lista[0]
        menores = [x for x in lista[1:] if x._nombre < pivote._nombre]
        iguales = [x for x in lista if x._nombre == pivote._nombre]
        mayores = [x for x in lista[1:] if x._nombre > pivote._nombre]
        return self.quick_sort_nombre(menores) + iguales + self.quick_sort_nombre(mayores)

class registro_clientes():
    def __init__(self):
        self.diccionario_clientes = {}
        self.cargar_clientes()
        self.sorter = quick_sorts_clientes()

    def registrar_clientes(self):
        s = False
        while s == False:
            try:
                cantidad = int(input("Ingrese la cantidad de clientes que desea registrar: "))
                if  cantidad > 0:
                    s = True
                else:
                    print("La cantidad debe de ser un numero entero mayor a cero")
            except Exception as ex:
                print(f"Ha ocurrido un error: {ex}")

            for i in range(cantidad):
                s = False
                print(f"Cliente: #{i+1}")
                while s == False:
                    try:
                        nit = int(input("Ingrese el nit del cliente: "))
                        if nit in self.diccionario_clientes:
                            print("El nit ya este en uso, intente de nuevo")
                        else:
                            s = True
                    except Exception as ex:
                        print(f"Ha ocurrido un error: {ex}")
                nombre = input("Ingrese el nombre del cliente: ").strip()
                direccion = input("Ingrese la direccion del cliente: ").strip()
                telefono = input("Ingrese el telefono del cliente: ").strip()
                correo = input("Ingrese el correo del cliente: ").strip()
                self.diccionario_clientes[nit] = Cliente(nit, nombre, direccion, telefono, correo)
                print(f"Cliente '{nombre}' registrado en el sistema")
        self.guardar_clientes()
        print("Datos de clientes guardados en el archivo")

    def registrar_un_solo_cliente(self, nit, nombre, direccion, telefono, correo):
        self.diccionario_clientes[nit] = Cliente(nit, nombre, direccion, telefono, correo)
        print("Cliente registrado en el sistema. ")
        self.guardar_clientes()

    def guardar_clientes(self):
        try:
            with open("clientes.txt", "w") as archivo:
                for cliente in self.diccionario_clientes.values():
                    archivo.write(f"{cliente.nit}:{cliente._nombre}:{cliente._direccion}:{cliente._telefono}:{cliente._correo}\n")
        except Exception as ex:
            print(f"Ha ocurrido un error al guardar clientes: {ex}")

    def cargar_clientes(self):
        try:
            with open("clientes.txt", "r") as archivo:
                for linea in archivo.readlines():
                    if linea.strip():
                        nit_str, nombre, direccion, telefono, correo = linea.strip().split(":")
                        nit = int(nit_str)
                        self.diccionario_clientes[nit] = Cliente(nit, nombre, direccion, telefono, correo)
            print("Clientes cargados desde clientes.txt")
        except FileNotFoundError:
            print("No se encontro el archivo clientes.txt, se creara uno nuevo al guardar")
        except Exception as ex:
            print(f"Ha ocurrido un error al cargar clientes: {ex}")

    def mostrar_clientes(self):
        print("\n---Clientes---")
        if not self.diccionario_clientes:
            print("No hay clientes registrados.")
        else:
            lista_clientes = list(self.diccionario_clientes.values())
            print("Como desea ordenar la lista?")
            print("1. Por NIT (menor a mayor)")
            print("2. Por Nombre (alfabeticamente)")
            try:
                opcion = int(input("Elija una opcion: "))
                match opcion:
                    case 1:
                        lista_ordenada = self.sorter.quick_sort_nit(lista_clientes)
                    case 2:
                        lista_ordenada = self.sorter.quick_sort_nombre(lista_clientes)
                    case _:
                        print("Opcion invalida, se mostrara sin ordenar")
                        lista_ordenada = lista_clientes
                for cliente in lista_ordenada:
                    print(f"NIT: {cliente.nit} | Nombre: {cliente._nombre} | Direccion: {cliente._direccion} | Telefono: {cliente._telefono} | Correo: {cliente._correo}")
            except Exception as ex:
                print(f"Ha ocurrido un error: {ex}")