from menus import Menus
from categoria import registro_categorias
from productos import registro_productos
from clientes import registro_clientes
from proveedores import registro_proveedores
from empleados import registro_empleados
from compras import registro_compras
from ventas import registro_ventas

registro_cat = registro_categorias()
registro_prod = registro_productos()
registro_cli = registro_clientes()
registro_prov = registro_proveedores()
registro_emp = registro_empleados()
registro_comp = registro_compras()
registro_ven = registro_ventas()

menu = Menus()

opcion = 0
a = False
while a == False:
    try:
        menu.menu_principal()
        opcion = int(input("Ingrese una opcion: "))
        match opcion:
            case 1:
                s = False
                while s == False:
                    try:
                        menu.menu_categorias()
                        opcion = int(input("Ingrese una opcion: "))
                        match opcion:
                            case 1:
                                registro_cat.registrar_categorias()
                            case 2:
                                registro_cat.mostrar_categorias()
                            case 3:
                                s = True
                            case _:
                                print("Opcion invalida")
                    except Exception as ex:
                        print(f"Ha ocurrido un error: {ex}")
            case 2:
                s = False
                while s == False:
                    try:
                        menu.menu_productos()
                        opcion = int(input("Ingrese una opcion: "))
                        match opcion:
                            case 1:
                                registro_prod.registrar_productos(registro_cat)
                            case 2:
                                registro_prod.mostrar_productos()
                            case 3:
                                s = True
                            case _:
                                print("Opcion invalida")
                    except Exception as ex:
                        print(f"Ha ocurrido un error: {ex}")
            case 3:
                s = False
                while s == False:
                    try:
                        menu.menu_clientes()
                        opcion = int(input("Ingrese una opcion: "))
                        match opcion:
                            case 1:
                                registro_cli.registrar_clientes()
                            case 2:
                                registro_cli.mostrar_clientes()
                            case 3:
                                s = True
                            case _:
                                print("Opcion invalida")
                    except Exception as ex:
                        print(f"Ha ocurrido un error: {ex}")
            case 4:
                s = False
                while s == False:
                    try:
                        menu.menu_proveedores()
                        opcion = int(input("Ingrese una opcion: "))
                        match opcion:
                            case 1:
                                registro_prov.registrar_proveedores()
                            case 2:
                                registro_prov.mostrar_proveedores()
                            case 3:
                                s = True
                            case _:
                                print("Opcion invalida")
                    except Exception as ex:
                        print(f"Ha ocurrido un error: {ex}")
            case 5:
                s = False
                while s == False:
                    try:
                        menu.menu_empleados()
                        opcion = int(input("Ingrese una opcion: "))
                        match opcion:
                            case 1:
                                registro_emp.registrar_empleados()
                            case 2:
                                registro_emp.mostrar_empleados()
                            case 3:
                                s = True
                            case _:
                                print("Opcion invalida")
                    except Exception as ex:
                        print(f"Ha ocurrido un error: {ex}")
            case 6:
                s = False
                while s == False:
                    try:
                        menu.menu_compras()
                        opcion = int(input("Ingrese una opcion: "))
                        match opcion:
                            case 1:
                                pass
                            case 2:
                                registro_comp.mostrar_compras()
                            case 3:
                                pass
                            case 4:
                                s = True
                            case _:
                                print("Opcion invalida")
                    except Exception as ex:
                        print(f"Ha ocurrido un error: {ex}")
            case 7:
                s = False
                while s == False:
                    try:
                        menu.menu_ventas()
                        opcion = int(input("Ingrese una opcion: "))
                        match opcion:
                            case 1:
                                registro_ven.registrar_ventas(registro_emp, registro_cli, registro_prod)
                            case 2:
                                registro_ven.mostrar_ventas()
                            case 3:
                                pass
                            case 4:
                                s = True
                            case _:
                                print("Opcion invalida")
                    except Exception as ex:
                        print(f"Ha ocurrido un error: {ex}")
            case 8:
                s = False
                while s == False:
                    try:
                        menu.menu_admin()
                        opcion = int(input("Ingrese una opcion: "))
                        match opcion:
                            case 1:
                                pass
                            case 2:
                                pass
                            case 3:
                                pass
                            case 4:
                                pass
                            case 5:
                                pass
                            case 6:
                                pass
                            case 7:
                                pass
                            case 8:
                                s = True
                            case _:
                                print("Opcion invalida")
                    except Exception as ex:
                        print(f"Ha ocurrido un error: {ex}")
            case 9:
                print("Gracias por usar el sistema")
                a = True
            case _:
                print("Opcion invalida")
    except Exception as ex:
        print(f"Ha ocurrido un error: {ex}")