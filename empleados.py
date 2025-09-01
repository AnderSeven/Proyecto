from admin import Admin
class Empleado():
    def __init__(self, id_empleado, nombre, direccion, telefono, correo, puesto):
        self.id_empleado = id_empleado
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono
        self._correo = correo
        self._puesto = puesto

class registro_empleados():
    def __init__(self):
        self.diccionario_empleados = {}

    def registrar_empleados(self):
        s = False
        while s == False:
            try:
                cantidad = int(input("Ingrese la cantidad de empleados que desasea registrar: "))
                if cantidad > 0:
                    s = True
                else:
                    print("La cantidad debe de ser un numero entero mayor a cero")
            except Exception as ex:
                print(f"Ha ocurrido un error: {ex}")
        for i in range(cantidad):
            s = False
            print(f"\nEmpleado: #{i+1}")
            s = False
            while s == False:
                try:
                    id_empleado = int(input("Ingrese el id del empleado: "))
                    if id_empleado in self.diccionario_empleados:
                        print("El id ya este en uso, intente de nuevo")
                    else:
                        s = True
                except Exception as ex:
                    print(f"Ha ocurrido un error: {ex}")
            nombre = input("Ingrese el nombre del empleado: ").strip()
            direccion = input("Ingrese la direccion del empleado: ").strip()
            telefono = input("Ingrese el telefono del empleado: ").strip()
            correo = input("Ingrese el correo del empleado: ").strip()
            puesto = input("Ingrese el puesto del empleado: ").capitalize().strip()
            if puesto == "Admin":
                nuevo_empleado = Admin(id_empleado, nombre, direccion, telefono, correo)
            else:
                nuevo_empleado = Empleado(id_empleado, nombre, direccion, telefono, correo, puesto)
            self.diccionario_empleados[id_empleado] = nuevo_empleado
            print("Empleado registrado en el sistema")