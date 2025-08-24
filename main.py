from menus import Menus
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
                                pass
                            case 2:
                                pass
                            case 3:
                                pass
                            case 4:
                                pass
                            case 5:
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
                                pass
                            case 2:
                                pass
                            case 3:
                                pass
                            case 4:
                                pass
                            case 5:
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
                                pass
                            case 2:
                                pass
                            case 3:
                                pass
                            case 4:
                                pass
                            case 5:
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
                                pass
                            case 2:
                                pass
                            case 3:
                                pass
                            case 4:
                                pass
                            case 5:
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
                                pass
                            case 2:
                                pass
                            case 3:
                                pass
                            case 4:
                                pass
                            case 5:
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
                                pass
                            case 3:
                                pass
                            case 4:
                                pass
                            case 5:
                                pass
                            case 6:
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
                                s = True
                            case _:
                                print("Opcion invalida")
                    except Exception as ex:
                        print(f"Ha ocurrido un error: {ex}")
            case 8:
                print("Gracias por usar el sistema")
                a = True
            case _:
                print("Opcion invalida")
    except Exception as ex:
        print(f"Ha ocurrido un error: {ex}")