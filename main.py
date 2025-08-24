from menus import Menus
menu = Menus()

opcion = 0
a = False
while a == False:
    menu.menu_principal()
    opcion = int(input("Ingrese una opcion: "))
    match opcion:
        case 1:
            s = False
            while s == False:
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
        case 2:
            s = False
            while s == False:
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
        case 3:
            s = False
            while s == False:
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
        case 4:
            s = False
            while s == False:
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
        case 5:
            s = False
            while s == False:
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
        case 6:
            s = False
            while s == False:
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
        case 7:
            s = False
            while s == False:
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
        case 8:
            print("Gracias por usar el sistema")
            a = True
        case _:
            print("Opcion invalida")