class Categoria():
    def __init__(self, id_categoria, nombre):
        self.id_categoria = id_categoria
        self._nombre = nombre

class registro_categorias():
    def __init__(self):
        self.diccionario_categorias = {}

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

    def _quick_sort_id(self, lista):
        if len(lista) <= 1:
            return lista
        pivote = lista[0]
        menores = [x for x in lista[1:] if x.id_categoria < pivote.id_categoria]
        iguales = [x for x in lista if x.id_categoria == pivote.id_categoria]
        mayores = [x for x in lista[1:] if x.id_categoria > pivote.id_categoria]
        return self._quick_sort_id(menores) + iguales + self._quick_sort_id(mayores)

    def _quick_sort_nombre(self, lista):
        if len(lista) <= 1:
            return lista
        pivote = lista[0]
        menores = [x for x in lista[1:] if x._nombre < pivote._nombre]
        iguales = [x for x in lista if x._nombre == pivote._nombre]
        mayores = [x for x in lista[1:] if x._nombre > pivote._nombre]
        return self._quick_sort_nombre(menores) + iguales + self._quick_sort_nombre(mayores)

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
                        lista_ordenada = self._quick_sort_id(lista_categorias)
                    case 2:
                        lista_ordenada = self._quick_sort_nombre(lista_categorias)
                    case _:
                        print("Opcion invalida, se mostrara sin ordenar")
                        lista_ordenada = lista_categorias
                for categoria in lista_ordenada:
                    print(f"ID: {categoria.id_categoria} | Nombre: {categoria._nombre}")
            except Exception as ex:
                print(f"Ha ocurrido un error: {ex}")