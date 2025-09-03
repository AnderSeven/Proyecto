class Empleado():
    def __init__(self, id_empleado, nombre, direccion, telefono, correo, puesto):
        self.id_empleado = id_empleado
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono
        self._correo = correo
        self._puesto = puesto

class quick_sorts_empleados():
    def quick_sort_id(self, lista):
        if len(lista) <= 1: return lista
        pivote = lista[0]
        menores = [x for x in lista[1:] if x.id_empleado < pivote.id_empleado]
        iguales = [x for x in lista if x.id_empleado == pivote.id_empleado]
        mayores = [x for x in lista[1:] if x.id_empleado > pivote.id_empleado]
        return self.quick_sort_id(menores) + iguales + self.quick_sort_id(mayores)

    def quick_sort_nombre(self, lista):
        if len(lista) <= 1: return lista
        pivote = lista[0]
        menores = [x for x in lista[1:] if x._nombre < pivote._nombre]
        iguales = [x for x in lista if x._nombre == pivote._nombre]
        mayores = [x for x in lista[1:] if x._nombre > pivote._nombre]
        return self.quick_sort_nombre(menores) + iguales + self.quick_sort_nombre(mayores)

class registro_empleados():
    def __init__(self):
        self.diccionario_empleados = {}
        self.cargar_empleados()
        self.sorter = quick_sorts_empleados()

    def registrar_empleados(self):
        s = False
        while s == False:
            try:
                cantidad = int(input("Ingrese la cantidad de empleados que desea registrar: "))
                if cantidad > 0:
                    s = True
                else:
                    print("La cantidad debe de ser un numero entero mayor a cero")
            except Exception as ex:
                print(f"Ha ocurrido un error: {ex}")
        
        for i in range(cantidad):
            s = False
            print(f"\nEmpleado: #{i+1}")
            s = False
            while s == False:
                try:
                    id_empleado = int(input("Ingrese el id del empleado: "))
                    if id_empleado in self.diccionario_empleados:
                        print("El id ya este en uso, intente de nuevo")
                    else:
                        s = True
                except Exception as ex:
                    print(f"Ha ocurrido un error: {ex}")
            nombre = input("Ingrese el nombre del empleado: ").strip()
            direccion = input("Ingrese la direccion del empleado: ").strip()
            telefono = input("Ingrese el telefono del empleado: ").strip()
            correo = input("Ingrese el correo del empleado: ").strip()
            puesto = input("Ingrese el puesto del empleado: ").strip().capitalize()
            if puesto == "Admin":
                nuevo_empleado = Admin(id_empleado, nombre, direccion, telefono, correo)
            else:
                nuevo_empleado = Empleado(id_empleado, nombre, direccion, telefono, correo, puesto)
            self.diccionario_empleados[id_empleado] = nuevo_empleado
            print("Empleado registrado en el sistema")
        self.guardar_empleados()
        print("Datos de empleados guardados en el archivo")

    def registrar_solo_admin(self):
        print("\n--- Registrar Nuevo Admin ---")
        s = False
        while s == False:
            try:
                id_empleado = int(input("Ingrese el id del nuevo admin: "))
                if id_empleado in self.diccionario_empleados:
                    print("El id ya esta en uso, intente de nuevo")
                else:
                    s = True
            except Exception as ex:
                print(f"Ha ocurrido un error: {ex}")
        
        nombre = input("Ingrese el nombre del admin: ").strip()
        direccion = input("Ingrese la direccion del admin: ").strip()
        telefono = input("Ingrese el telefono del admin: ").strip()
        correo = input("Ingrese el correo del admin: ").strip()
        
        nuevo_admin = Admin(id_empleado, nombre, direccion, telefono, correo)
        self.diccionario_empleados[id_empleado] = nuevo_admin
        
        self.guardar_empleados()
        print("Nuevo admin registrado y guardado con exito")

    def guardar_empleados(self):
        try:
            with open("empleados.txt", "w") as archivo:
                for empleado in self.diccionario_empleados.values():
                    linea = f"{empleado.id_empleado}:{empleado._nombre}:{empleado._direccion}:{empleado._telefono}:{empleado._correo}:{empleado._puesto}\n"
                    archivo.write(linea)
        except Exception as ex:
            print(f"Ha ocurrido un error al guardar empleados: {ex}")

    def cargar_empleados(self):
        try:
            with open("empleados.txt", "r") as archivo:
                for linea in archivo.readlines():
                    if linea.strip():
                        id_str, nombre, direccion, telefono, correo, puesto = linea.strip().split(":")
                        id_empleado = int(id_str)
                        if puesto == "Admin":
                            nuevo_empleado = Admin(id_empleado, nombre, direccion, telefono, correo)
                        else:
                            nuevo_empleado = Empleado(id_empleado, nombre, direccion, telefono, correo, puesto)
                        self.diccionario_empleados[id_empleado] = nuevo_empleado
            print("Empleados cargados desde empleados.txt")
        except FileNotFoundError:
            print("No se encontro el archivo empleados.txt, se creara uno nuevo al guardar")
        except Exception as ex:
            print(f"Ha ocurrido un error al cargar empleados: {ex}")

    def mostrar_empleados(self):
        print("\n---Empleados---")
        if not self.diccionario_empleados:
            print("No hay empleados registrados.")
        else:
            lista_empleados = list(self.diccionario_empleados.values())
            print("Como desea ordenar la lista?")
            print("1. Por ID (menor a mayor)")
            print("2. Por Nombre (alfabeticamente)")
            try:
                opcion = int(input("Elija una opcion: "))
                match opcion:
                    case 1:
                        lista_ordenada = self.sorter.quick_sort_id(lista_empleados)
                    case 2:
                        lista_ordenada = self.sorter.quick_sort_nombre(lista_empleados)
                    case _:
                        print("Opcion invalida, se mostrara sin ordenar")
                        lista_ordenada = lista_empleados
                for empleado in lista_ordenada:
                    print(f"ID: {empleado.id_empleado} | Nombre: {empleado._nombre} | Puesto: {empleado._puesto}")
            except Exception as ex:
                print(f"Ha ocurrido un error: {ex}")

class Admin(Empleado):
    def __init__(self, id_empleado, nombre, direccion, telefono, correo):
        Empleado.__init__(self, id_empleado, nombre, direccion, telefono, correo, puesto = "Admin")