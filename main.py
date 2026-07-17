from datetime import datetime
import os

def usuario():
    try:
        rut = input("Ingrese el rut de la usuario: ")
        os.system("cls")
        nombre = input("Ingrese el nombde de la usuario: ")
        apellido_paterno = input("Ingrese el apellido paterno de la usuario: ")
        apellido_materno = input("Ingrese el apellido materno de la usuario: ")
        nacimiento = input("Ingrese la fecha de nacimiento (DD/MM/AAAA): ")
        fecha_nacimiento = datetime.strptime(nacimiento, "%d/%m/%m").date()
        telefono = int(input("Ingrese el telefono del usuario: "))
        direccion = input("Ingrese la dirección del usuario: ")
        correo = input("Ingrese el correo del usuario: ")
        #HACER UN DICCIONARIO Y DEVOLVER TODO PARA ALMACENARLO
    except:
        os.system("cls")
        print("Error al momento de crear usuario")
        os.system("pause")

def vehiculo():
    try:
        #Hacer que se traigan los rut del diccionario de usuario para mostrarlos acá y dar a elegir
        patente = input("Ingrese la patente del vehiculo: ")
        chasis = int(input("Ingrese el número de chasis del vehiculo: "))
        motor = int(input("Ingrese el número de motor del vehículo: "))
        marca = input("Ingrese la marca del vehíchulo: ")
        modelo = input("Ingrese el modelo del vehiculo: ")
        color = input("Ingrese el color del vehiculo: ")
        anio = int(input("Ingrese el año del vehiculo: "))
    except:
        os.system("cls")
        print("Error al momento de crear vehiculo")
        os.system("pause")

def poliza():
    try:
        #HACER QUE SE SE TENGA QUE INGRESAR UN RUT VALIDO DE AGENTE DE VENTAS
        rut_agente = input("Ingrese el rut del agente de ventas: ")
        id_poliza = int(input("Ingrese el identificador de su póliza: "))
        #rut_usuario = VALIDAR CON RUT DE PERSONA
        os.system("cls")
        print("[1] Seguro automotriz")
        print("[2] Seguro de vida")
        opcion = int(input("Ingrese el tipo de seguro: "))
        if opcion ==  1:
            tipo_seguro = "automotriz"
        elif opcion == 2:
            tipo_seguro = "vida"

    except:
        os.system("cls")
        print("Error al momento de crear poliza")
        os.system("pause")

def siniestro():
    pass

#DEFINICIÓN DE VARIABLES A UTILIZAR
rut_agentes = [] #INVENTAR RUT DE AGENTES DE VENTA
rut_usuarios = [] #RUT DE USUARIOS QUE SE HAN INGRESADO

    #MENÚ PRINCIPAL
while True:
    os.system("cls")
    print("############################################################")
    print("[1] Registrar usuario")
    print("[2] Registrar vehiculo (Debe tener propietario)")
    print("[3] Registrar póliza (Debe existir usuario con vehiculo)")
    print("[4] Registrar siniestro (Debe existir vehiculo y póliza)")
    print("[5] Salir")
    print("############################################################")
    opcion = int(input("Ingrese su opción: "))

    if opcion == 1:
        usuario()
    elif opcion == 2:
        vehiculo()
    elif opcion == 3:
        poliza()
    elif opcion == 4:
        siniestro()
    else:
        break