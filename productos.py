class Producto():
    def __init__(self, id_producto, nombre, precio, id_categoria, total_compras, total_ventas, stock):
        self.id_producto = id_producto
        self.id_categoria = id_categoria
        self._nombre = nombre
        self._precio = precio
        self._total_compras = total_compras
        self._total_ventas = total_ventas
        self._stock = stock

class registro_productos():
    def __init__(self):
        self.diccionario_productos = {}

    def registrar_productos(self, registro_categorias):
        s = False
        while s == False:
            try:
                cantidad = int(input("Ingrese la cantidad de productos que desasea registrar: "))
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
                    stock = int(input("Ingrese el stock del producto: "))
                    if stock > 0:
                        s = True
                    else:
                        print("El stock debe de ser mayor a cero")
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
            nuevo_producto = Producto(id_producto, nombre, precio, id_categoria, 0, 0, stock)
            self.diccionario_productos[id_producto] = nuevo_producto
            print("Producto registrado en el sistema")