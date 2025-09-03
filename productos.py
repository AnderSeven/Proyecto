class Producto():
    def __init__(self, id_producto, nombre, precio, id_categoria, total_compras, total_ventas, stock):
        self.id_producto = id_producto
        self.id_categoria = id_categoria
        self._nombre = nombre
        self._precio = precio
        self._total_compras = total_compras
        self._total_ventas = total_ventas
        self._stock = stock

class quick_sorts_productos():
    def quick_sort_id(self, lista):
        if len(lista) <= 1: return lista
        pivote = lista[0]
        menores = [x for x in lista[1:] if x.id_producto < pivote.id_producto]
        iguales = [x for x in lista if x.id_producto == pivote.id_producto]
        mayores = [x for x in lista[1:] if x.id_producto > pivote.id_producto]
        return self.quick_sort_id(menores) + iguales + self.quick_sort_id(mayores)

    def quick_sort_nombre(self, lista):
        if len(lista) <= 1: return lista
        pivote = lista[0]
        menores = [x for x in lista[1:] if x._nombre < pivote._nombre]
        iguales = [x for x in lista if x._nombre == pivote._nombre]
        mayores = [x for x in lista[1:] if x._nombre > pivote._nombre]
        return self.quick_sort_nombre(menores) + iguales + self.quick_sort_nombre(mayores)

    def quick_sort_precio(self, lista):
        if len(lista) <= 1: return lista
        pivote = lista[0]
        menores = [x for x in lista[1:] if x._precio < pivote._precio]
        iguales = [x for x in lista if x._precio == pivote._precio]
        mayores = [x for x in lista[1:] if x._precio > pivote._precio]
        return self.quick_sort_precio(menores) + iguales + self.quick_sort_precio(mayores)

    def quick_sort_stock(self, lista):
        if len(lista) <= 1: return lista
        pivote = lista[0]
        menores = [x for x in lista[1:] if x._stock < pivote._stock]
        iguales = [x for x in lista if x._stock == pivote._stock]
        mayores = [x for x in lista[1:] if x._stock > pivote._stock]
        return self.quick_sort_stock(menores) + iguales + self.quick_sort_stock(mayores)

class registro_productos():
    def __init__(self):
        self.diccionario_productos = {}
        self.cargar_productos()
        self.sorter = quick_sorts_productos()

    def registrar_productos(self, registro_categorias):
        s = False
        while s == False:
            try:
                cantidad = int(input("Ingrese la cantidad de productos que desea registrar: "))
                if cantidad > 0:
                    s = True
                else:
                    print("La cantidad debe de ser un numero entero mayor a cero")
            except Exception as ex:
                print(f"Ha ocurrido un error: {ex}")
        for i in range(cantidad):
            print(f"\nProducto: #{i+1}")
            s = False
            while s == False:
                try:
                    id_producto = int(input("Ingrese el id del producto: "))
                    if id_producto in self.diccionario_productos:
                        print("El id ya este en uso, intente de nuevo")
                    else:
                        s = True
                except Exception as ex:
                    print(f"Ha ocurrido un error: {ex}")
            nombre = input("Ingrese el nombre del producto: ").strip().lower()
            nombre_duplicado = False
            for producto_existente in self.diccionario_productos.values():
                if producto_existente._nombre.lower() == nombre:
                    print(f"Error, ya existe un producto con el nombre {nombre}, este producto no se registrara")
                    nombre_duplicado = True
                    break
            if nombre_duplicado:
                continue
            s = False
            while s == False:
                try:
                    precio = float(input("Ingrese el precio del producto: "))
                    if precio > 0:
                        s = True
                    else:
                        print("El precio debe de ser un numero mayor a cero")
                except Exception as ex:
                    print(f"Ha ocurrido un error: {ex}")
            s = False
            while s == False:
                try:
                    id_categoria = int(input("Ingrese el id de la categoria a la que le pertenece: "))
                    if id_categoria in registro_categorias.diccionario_categorias:
                        s = True
                    else:
                        print("Error, la categoria no existe, intenta de nuevo")
                except Exception as ex:
                    print(f"Ha ocurrido un error: {ex}")
            nuevo_producto = Producto(id_producto, nombre, precio, id_categoria, 0, 0, 0)
            self.diccionario_productos[id_producto] = nuevo_producto
            print("Producto registrado en el sistema")
        self.guardar_productos()
        print("Datos de productos guardados en el archivo")

    def guardar_productos(self):
        try:
            with open("productos.txt", "w") as archivo:
                for producto in self.diccionario_productos.values():
                    linea = f"{producto.id_producto}:{producto._nombre}:{producto._precio}:{producto.id_categoria}:{producto._total_compras}:{producto._total_ventas}:{producto._stock}\n"
                    archivo.write(linea)
        except Exception as ex:
            print(f"Ha ocurrido un error al guardar productos: {ex}")

    def cargar_productos(self):
        try:
            with open("productos.txt", "r") as archivo:
                for linea in archivo.readlines():
                    if linea.strip():
                        (id_str, nombre, precio_str, id_cat_str, 
                         compras_str, ventas_str, stock_str) = linea.strip().split(":")
                        id_producto = int(id_str)
                        precio = float(precio_str)
                        id_categoria = int(id_cat_str)
                        nuevo_producto = Producto(id_producto, nombre, precio, id_categoria, int(compras_str), int(ventas_str), int(stock_str))
                        self.diccionario_productos[id_producto] = nuevo_producto
            print("Productos cargados desde productos.txt")
        except FileNotFoundError:
            print("No se encontro el archivo productos.txt, se creara uno nuevo al guardar")
        except Exception as ex:
            print(f"Ha ocurrido un error al cargar productos: {ex}")

    def mostrar_productos(self):
        print("\n---Productos---")
        if not self.diccionario_productos:
            print("No hay productos registrados.")
        else:
            lista_productos = list(self.diccionario_productos.values())
            print("Como desea ordenar la lista?")
            print("1. Por ID (menor a mayor)")
            print("2. Por Nombre (alfabeticamente)")
            print("3. Por Precio (menor a mayor)")
            print("4. Por Stock (menor a mayor)")
            try:
                opcion = int(input("Elija una opcion: "))
                match opcion:
                    case 1:
                        lista_ordenada = self.sorter.quick_sort_id(lista_productos)
                    case 2:
                        lista_ordenada = self.sorter.quick_sort_nombre(lista_productos)
                    case 3:
                        lista_ordenada = self.sorter.quick_sort_precio(lista_productos)
                    case 4:
                        lista_ordenada = self.sorter.quick_sort_stock(lista_productos)
                    case _:
                        print("Opcion invalida, se mostrara sin ordenar")
                        lista_ordenada = lista_productos
                for producto in lista_ordenada:
                    print(f"ID: {producto.id_producto} | Nombre: {producto._nombre} | Precio: Q{producto._precio:.2f} | Stock: {producto._stock} | Categoria ID: {producto.id_categoria}")
            except Exception as ex:
                print(f"Ha ocurrido un error: {ex}")

    def modificar_producto(self):
        print("\n---Modificar Producto---")
        if not self.diccionario_productos:
            print("No hay productos para modificar.")
        else:
            s = False
            while s == False:
                try:
                    id_prod = int(input("Ingrese el ID del producto que desea modificar: "))
                    if id_prod in self.diccionario_productos:
                        s = True
                    else:
                        print("Error, el producto no existe, intente de nuevo")
                except Exception as ex:
                    print(f"Ha ocurrido un error: {ex}")
            
            producto_a_modificar = self.diccionario_productos[id_prod]
            print(f"Datos actuales -> Nombre: {producto_a_modificar._nombre}, Precio: Q{producto_a_modificar._precio:.2f}")
            
            print("Que desea modificar?")
            print("1. Nombre")
            print("2. Precio")
            opcion = input("Elija una opcion: ")

            match opcion:
                case "1":
                    nombre_duplicado = False
                    nuevo_nombre = input("Ingrese el nuevo nombre: ").strip().lower()
                    for producto_existente in self.diccionario_productos.values():
                        if producto_existente._nombre.lower() == nuevo_nombre and producto_existente.id_producto != id_prod:
                            print(f"Error, ya existe otro producto con el nombre {nuevo_nombre}")
                            nombre_duplicado = True
                            break
                    if not nombre_duplicado:
                        producto_a_modificar._nombre = nuevo_nombre
                case "2":
                    producto_a_modificar._precio = float(input("Ingrese el nuevo precio: "))
                case _:
                    print("Opcion no valida.")
            
            if opcion in ["1", "2"]:
                self.guardar_productos()
                print("Producto modificado con exito y cambios guardados.")