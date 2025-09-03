class Proveedor():
    def __init__(self, nit, nombre, direccion, telefono, correo, empresa):
        self.nit = nit
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono
        self._correo = correo
        self._empresa = empresa

class quick_sorts_proveedores():
    def quick_sort_nit(self, lista):
        if len(lista) <= 1: return lista
        pivote = lista[0]
        menores = [x for x in lista[1:] if x.nit < pivote.nit]
        iguales = [x for x in lista if x.nit == pivote.nit]
        mayores = [x for x in lista[1:] if x.nit > pivote.nit]
        return self.quick_sort_nit(menores) + iguales + self.quick_sort_nit(mayores)

    def quick_sort_nombre(self, lista):
        if len(lista) <= 1: return lista
        pivote = lista[0]
        menores = [x for x in lista[1:] if x._nombre < pivote._nombre]
        iguales = [x for x in lista if x._nombre == pivote._nombre]
        mayores = [x for x in lista[1:] if x._nombre > pivote._nombre]
        return self.quick_sort_nombre(menores) + iguales + self.quick_sort_nombre(mayores)

class registro_proveedores():
    def __init__(self):
        self.diccionario_proveedores = {}
        self.cargar_proveedores()
        self.sorter = quick_sorts_proveedores()

    def registrar_proveedores(self):
        s = False
        while s == False:
            try:
                cantidad = int(input("Ingrese la cantidad de proveedores que desea registrar: "))
                if cantidad > 0:
                    s = True
                else:
                    print("La cantidad debe de ser un numero entero mayor a cero")
            except Exception as ex:
                print(f"Ha ocurrido un error: {ex}")

        for i in range(cantidad):
            print(f"\nProveedor: #{i+1}")
            s_nit = False
            while s_nit == False:
                try:
                    nit = int(input("Ingrese el nit del proveedor: "))
                    if nit in self.diccionario_proveedores:
                        print("Error, el nit ya esta en uso, intente de nuevo")
                    else:
                        s_nit = True
                except Exception as ex:
                    print(f"Ha ocurrido un error: {ex}")

            nombre = input("Ingrese el nombre del proveedor: ").strip()
            direccion = input("Ingrese la direccion del proveedor: ").strip()
            telefono = input("Ingrese el telefono del proveedor: ").strip()
            correo = input("Ingrese el correo del proveedor: ").strip()
            empresa = input("Ingrese el nombre de la empresa: ").strip()
            self.diccionario_proveedores[nit] = Proveedor(nit, nombre, direccion, telefono, correo, empresa)
            print("Proveedor registrado en el sistema")
        self.guardar_proveedores()
        print("Datos de proveedores guardados en el archivo")

    def guardar_proveedores(self):
        try:
            with open("proveedores.txt", "w") as archivo:
                for proveedor in self.diccionario_proveedores.values():
                    archivo.write(f"{proveedor.nit}:{proveedor._nombre}:{proveedor._direccion}:{proveedor._telefono}:{proveedor._correo}:{proveedor._empresa}\n")
        except Exception as ex:
            print(f"Ha ocurrido un error al guardar proveedores: {ex}")

    def cargar_proveedores(self):
        try:
            with open("proveedores.txt", "r") as archivo:
                for linea in archivo.readlines():
                    if linea.strip():
                        nit_str, nombre, direccion, telefono, correo, empresa = linea.strip().split(":")
                        self.diccionario_proveedores[int(nit_str)] = Proveedor(int(nit_str), nombre, direccion, telefono, correo, empresa)
            print("Proveedores cargados desde proveedores.txt")
        except FileNotFoundError:
            print("No se encontro el archivo proveedores.txt, se creara uno nuevo al guardar")
        except Exception as ex:
            print(f"Ha ocurrido un error al cargar proveedores: {ex}")

    def mostrar_proveedores(self):
        print("\n---Proveedores---")
        if not self.diccionario_proveedores:
            print("No hay proveedores registrados.")
        else:
            lista_proveedores = list(self.diccionario_proveedores.values())
            print("Como desea ordenar la lista?")
            print("1. Por NIT (menor a mayor)")
            print("2. Por Nombre (alfabeticamente)")
            try:
                opcion = int(input("Elija una opcion: "))
                match opcion:
                    case 1:
                        lista_ordenada = self.sorter.quick_sort_nit(lista_proveedores)
                    case 2:
                        lista_ordenada = self.sorter.quick_sort_nombre(lista_proveedores)
                    case _:
                        print("Opcion invalida, se mostrara sin ordenar")
                        lista_ordenada = lista_proveedores
                for proveedor in lista_ordenada:
                    print(f"NIT: {proveedor.nit} | Nombre: {proveedor._nombre} | Empresa: {proveedor._empresa} | Telefono: {proveedor._telefono}")
            except Exception as ex:
                print(f"Ha ocurrido un error: {ex}")