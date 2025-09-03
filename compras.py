class Compra():
    def __init__(self, id_compra, fecha_ingreso, id_empleado, nit, total):
        self.id_compra = id_compra
        self._fecha_ingreso = fecha_ingreso
        self.id_empleado = id_empleado
        self.nit = nit
        self._total = total
class quick_sorts_compras():
    def quick_sort_id(self, lista):
        if len(lista) <= 1: return lista
        pivote = lista[0]
        menores = [x for x in lista[1:] if x.id_compra < pivote.id_compra]
        iguales = [x for x in lista if x.id_compra == pivote.id_compra]
        mayores = [x for x in lista[1:] if x.id_compra > pivote.id_compra]
        return self.quick_sort_id(menores) + iguales + self.quick_sort_id(mayores)

    def quick_sort_total(self, lista):
        if len(lista) <= 1: return lista
        pivote = lista[0]
        menores = [x for x in lista[1:] if x._total < pivote._total]
        iguales = [x for x in lista if x._total == pivote._total]
        mayores = [x for x in lista[1:] if x._total > pivote._total]
        return self.quick_sort_total(menores) + iguales + self.quick_sort_total(mayores)
class registro_compras():
    def __init__(self):
        self.diccionario_compras = {}
        self.sorter = quick_sorts_compras()

    def mostrar_compras(self):
        print("\n---Compras---")
        if not self.diccionario_compras:
            print("No hay compras registradas.")
        else:
            lista_compras = list(self.diccionario_compras.values())
            print("Como desea ordenar la lista?")
            print("1. Por ID de Compra (menor a mayor)")
            print("2. Por Total (menor a mayor)")
            try:
                opcion = int(input("Elija una opcion: "))
                match opcion:
                    case 1:
                        lista_ordenada = self.sorter.quick_sort_id(lista_compras)
                    case 2:
                        lista_ordenada = self.sorter.quick_sort_total(lista_compras)
                    case _:
                        print("Opcion invalida, se mostrara sin ordenar")
                        lista_ordenada = lista_compras
                for compra in lista_ordenada:
                    print(f"ID Compra: {compra.id_compra} | Fecha: {compra._fecha_ingreso} | Empleado ID: {compra.id_empleado} | Proveedor NIT: {compra.nit} | Total: Q{compra._total:.2f}")
            except Exception as ex:
                print(f"Ha ocurrido un error: {ex}")