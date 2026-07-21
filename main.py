from datetime import datetime
import os

def usuario():
    try:
        os.system("cls")
        rut = input("Ingrese el rut del usuario (sin puntos y sin guion): ")
        os.system("cls")
        while rut == "" or len(rut) < 8 or len(rut) > 9 or not rut.isdigit():
            print("El rut no puede quedar vacío, debe tener entre 8 y 9 dígitos")
            rut = input("Ingrese el rut del usuario: ")

        nombre = input("Ingrese el nombre del usuario: ")
        while nombre == "" or not nombre.isalpha():
            print("El nombre no puede quedar vacío")
            nombre = input("Ingrese el nombre del usuario: ")

        apellido_paterno = input("Ingrese el apellido paterno del usuario: ")
        while apellido_paterno == "" or not apellido_paterno.isalpha():
            print("El apellido paterno no puede quedar vacío")
            apellido_paterno = input("Ingrese el apellido paterno del usuario: ")

        apellido_materno = input("Ingrese el apellido materno del usuario: ")
        while apellido_materno == "" or not apellido_materno.isalpha():
            print("El apellido materno no puede quedar vacío")
            apellido_materno = input("Ingrese el apellido materno del usuario: ")

        nacimiento = input("Ingrese la fecha de nacimiento (DD/MM/AAAA): ")
        while nacimiento == "" or not datetime.strptime(nacimiento, "%d/%m/%Y"):
            print("La fecha de nacimiento no puede quedar vacía")
            nacimiento = input("Ingrese la fecha de nacimiento (DD/MM/AAAA): ")
        fecha_nacimiento = datetime.strptime(nacimiento, "%d/%m/%Y").date()

        telefono = int(input("Ingrese el telefono del usuario (9 dígitos): "))
        while telefono == "" or len(str(telefono)) != 9:
            print("El teléfono no puede quedar vacío y debe tener 9 dígitos")
            telefono = int(input("Ingrese el telefono del usuario (9 dígitos): "))

        direccion = input("Ingrese la dirección del usuario: ")
        while direccion == "" or not direccion.isalpha():
            print("La dirección no puede quedar vacía")
            os.system("pause")
            direccion = input("Ingrese la dirección del usuario: ")

        correo = input("Ingrese el correo del usuario: ")
        while correo == "" or "@" not in correo or "." not in correo:
            print("El correo no puede quedar vacío")
            os.system("pause")
            correo = input("Ingrese el correo del usuario: ")

        
        datos_usuario = {
            "rut": rut,
            "nombre": nombre,
            "apellido_paterno": apellido_paterno,
            "apellido_materno": apellido_materno,
            "fecha_nacimiento": fecha_nacimiento,
            "telefono": telefono,
            "direccion": direccion,
            "correo": correo
    }
        return datos_usuario
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
                print("Muy bien, el rut si existe :D")
                break
            else:
                print("rut invalido, volviendo a la creacion de vehiculo")
                os.system("pause")
                vehiculo(usuarios)
        patente = input("Ingrese la patente del vehiculo: ")
        while patente == "" or len(patente) < 6 or len(patente) > 7:
            print("La patente no puede quedar vacía")
            patente = input("Ingrese la patente del vehiculo: ")
        chasis = int(input("Ingrese el número de chasis del vehiculo: "))
        while chasis == "" or chasis <= 0 or len(str(chasis)) < 6 or len(str(chasis)) > 17:
            print("El número de chasis no puede quedar vacío")
            chasis = int(input("Ingrese el número de chasis del vehiculo: "))
        motor = int(input("Ingrese el número de motor del vehículo: "))
        while motor == "" or motor <= 0 or len(str(motor)) < 6 or len(str(motor)) > 17:
            print("El número de motor no puede quedar vacío")
            motor = int(input("Ingrese el número de motor del vehículo: "))
        marca = input("Ingrese la marca del vehíchulo: ")
        while marca == "" or not marca.isalpha():
            print("La marca no puede quedar vacía")
            marca = input("Ingrese la marca del vehíchulo: ")
        modelo = input("Ingrese el modelo del vehiculo: ")
        while modelo == "" or not modelo.isalpha():
            print("El modelo no puede quedar vacío")
            modelo = input("Ingrese el modelo del vehiculo: ")
        color = input("Ingrese el color del vehiculo: ")
        while color == "" or not color.isalpha():
            print("El color no puede quedar vacío")
            color = input("Ingrese el color del vehiculo: ")
        anio = int(input("Ingrese el año del vehiculo: "))
        while anio <= 0 or anio > datetime.now().year:
            print("El año no puede ser negativo o cero")
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
        while rut_agente == "" or len(rut_agente) < 8 or len(rut_agente) > 9 or not rut_agente.isdigit():
            print("El rut no puede quedar vacío")
            rut_agente = input("Ingrese el rut del agente de ventas: ")
        id_poliza = int(input("Ingrese el identificador de su póliza: "))
        while id_poliza == "" or id_poliza <= 0 or len(str(id_poliza)) < 1:
            print("El identificador de la póliza no puede quedar vacío")
            id_poliza = int(input("Ingrese el identificador de su póliza: "))
        rut_usuario = input("Ingrese el rut del usuario (sin puntos y sin guion): ")
        os.system("cls")
        while rut_usuario == "" or len(rut_usuario) < 8 or len(rut_usuario) > 9 or not rut_usuario.isdigit():
            print("El rut no puede quedar vacío, debe tener entre 8 y 9 dígitos")
            rut_usuario = input("Ingrese el rut del usuario: ")
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
        patente = int(input("Ingrese la patente del vehiculo asegurado: "))
        while patente == "" or patente <= 0 or len(str(patente)) < 1:
            print("La patente del vehiculo asegurado no puede quedar vacío")
        
        valor_anual = int(input("Ingrese el valor anual de su seguro: "))
        while valor_anual == "" or valor_anual <= 0 or len(str(valor_anual)) < 1:
            print("El valor anual no puede quedar vacío")
            valor_anual = int(input("Ingrese el valor anual de su seguro: "))
        cobertura = int(input("Ingrese la cobertura maxima en años de su seguro: "))
        while cobertura == "" or cobertura <= 0 or len(str(cobertura)) < 1:
            print("La cobertura no puede quedar vacía")
            cobertura = int(input("Ingrese la cobertura maxima en años de su seguro: "))

            datos_poliza = {
                "rut_agente": rut_agente,
                "id_poliza": id_poliza,
                "tipo_seguro": tipo_seguro,
                "valor_anual": valor_anual,
                "cobertura": cobertura
                }
            return datos_poliza
    except:
        os.system("cls")
        print("Error al momento de crear poliza")
        os.system("pause")

        


def siniestro():
    try:
        os.system("cls")
        numero_declaracion = int(input("Ingrese el numero de su declaración: "))
        while numero_declaracion == "" or numero_declaracion <= 0 or len(str(numero_declaracion)) < 1:
            print("El número de declaración no puede quedar vacío")
            numero_declaracion = int(input("Ingrese el numero de su declaración: "))
        informacion_siniestro = input("Ingrese información del siniestro: ")
        while informacion_siniestro == "":
            print("La información del siniestro no puede quedar vacía")
        poliza_asociada = input("Ingrese la poliza de seguro asociada al siniestro: ")
        while poliza_asociada == "":
            print("La pooliza del seguro no puede quedar vacía")
            informacion_siniestro = input("Ingrese la poliza del seguro asociado: ")
        #PARA LA POLIZA DEL SEGURO SE DEBE VALIDAR CON LAS POLIZAS ACTIVAS, SI ES QUE SE DEJA PARA DESPUES
        rut_siniestrado = input("Ingrese el RUT del conductor siniestrado: ")
        while rut_siniestrado == "" or len(rut_siniestrado) < 8 or len(rut_siniestrado) > 9 or not rut_siniestrado.isdigit():
            print("El RUT del conductor siniestrado no puede quedar vacío")
            rut_siniestrado = input("Ingrese el RUT del conductor siniestrado: ")
        patente = input("Ingrese la patente asociada al vehiculo siniestrado: ")
        while patente == "" or len(patente) < 6 or len(patente) > 7:
            print("La patente no puede quedar vacía")
            patente = input("Ingrese la patente asociada al vehiculo siniestrado: ")
        while patente == "" or len(patente) < 6 or len(patente) > 7:
            print("La patente no puede quedar vacía")
            patente = input("Ingrese la patente asociada al vehiculo siniestrado: ")
        fecha = input("Ingrese la fecha de siniestro (DD/MM/AAAA): ")
        while fecha == "" or not datetime.strptime(fecha, "%d/%m/%Y"):
            print("La fecha de siniestro no puede quedar vacía")
            fecha = input("Ingrese la fecha de siniestro (DD/MM/AAAA): ")
        fecha_siniestro = datetime.strptime(fecha, "%d/%m/%Y").date()
        taller = input("Ingrese la dirección del taller: ")
        while taller == "" or not taller.isalpha():
            print("La dirección del taller no puede quedar vacía")
            taller = input("Ingrese la dirección del taller: ")
        fecha = input("Ingrese la fecha de reparación (DD/MM/AAAA): ")
        while fecha == "" or not datetime.strptime(fecha, "%d/%m/%Y"):
            print("La fecha de reparación no puede quedar vacía")
            fecha = input("Ingrese la fecha de reparación (DD/MM/AAAA): ")
        fecha_reparacion = datetime.strptime(fecha, "%d/%m/%Y").date()
        
        datos_siniestro = {
    "numero_declaracion": numero_declaracion,
    "informacion_siniestro": informacion_siniestro,
    "rut_siniestrado": rut_siniestrado,
    "patente": patente,
    "fecha_siniestro": fecha_siniestro,
    "taller": taller,
    "fecha_reparacion": fecha_reparacion
}
        return datos_siniestro
        
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
    print("############################################################")
    print("[1] Registrar usuario")
    print("[2] Registrar vehiculo (Debe tener propietario)")
    print("[3] Registrar póliza (Debe existir usuario con vehiculo)")
    print("[4] Registrar siniestro (Debe existir vehiculo y póliza)")
    print("[5] Salir")
    print("############################################################")
    
    try:
        os.system("cls")
        opcion = int(input("Ingrese su opción: "))
        os.system("cls")
    except ValueError:
        print("\n¡Error! Debes ingresar un número entero.")
        input("Presiona Enter para reintentar...")
        continue

    if opcion == 1:
        usuario()
    elif opcion == 2:
        datos = vehiculo(rut_usuarios)
    elif opcion == 3:
        poliza()
    elif opcion == 4:
        siniestro()
    elif opcion == 5:
        print("\nGracias por utilizar el programa :D")
        input("Presiona Enter para salir...")
        break
    else:
        print("\nOpción no válida. Elige un número del 1 al 5.")
        input("Presiona Enter para reintentar...")