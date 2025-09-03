from menus import Menus
from categoria import registro_categorias
from productos import registro_productos
from clientes import registro_clientes
from proveedores import registro_proveedores
from empleados import registro_empleados
from compras import registro_compras
from ventas import registro_ventas
from detalle_ventas import registro_detalle_ventas
from detalle_compras import registro_detalle_compra

registro_cat = registro_categorias()
registro_prod = registro_productos()
registro_cli = registro_clientes()
registro_prov = registro_proveedores()
registro_emp = registro_empleados()
registro_comp = registro_compras()
registro_dc = registro_detalle_compra()
registro_ven = registro_ventas()
registro_dv = registro_detalle_ventas()

menu = Menus()

opcion = 0
a = False
while a == False:
    try:
        menu.menu_principal()
        opcion = int(input("Ingrese una opcion: "))
        match opcion:
            case 0:
                clave_jefe = input("Ingrese la clave de jefe: ")
                if clave_jefe == "jefe123":
                    registro_emp.registrar_solo_admin()
                else:
                    print("Clave incorrecta")
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
                                registro_comp.mostrar_compras()
                            case 2:
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
                                registro_ven.registrar_ventas(registro_emp, registro_cli, registro_prod, registro_dv)
                            case 2:
                                registro_ven.mostrar_ventas()
                            case 3:
                                s = True
                            case _:
                                print("Opcion invalida")
                    except Exception as ex:
                        print(f"Ha ocurrido un error: {ex}")
            case 8:
                clave_admin = input("Ingrese la clave de administrador: ")
                if clave_admin == "admin123":
                    s = False
                    while s == False:
                        try:
                            menu.menu_admin()
                            opcion = int(input("Ingrese una opcion: "))
                            match opcion:
                                case 1:
                                    registro_cat.modificar_categoria()
                                case 2:
                                    registro_prod.modificar_producto()
                                case 3:
                                    registro_cli.modificar_cliente()
                                case 4:
                                    registro_emp.modificar_empleado()
                                case 5:
                                    registro_comp.registrar_compras(registro_emp, registro_prov, registro_prod, registro_dc)
                                case 6:
                                    registro_ven.modificar_venta(registro_prod, registro_dv)
                                case 7:
                                    registro_comp.modificar_compra(registro_prod, registro_dc)
                                case 8:
                                    registro_prov.modificar_proveedor()
                                case 9:
                                    s = True
                                case _:
                                    print("Opcion invalida")
                        except Exception as ex:
                            print(f"Ha ocurrido un error: {ex}")
                else:
                    print("Clave incorrecta")
            case 9:
                print("Gracias por usar el sistema")
                a = True
            case _:
                print("Opcion invalida")
    except Exception as ex:
        print(f"Ha ocurrido un error: {ex}")