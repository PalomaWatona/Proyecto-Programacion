from datetime import datetime
import os

# ============================================================
# MÓDULOS DE REGISTRO
# ============================================================

def usuario(usuarios):
    """Registra un nuevo usuario (cliente) validando cada campo."""
    try:
        os.system("cls")
        rut = input("Ingrese el rut del usuario (sin puntos y sin guion): ")
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

        # Fecha de nacimiento: control de excepciones para formato inválido
        fecha_valida = False
        while not fecha_valida:
            nacimiento = input("Ingrese la fecha de nacimiento (DD/MM/AAAA): ")
            try:
                fecha_nacimiento = datetime.strptime(nacimiento, "%d/%m/%Y").date()
                fecha_valida = True
            except ValueError:
                print("Formato de fecha inválido, debe ser DD/MM/AAAA")

        # Teléfono: control de excepciones para valores no numéricos
        telefono_valido = False
        while not telefono_valido:
            try:
                telefono = int(input("Ingrese el teléfono del usuario (9 dígitos): "))
                if len(str(telefono)) != 9:
                    print("El teléfono debe tener 9 dígitos")
                else:
                    telefono_valido = True
            except ValueError:
                print("El teléfono debe ser un valor numérico")

        direccion = input("Ingrese la dirección del usuario: ")
        while direccion == "":
            print("La dirección no puede quedar vacía")
            direccion = input("Ingrese la dirección del usuario: ")

        correo = input("Ingrese el correo del usuario: ")
        while correo == "" or "@" not in correo or "." not in correo:
            print("El correo no puede quedar vacío y debe tener un formato válido")
            correo = input("Ingrese el correo del usuario: ")

        usuarios[rut] = {
            "rut": rut,
            "nombre": nombre,
            "apellido_paterno": apellido_paterno,
            "apellido_materno": apellido_materno,
            "fecha_nacimiento": fecha_nacimiento,
            "telefono": telefono,
            "direccion": direccion,
            "correo": correo
        }
        print(f"\nUsuario {nombre} {apellido_paterno} registrado con éxito.")
        os.system("pause")
        return usuarios
    except Exception as error:
        os.system("cls")
        print(f"Error al momento de crear usuario: {error}")
        os.system("pause")
        return usuarios


def vehiculo(usuarios, vehiculos):
    """Registra un vehículo asociado a un usuario ya existente."""
    try:
        os.system("cls")
        if not usuarios:
            print("No hay usuarios registrados. Debe registrar un usuario primero.")
            os.system("pause")
            return vehiculos

        print("Usuarios disponibles (RUT):")
        print(list(usuarios.keys()))

        rut_usuario = input("Ingrese el rut del usuario al que pertenece el vehículo: ")
        while rut_usuario not in usuarios:
            print("El rut ingresado no está registrado como usuario")
            rut_usuario = input("Ingrese el rut del usuario al que pertenece el vehículo: ")

        patente = input("Ingrese la patente del vehículo: ")
        while patente == "" or len(patente) < 6 or len(patente) > 7:
            print("La patente debe tener entre 6 y 7 caracteres")
            patente = input("Ingrese la patente del vehículo: ")

        # Número de chasis con control de excepciones
        chasis_valido = False
        while not chasis_valido:
            try:
                chasis = int(input("Ingrese el número de chasis del vehículo: "))
                if chasis <= 0 or len(str(chasis)) < 6 or len(str(chasis)) > 17:
                    print("El número de chasis debe tener entre 6 y 17 dígitos")
                else:
                    chasis_valido = True
            except ValueError:
                print("El número de chasis debe ser numérico")

        # Número de motor con control de excepciones
        motor_valido = False
        while not motor_valido:
            try:
                motor = int(input("Ingrese el número de motor del vehículo: "))
                if motor <= 0 or len(str(motor)) < 6 or len(str(motor)) > 17:
                    print("El número de motor debe tener entre 6 y 17 dígitos")
                else:
                    motor_valido = True
            except ValueError:
                print("El número de motor debe ser numérico")

        marca = input("Ingrese la marca del vehículo: ")
        while marca == "" or not marca.isalpha():
            print("La marca no puede quedar vacía")
            marca = input("Ingrese la marca del vehículo: ")

        modelo = input("Ingrese el modelo del vehículo: ")
        while modelo == "":
            print("El modelo no puede quedar vacío")
            modelo = input("Ingrese el modelo del vehículo: ")

        color = input("Ingrese el color del vehículo: ")
        while color == "" or not color.isalpha():
            print("El color no puede quedar vacío")
            color = input("Ingrese el color del vehículo: ")

        # Año con control de excepciones
        anio_valido = False
        while not anio_valido:
            try:
                anio = int(input("Ingrese el año del vehículo: "))
                if anio <= 0 or anio > datetime.now().year:
                    print("El año no puede ser negativo, cero o mayor al actual")
                else:
                    anio_valido = True
            except ValueError:
                print("El año debe ser un valor numérico")

        vehiculos[patente] = {
            "rut_duenio": rut_usuario,
            "patente": patente,
            "chasis": chasis,
            "motor": motor,
            "marca": marca,
            "modelo": modelo,
            "color": color,
            "anio": anio
        }
        print(f"\nVehículo con patente {patente} registrado con éxito.")
        os.system("pause")
        return vehiculos
    except Exception as error:
        os.system("cls")
        print(f"Error al momento de crear vehículo: {error}")
        os.system("pause")
        return vehiculos


def poliza(usuarios, vehiculos, polizas):
    """Registra una póliza asociada a un usuario y a un vehículo ya existentes."""
    try:
        os.system("cls")
        rut_agente = input("Ingrese el rut del agente de ventas: ")
        while rut_agente == "" or len(rut_agente) < 8 or len(rut_agente) > 9 or not rut_agente.isdigit():
            print("El rut del agente debe tener entre 8 y 9 dígitos")
            rut_agente = input("Ingrese el rut del agente de ventas: ")

        # ID de póliza con control de excepciones
        id_valido = False
        while not id_valido:
            try:
                id_poliza = int(input("Ingrese el identificador de la póliza: "))
                if id_poliza <= 0:
                    print("El identificador debe ser un número positivo")
                elif id_poliza in polizas:
                    print("Ya existe una póliza registrada con ese identificador")
                else:
                    id_valido = True
            except ValueError:
                print("El identificador debe ser numérico")

        if not usuarios:
            print("No hay usuarios registrados. Debe registrar un usuario primero.")
            os.system("pause")
            return polizas

        rut_usuario = input("Ingrese el rut del usuario contratante: ")
        while rut_usuario not in usuarios:
            print("El rut ingresado no corresponde a un usuario registrado")
            rut_usuario = input("Ingrese el rut del usuario contratante: ")

        # Tipo de seguro con control de excepciones
        tipo_valido = False
        while not tipo_valido:
            os.system("cls")
            print("[1] Seguro automotriz")
            print("[2] Seguro de vida")
            try:
                opcion = int(input("Ingrese el tipo de seguro: "))
                if opcion == 1:
                    tipo_seguro = "Automotriz"
                    tipo_valido = True
                elif opcion == 2:
                    tipo_seguro = "Vida"
                    tipo_valido = True
                else:
                    print("Opción inválida, elige 1 o 2")
                    os.system("pause")
            except ValueError:
                print("Debe ingresar un número")
                os.system("pause")

        if not vehiculos:
            print("No hay vehículos registrados. Debe registrar un vehículo primero.")
            os.system("pause")
            return polizas

        patente = input("Ingrese la patente del vehículo asegurado: ")
        while patente not in vehiculos:
            print("La patente ingresada no corresponde a un vehículo registrado")
            patente = input("Ingrese la patente del vehículo asegurado: ")

        # Valor anual con control de excepciones
        valor_valido = False
        while not valor_valido:
            try:
                valor_anual = int(input("Ingrese el valor anual de la póliza: "))
                if valor_anual <= 0:
                    print("El valor anual debe ser positivo")
                else:
                    valor_valido = True
            except ValueError:
                print("El valor anual debe ser numérico")

        # Cobertura con control de excepciones
        cobertura_valida = False
        while not cobertura_valida:
            try:
                cobertura = int(input("Ingrese la cobertura máxima de la póliza: "))
                if cobertura <= 0:
                    print("La cobertura debe ser positiva")
                else:
                    cobertura_valida = True
            except ValueError:
                print("La cobertura debe ser numérica")

        polizas[id_poliza] = {
            "rut_agente": rut_agente,
            "id_poliza": id_poliza,
            "rut_usuario": rut_usuario,
            "tipo_seguro": tipo_seguro,
            "patente": patente,
            "valor_anual": valor_anual,
            "cobertura": cobertura,
            "estado": "Vigente"
        }
        print(f"\nPóliza N° {id_poliza} registrada con éxito.")
        os.system("pause")
        return polizas
    except Exception as error:
        os.system("cls")
        print(f"Error al momento de crear póliza: {error}")
        os.system("pause")
        return polizas


def siniestro(usuarios, vehiculos, polizas, siniestros):
    """Registra un siniestro asociado a un usuario, vehículo y póliza existentes."""
    try:
        os.system("cls")

        # Número de declaración con control de excepciones
        num_valido = False
        while not num_valido:
            try:
                numero_declaracion = int(input("Ingrese el número de declaración del siniestro: "))
                if numero_declaracion <= 0:
                    print("El número de declaración debe ser positivo")
                else:
                    num_valido = True
            except ValueError:
                print("El número de declaración debe ser numérico")

        informacion_siniestro = input("Ingrese información del siniestro: ")
        while informacion_siniestro == "":
            print("La información del siniestro no puede quedar vacía")
            informacion_siniestro = input("Ingrese información del siniestro: ")

        if not polizas:
            print("No hay pólizas registradas. Debe registrar una póliza primero.")
            os.system("pause")
            return siniestros

        # ID de póliza asociada con control de excepciones
        poliza_valida = False
        while not poliza_valida:
            try:
                poliza_asociada = int(input("Ingrese el ID de la póliza asociada al siniestro: "))
                if poliza_asociada not in polizas:
                    print("No existe una póliza registrada con ese ID")
                else:
                    poliza_valida = True
            except ValueError:
                print("El ID de la póliza debe ser numérico")

        rut_siniestrado = input("Ingrese el RUT del conductor siniestrado: ")
        while rut_siniestrado == "" or len(rut_siniestrado) < 8 or len(rut_siniestrado) > 9 or not rut_siniestrado.isdigit():
            print("El RUT debe tener entre 8 y 9 dígitos")
            rut_siniestrado = input("Ingrese el RUT del conductor siniestrado: ")

        patente = input("Ingrese la patente del vehículo siniestrado: ")
        while patente not in vehiculos:
            print("La patente ingresada no corresponde a un vehículo registrado")
            patente = input("Ingrese la patente del vehículo siniestrado: ")

        fecha_valida = False
        while not fecha_valida:
            fecha = input("Ingrese la fecha del siniestro (DD/MM/AAAA): ")
            try:
                fecha_siniestro = datetime.strptime(fecha, "%d/%m/%Y").date()
                fecha_valida = True
            except ValueError:
                print("Formato de fecha inválido, debe ser DD/MM/AAAA")

        taller = input("Ingrese la dirección del taller: ")
        while taller == "":
            print("La dirección del taller no puede quedar vacía")
            taller = input("Ingrese la dirección del taller: ")

        fecha_rep_valida = False
        while not fecha_rep_valida:
            fecha_rep = input("Ingrese la fecha estimada de reparación (DD/MM/AAAA): ")
            try:
                fecha_reparacion = datetime.strptime(fecha_rep, "%d/%m/%Y").date()
                fecha_rep_valida = True
            except ValueError:
                print("Formato de fecha inválido, debe ser DD/MM/AAAA")

        siniestros[numero_declaracion] = {
            "numero_declaracion": numero_declaracion,
            "informacion_siniestro": informacion_siniestro,
            "poliza_asociada": poliza_asociada,
            "rut_siniestrado": rut_siniestrado,
            "patente": patente,
            "fecha_siniestro": fecha_siniestro,
            "taller": taller,
            "fecha_reparacion": fecha_reparacion
        }
        print(f"\nSiniestro N° {numero_declaracion} registrado con éxito.")
        os.system("pause")
        return siniestros
    except Exception as error:
        os.system("cls")
        print(f"Error al momento de crear siniestro: {error}")
        os.system("pause")
        return siniestros


# ============================================================
# MÓDULOS DE CONSULTA (nuevas funcionalidades de esta entrega)
# ============================================================

def consultar_vehiculo_por_patente(vehiculos, usuarios):
    """Busca un vehículo por su patente y muestra sus datos
    junto con el nombre del propietario."""
    os.system("cls")
    print("7. Consultar vehículo por patente\n")

    if not vehiculos:
        print("No hay vehículos registrados en el sistema.")
        os.system("pause")
        return

    try:
        patente = input("Ingrese la patente: ").strip().upper()
        vehiculo_encontrado = vehiculos.get(patente)

        if vehiculo_encontrado is None:
            print(f"\nNo se encontró ningún vehículo con la patente {patente}")
        else:
            propietario_rut = vehiculo_encontrado["rut_duenio"]
            propietario = usuarios.get(propietario_rut)
            nombre_propietario = (
                f"{propietario['nombre']} {propietario['apellido_paterno']}"
                if propietario else "Desconocido"
            )

            print(f"\nPatente: {vehiculo_encontrado['patente']}")
            print(f"Marca: {vehiculo_encontrado['marca']}")
            print(f"Modelo: {vehiculo_encontrado['modelo']}")
            print(f"Año: {vehiculo_encontrado['anio']}")
            print(f"Propietario: {nombre_propietario}")
    except Exception as error:
        print(f"Error al momento de realizar la consulta: {error}")

    os.system("pause")


def consultar_poliza(polizas):
    """Busca una póliza por su ID y muestra sus datos principales."""
    os.system("cls")
    print("8. Consultar póliza\n")

    if not polizas:
        print("No hay pólizas registradas en el sistema.")
        os.system("pause")
        return

    try:
        id_poliza = int(input("Ingrese el ID de la póliza: "))
        poliza_encontrada = polizas.get(id_poliza)

        if poliza_encontrada is None:
            print(f"\nNo se encontró ninguna póliza con el ID {id_poliza}")
        else:
            valor_formateado = f"${poliza_encontrada['valor_anual']:,}".replace(",", ".")
            cobertura_formateada = f"${poliza_encontrada['cobertura']:,}".replace(",", ".")

            print(f"\nTipo de seguro: {poliza_encontrada['tipo_seguro']}")
            print(f"Valor anual: {valor_formateado}")
            print(f"Cobertura: {cobertura_formateada}")
            print(f"Estado: {poliza_encontrada['estado']}")
    except ValueError:
        print("\nEl ID de la póliza debe ser un valor numérico")
    except Exception as error:
        print(f"Error al momento de realizar la consulta: {error}")

    os.system("pause")


def listar_usuarios(usuarios):
    """Lista paginada de todos los usuarios registrados."""
    os.system("cls")

    if not usuarios:
        print("==========================================================")
        print("           NO HAY USUARIOS REGISTRADOS EN EL SISTEMA       ")
        print("==========================================================")
        os.system("pause")
        return

    lista_ruts = list(usuarios.keys())
    registros_por_pagina = 5
    total_registros = len(lista_ruts)

    for i in range(0, total_registros, registros_por_pagina):
        os.system("cls")
        pagina_actual = (i // registros_por_pagina) + 1
        total_paginas = (total_registros + registros_por_pagina - 1) // registros_por_pagina

        print("==========================================================")
        print(f"        LISTADO DE USUARIOS (Página {pagina_actual} de {total_paginas})")
        print(f"        Total registrados: {total_registros}")
        print("==========================================================")

        bloque = lista_ruts[i: i + registros_por_pagina]
        for num, rut in enumerate(bloque, start=i + 1):
            datos = usuarios[rut]
            nombre_completo = f"{datos['nombre']} {datos['apellido_paterno']} {datos['apellido_materno']}"
            fecha_str = datos['fecha_nacimiento'].strftime('%d/%m/%Y')

            print(f"[{num}] RUT: {datos['rut']}")
            print(f"    Nombre:    {nombre_completo}")
            print(f"    Nacimiento:{fecha_str}")
            print(f"    Teléfono:  +56 {datos['telefono']}")
            print(f"    Dirección: {datos['direccion']}")
            print(f"    Correo:    {datos['correo']}")
            print("-" * 58)

        if i + registros_por_pagina < total_registros:
            input("\nPresione ENTER para ver la siguiente página...")

    print("\nFin del listado.")
    os.system("pause")


# ============================================================
# VARIABLES GLOBALES DEL SISTEMA
# ============================================================
usuarios = {}
vehiculos = {}
polizas = {}
siniestros = {}

# ============================================================
# MENÚ PRINCIPAL
# ============================================================
while True:
    print("############################################################")
    print("#########################REGISTROS##########################")
    print("[1] Registrar usuario")
    print("[2] Registrar vehículo (Debe tener propietario)")
    print("[3] Registrar póliza (Debe existir usuario con vehículo)")
    print("[4] Registrar siniestro (Debe existir vehículo y póliza)")
    print("")
    print("#########################CONSULTAS###########################")
    print("[5] Listar usuarios")
    print("[6] Consultar vehículo por patente")
    print("[7] Consultar póliza")
    print("")
    print("[0] Salir")
    print("############################################################")

    try:
        opcion = int(input("Ingrese su opción: "))
        os.system("cls")
    except ValueError:
        print("\n¡Error! Debes ingresar un número entero.")
        input("Presiona Enter para reintentar...")
        continue

    if opcion == 1:
        usuarios = usuario(usuarios)
    elif opcion == 2:
        vehiculos = vehiculo(usuarios, vehiculos)
    elif opcion == 3:
        polizas = poliza(usuarios, vehiculos, polizas)
    elif opcion == 4:
        siniestros = siniestro(usuarios, vehiculos, polizas, siniestros)
    elif opcion == 5:
        listar_usuarios(usuarios)
    elif opcion == 6:
        consultar_vehiculo_por_patente(vehiculos, usuarios)
    elif opcion == 7:
        consultar_poliza(polizas)
    elif opcion == 0:
        print("\nGracias por utilizar el programa :D")
        input("Presiona Enter para salir...")
        break
    else:
        print("\nOpción no válida. Elige un número del 0 al 7.")
        input("Presiona Enter para reintentar...")
