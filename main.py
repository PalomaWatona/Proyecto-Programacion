from datetime import datetime
import os

def usuario():
    try:
        os.system("cls")
        rut = input("Ingrese el rut de la usuario: ")
        os.system("cls")
        while rut == "":
            print("El rut no puede quedar vacío")
            rut = input("Ingrese el rut de la usuario: ")

        nombre = input("Ingrese el nombre del usuario: ")
        while nombre == "":
            print("El nombre no puede quedar vacío")
            nombre = input("Ingrese el nombre del usuario: ")

        apellido_paterno = input("Ingrese el apellido paterno del usuario: ")
        while apellido_paterno == "":
            print("El apellido paterno no puede quedar vacío")
            apellido_paterno = input("Ingrese el apellido paterno del usuario: ")

        apellido_materno = input("Ingrese el apellido materno del usuario: ")
        while apellido_materno == "":
            print("El apellido materno no puede quedar vacío")
            apellido_materno = input("Ingrese el apellido materno del usuario: ")

        nacimiento = input("Ingrese la fecha de nacimiento (DD/MM/AAAA): ")
        while nacimiento == "":
            print("La fecha de nacimiento no puede quedar vacía")
            nacimiento = input("Ingrese la fecha de nacimiento (DD/MM/AAAA): ")
        fecha_nacimiento = datetime.strptime(nacimiento, "%d/%m/%Y").date()

        telefono = int(input("Ingrese el telefono del usuario: "))
        while telefono == "":
            print("El teléfono no puede quedar vacío")
            telefono = int(input("Ingrese el telefono del usuario: "))

        direccion = input("Ingrese la dirección del usuario: ")
        while direccion == "":
            print("La dirección no puede quedar vacía")
            os.system("pause")
            direccion = input("Ingrese la dirección del usuario: ")

        correo = input("Ingrese el correo del usuario: ")
        while correo == "":
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
        while patente == "":
            print("La patente no puede quedar vacía")
            patente = input("Ingrese la patente del vehiculo: ")
        chasis = int(input("Ingrese el número de chasis del vehiculo: "))
        while chasis == "":
            print("El número de chasis no puede quedar vacío")
            chasis = int(input("Ingrese el número de chasis del vehiculo: "))
        motor = int(input("Ingrese el número de motor del vehículo: "))
        while motor == "":
            print("El número de motor no puede quedar vacío")
            motor = int(input("Ingrese el número de motor del vehículo: "))
        marca = input("Ingrese la marca del vehíchulo: ")
        while marca == "":
            print("La marca no puede quedar vacía")
            marca = input("Ingrese la marca del vehíchulo: ")
        modelo = input("Ingrese el modelo del vehiculo: ")
        while modelo == "":
            print("El modelo no puede quedar vacío")
            modelo = input("Ingrese el modelo del vehiculo: ")
        color = input("Ingrese el color del vehiculo: ")
        while color == "":
            print("El color no puede quedar vacío")
            color = input("Ingrese el color del vehiculo: ")
        anio = int(input("Ingrese el año del vehiculo: "))
        while anio <= 0:
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
        while rut_agente == "":
            print("El rut no puede quedar vacío")
            rut_agente = input("Ingrese el rut del agente de ventas: ")
        id_poliza = int(input("Ingrese el identificador de su póliza: "))
        while id_poliza == "":
            print("El identificador de la póliza no puede quedar vacío")
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
        while valor_anual == "":
            print("El valor anual no puede quedar vacío")
            valor_anual = int(input("Ingrese el valor anual de su seguro: "))
        cobertura = int(input("Ingrese la cobertura maxima en años de su seguro: "))
        while cobertura == "":
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
        while numero_declaracion == "":
            print("El número de declaración no puede quedar vacío")
            numero_declaracion = int(input("Ingrese el numero de su declaración: "))
        informacion_siniestro = input("Ingrese información del siniestro: ")
        while informacion_siniestro == "":
            print("La información del siniestro no puede quedar vacía")
            informacion_siniestro = input("Ingrese información del siniestro: ")
        #PARA LA POLIZA DEL SEGURO SE DEBE VALIDAR CON LAS POLIZAS ACTIVAS, SI ES QUE SE DEJA PARA DESPUES
        rut_siniestrado = input("Ingrese el RUT del conductor siniestrado: ")
        while rut_siniestrado == "":
            print("El RUT del conductor siniestrado no puede quedar vacío")
            rut_siniestrado = input("Ingrese el RUT del conductor siniestrado: ")
        patente = input("Ingrese la patente asociada al vehiculo siniestrado: ")
        while patente == "":
            print("La patente no puede quedar vacía")
            patente = input("Ingrese la patente asociada al vehiculo siniestrado: ")
        while patente == "":
            print("La patente no puede quedar vacía")
            patente = input("Ingrese la patente asociada al vehiculo siniestrado: ")
        fecha = input("Ingrese la fecha de siniestro (DD/MM/AAAA): ")
        while fecha == "":
            print("La fecha de siniestro no puede quedar vacía")
            fecha = input("Ingrese la fecha de siniestro (DD/MM/AAAA): ")
        fecha_siniestro = datetime.strptime(fecha, "%d/%m/%Y").date()
        taller = input("Ingrese la dirección del taller: ")
        while taller == "":
            print("La dirección del taller no puede quedar vacía")
            taller = input("Ingrese la dirección del taller: ")
        fecha = input("Ingrese la fecha de reparación (DD/MM/AAAA): ")
        while fecha == "":
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
        print("Finalizó el programa por un error en el menú: ")
        os.system("pause")
        break 
