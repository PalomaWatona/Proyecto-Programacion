from datetime import datetime
import os

def usuario():
    try:
        os.system("cls")
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

def vehiculo(usuarios): #EN PROCESO LA CREACION DE DICCIONARIO DE DATOS PARA ALMACENAR DATOS DE VEHICULOS (PROBVABLEMENTE EN OTRA FUNCION)
    try:
        os.system("cls")
        print("Usuarios disponibles: ")
        print(usuarios)
        rut_usuario = input("Ingrese el rut del usuario al que le pertenece el vehiculo: ")
        for i in usuarios:
            if rut_usuario == i:
                print("muy bien, el rut si existe :D")
                break
            else:
                print("rut invalido, volviendo a la creacion de vehiculo")
                os.system("pause")
                vehiculo(usuarios)

        patente = input("Ingrese la patente del vehiculo: ")
        chasis = int(input("Ingrese el número de chasis del vehiculo: "))
        motor = int(input("Ingrese el número de motor del vehículo: "))
        marca = input("Ingrese la marca del vehíchulo: ")
        modelo = input("Ingrese el modelo del vehiculo: ")
        color = input("Ingrese el color del vehiculo: ")
        anio = int(input("Ingrese el año del vehiculo: "))
        
        #CREAR REGISTRO Y GUARDARLO EN UN DICCIONARIO
        datos_vehiculo = {
            "rut_duenio": rut_usuario,
            "patente": patente,
            "chasis": chasis,
            "motor": motor,
            "marca": marca,
            "modelo": modelo,
            "color": color,
            "anio": anio
        }
        return datos_vehiculo
    except:
        os.system("cls")
        print("Error al momento de crear vehiculo")
        os.system("pause")

def poliza():
    try:
        os.system("cls")
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
        else:
            print("opcion invalida, redirigiendo a menu de creación de poliza")
            os.system("pause")
            poliza()
        valor_anual = int(input("Ingrese el valor anual de su seguro: "))
        cobertura = int(input("Ingrese la cobertura maxima en años de su seguro: "))

    except:
        os.system("cls")
        print("Error al momento de crear poliza")
        os.system("pause")

def siniestro():
    try:
        os.system("cls")
        numero_declaracion = int(input("Ingrese el numero de su declaración: "))
        informacion_siniestro = input("Ingrese información del siniestro: ")
        #PARA LA POLIZA DEL SEGURO SE DEBE VALIDAR CON LAS POLIZAS ACTIVAS, SI QUE SE DEJA PARA DESPUES
        rut_siniestrado = input("Ingrese el RUT del conductor siniestrado: ")
        patente = input("Ingrese la patente asociada al vehiculo siniestrado: ")
        fecha = input("Ingrese la fecha de nacimiento (DD/MM/AAAA): ")
        fecha_siniestro = datetime.strptime(fecha, "%d/%m/%m").date()
        taller = input("Ingrese la dirección del taller: ")
        fecha = input("Ingrese la fecha de nacimiento (DD/MM/AAAA): ")
        fecha_reparacion = datetime.strptime(fecha, "%d/%m/%m").date()
    except:
        os.system("cls")
        print("Error al momento de crear siniestro")
        os.system("pause")

#DEFINICIÓN DE VARIABLES A UTILIZAR
usuarios = {}
vehiculos = {}
polizas = {}
accidentes = {}

rut_agentes = [] #INVENTAR RUT DE AGENTES DE VENTA
rut_usuarios = ["00.000.000-0"] #RUT DE USUARIOS QUE SE HAN INGRESADO


    #MENÚ PRINCIPAL
while True:
    try:

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
            datos = vehiculo(rut_usuarios)

        elif opcion == 3:
            poliza()
        elif opcion == 4:
            siniestro()
        else:
            print("Gracias por utilizar el programa :D")
            os.system("pause")
            break
    except:
        print("Finalizó el programa por un error en el menú: ")
        os.system("pause")
        break 