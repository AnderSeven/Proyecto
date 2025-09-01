class Cliente():
    def __init__(self, nit, nombre, direccion, telefono, correo):
        self.nit = nit
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono
        self._correo = correo

class registro_clientes():
    def __init__(self):
        self.diccionario_clientes = {}

    def registrar_clientes(self):
        s = False
        while s == False:
            cantidad = int(input("Ingrese la cantidad de clientes que desasea registrar: "))
            if  cantidad <= 0:
                print("La cantidad debe de ser un numero entero mayor a cero")
            else:
                 s = True
            for i in range(cantidad):
                s = False
                print(f"Cliente: #{i+1}")
                while s == False:
                    try:
                        nit = int(input("Ingrese el nit del cliente: "))
                        if nit in self.diccionario_clientes:
                            print("El nit ya este en uso, intente de nuevo")
                        else:
                            s = True
                    except Exception as ex:
                        print(f"Ha ocurrido un error: {ex}")
                nombre = input("Ingrese el nombre del cliente: ").strip()
                direccion = input("Ingrese la direccion del cliente: ").strip()
                telefono = input("Ingrese el telefono del cliente: ").strip()
                correo = input("Ingrese el correo del cliente: ").strip()
                self.diccionario_clientes[nit] = Cliente(nit, nombre, direccion, telefono, correo)

    def registrar_un_solo_cliente(self, nit, nombre, direccion, telefono, correo):
        self.diccionario_clientes[nit] = Cliente(nit, nombre, direccion, telefono, correo)
        print("Cliente registrado en el sistema. ")