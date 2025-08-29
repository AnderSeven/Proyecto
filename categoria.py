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
            cantidad = int(input("Ingrese la cantidad de categorias que desasea registrar: "))
            if  cantidad <= 0:
                print("La cantidad debe de ser un numero entero mayor a cero")
            else:
                 s = True
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
    #ahora que lo pienso en categorias en categorias solo podria hacerlo por el alfabeto