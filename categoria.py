class Categoria():
    def __init__(self, id_categoria, nombre):
        self.id_categoria = id_categoria
        self._nombre = nombre

class quick_sorts_categorias():
    def quick_sort_id(self, lista):
        if len(lista) <= 1:
            return lista
        pivote = lista[0]
        menores = [x for x in lista[1:] if x.id_categoria < pivote.id_categoria]
        iguales = [x for x in lista if x.id_categoria == pivote.id_categoria]
        mayores = [x for x in lista[1:] if x.id_categoria > pivote.id_categoria]
        return self.quick_sort_id(menores) + iguales + self.quick_sort_id(mayores)

    def quick_sort_nombre(self, lista):
        if len(lista) <= 1:
            return lista
        pivote = lista[0]
        menores = [x for x in lista[1:] if x._nombre < pivote._nombre]
        iguales = [x for x in lista if x._nombre == pivote._nombre]
        mayores = [x for x in lista[1:] if x._nombre > pivote._nombre]
        return self.quick_sort_nombre(menores) + iguales + self.quick_sort_nombre(mayores)

class registro_categorias():
    def __init__(self):
        self.diccionario_categorias = {}
        self.cargar_categorias()
        self.sorter = quick_sorts_categorias()

    def registrar_categorias(self):
        s = False
        while s == False:
            try:
                cantidad = int(input("Ingrese la cantidad de categorias que desasea registrar: "))
                if  cantidad <= 0:
                    print("La cantidad debe de ser un numero entero mayor a cero")
                else:
                     s = True
            except Exception as ex:
                print(f"Ha ocurrido un error: {ex}")
        for i in range(cantidad):
            s = False
            print(f"Categoria: #{i+1}")
            while s == False:
                try:
                    id_categoria = int(input("Ingrese el id de la categoria: "))
                    if id_categoria in self.diccionario_categorias:
                        print("El ID ya este en uso, intente de nuevo")
                    else:
                        s = True
                except Exception as ex:
                    print(f"Ha ocurrido un error: {ex}")
            nombre = input("Ingrese el nombre de la categoria: ").strip().lower()
            self.diccionario_categorias[id_categoria] = Categoria(id_categoria, nombre)
            print("Categoria registrada en el sistema")
        
        self.guardar_categorias()
        print("Datos de categorias guardados en el archivo")

    def mostrar_categorias(self):
        print("\n---Categorias ---")
        if not self.diccionario_categorias:
            print("No hay categorias registradas.")
        else:
            lista_categorias = list(self.diccionario_categorias.values())
            print("Como desea ordenar la lista?")
            print("1. Por ID (menor a mayor)")
            print("2. Por Nombre (alfabeticamente)")
            try:
                opcion = int(input("Elija una opcion: "))
                match opcion:
                    case 1:
                        lista_ordenada = self.sorter.quick_sort_id(lista_categorias)
                    case 2:
                        lista_ordenada = self.sorter.quick_sort_nombre(lista_categorias)
                    case _:
                        print("Opcion invalida, se mostrara sin ordenar")
                        lista_ordenada = lista_categorias
                for categoria in lista_ordenada:
                    print(f"ID: {categoria.id_categoria} | Nombre: {categoria._nombre}")
            except Exception as ex:
                print(f"Ha ocurrido un error: {ex}")

    def modificar_categoria(self):
        print("\n---Modificar Categoria---")
        if not self.diccionario_categorias:
            print("No hay categorias para modificar.")
        else:
            s = False
            while s == False:
                try:
                    id_cat = int(input("Ingrese el ID de la categoria que desea modificar: "))
                    if id_cat in self.diccionario_categorias:
                        s = True
                    else:
                        print("Error, la categoria no existe, intente de nuevo")
                except Exception as ex:
                    print(f"Ha ocurrido un error: {ex}")
            
            categoria_a_modificar = self.diccionario_categorias[id_cat]
            print(f"Nombre actual: {categoria_a_modificar._nombre}")
            nuevo_nombre = input("Ingrese el nuevo nombre para la categoria: ").strip().lower()
            
            categoria_a_modificar._nombre = nuevo_nombre
            self.guardar_categorias()
            print("Categoria modificada con exito.")

    def guardar_categorias(self):
        try:
            with open("categorias.txt", "w") as archivo:
                for categoria in self.diccionario_categorias.values():
                    archivo.write(f"{categoria.id_categoria}:{categoria._nombre}\n")
        except Exception as ex:
            print(f"Ha ocurrido un error al guardar: {ex}")

    def cargar_categorias(self):
        try:
            with open("categorias.txt", "r") as archivo:
                for linea in archivo.readlines():
                    if linea.strip():
                        id_str, nombre = linea.strip().split(":")
                        id_categoria = int(id_str)
                        self.diccionario_categorias[id_categoria] = Categoria(id_categoria, nombre)
            print("Categorias cargadas desde categorias.txt")
        except FileNotFoundError:
            print("No se encontro el archivo categorias.txt, se creara uno nuevo al guardar")
        except Exception as ex:
            print(f"Ha ocurrido un error al cargar: {ex}")