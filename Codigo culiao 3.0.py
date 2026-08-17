from datetime import datetime
import calendar
import os

# ============================================================
# COLORES Y ESTILOS PARA LA INTERFAZ
# ============================================================
C_CYAN = '\033[96m'
C_GREEN = '\033[92m'
C_YELLOW = '\033[93m'
C_RED = '\033[91m'
C_BLUE = '\033[94m'
C_RESET = '\033[0m'
C_BOLD = '\033[1m'

# ============================================================
# CONFIGURACIÓN FINANCIERA (UF)
# ============================================================
VALOR_UF_HOY = 40851.38

def uf_a_clp(uf):
    """Convierte UF a pesos chilenos y redondea al entero más cercano."""
    return int(round(uf * VALOR_UF_HOY))

def formato_clp(valor_pesos):
    """Aplica formato de separador de miles con puntos para CLP."""
    return f"${valor_pesos:,}".replace(",", ".")

# ============================================================
# UTILIDADES
# ============================================================

def limpiar_consola():
    """Limpia la pantalla de la consola independientemente del sistema operativo."""
    if os.name == 'nt':
        os.system('') # Habilita secuencias ANSI en CMD/PowerShell
        os.system('cls') # Para Windows
    else:
        os.system('clear') # Para Linux/Mac

def mostrar_encabezado(titulo, mostrar_uf=False):
    """Muestra un marco superior estandarizado para las pantallas de datos."""
    limpiar_consola()
    texto_centrado = titulo.center(58)
    print(f"{C_BLUE}╔════════════════════════════════════════════════════════════╗{C_RESET}")
    print(f"{C_BLUE}║{C_CYAN}{C_BOLD}{texto_centrado}{C_RESET}{C_BLUE}  ║{C_RESET}")
    print(f"{C_BLUE}╚════════════════════════════════════════════════════════════╝{C_RESET}\n")
    if mostrar_uf:
        uf_fmt = f"{VALOR_UF_HOY:,.2f}".replace(",", "@").replace(".", ",").replace("@", ".")
        print(f"  {C_CYAN}[i] Valor UF de hoy: ${uf_fmt}{C_RESET}\n")


# ============================================================
# 1. MÓDULOS DE REGISTRO
# ============================================================

def usuario(usuarios):
    try:
        mostrar_encabezado("REGISTRO DE NUEVO CLIENTE")
        print(f"{C_YELLOW}Complete los siguientes datos:{C_RESET}\n")

        rut = input(f"  {C_GREEN}[+]{C_RESET} Ingrese el RUT (sin puntos y sin guion): ")
        while rut == "" or len(rut) < 8 or len(rut) > 9 or not rut.isdigit():
            mostrar_encabezado("REGISTRO DE NUEVO CLIENTE")
            print(f"      {C_RED}[!] Error: El RUT debe tener entre 8 y 9 dígitos.{C_RESET}")
            rut = input(f"  {C_GREEN}[+]{C_RESET} Ingrese el RUT nuevamente: ")

        nombre = input(f"  {C_GREEN}[+]{C_RESET} Ingrese el nombre: ")
        while nombre == "" or not nombre.isalpha():
            mostrar_encabezado("REGISTRO DE NUEVO CLIENTE")
            print(f"      {C_RED}[!] Error: El nombre no puede quedar vacío y debe contener solo letras.{C_RESET}")
            nombre = input(f"  {C_GREEN}[+]{C_RESET} Ingrese el nombre: ")

        apellido_paterno = input(f"  {C_GREEN}[+]{C_RESET} Ingrese el apellido paterno: ")
        while apellido_paterno == "" or not apellido_paterno.isalpha():
            mostrar_encabezado("REGISTRO DE NUEVO CLIENTE")
            print(f"      {C_RED}[!] Error: El apellido paterno no puede quedar vacío y debe ser solo letras.{C_RESET}")
            apellido_paterno = input(f"  {C_GREEN}[+]{C_RESET} Ingrese el apellido paterno: ")

        apellido_materno = input(f"  {C_GREEN}[+]{C_RESET} Ingrese el apellido materno: ")
        while apellido_materno == "" or not apellido_materno.isalpha():
            mostrar_encabezado("REGISTRO DE NUEVO CLIENTE")
            print(f"      {C_RED}[!] Error: El apellido materno no puede quedar vacío y debe ser solo letras.{C_RESET}")
            apellido_materno = input(f"  {C_GREEN}[+]{C_RESET} Ingrese el apellido materno: ")

        fecha_valida = False
        while not fecha_valida:
            nacimiento = input(f"  {C_GREEN}[+]{C_RESET} Ingrese la fecha de nacimiento (DD/MM/AAAA): ")
            try:
                fecha_nacimiento = datetime.strptime(nacimiento, "%d/%m/%Y").date()
                fecha_valida = True
            except ValueError:
                mostrar_encabezado("REGISTRO DE NUEVO CLIENTE")
                print(f"      {C_RED}[!] Error: Formato de fecha inválido, debe ser DD/MM/AAAA.{C_RESET}")

        telefono_valido = False
        while not telefono_valido:
            try:
                telefono = int(input(f"  {C_GREEN}[+]{C_RESET} Ingrese el teléfono (9 dígitos): "))
                if len(str(telefono)) != 9:
                    mostrar_encabezado("REGISTRO DE NUEVO CLIENTE")
                    print(f"      {C_RED}[!] Error: El teléfono debe tener exactamente 9 dígitos.{C_RESET}")
                else:
                    telefono_valido = True
            except ValueError:
                mostrar_encabezado("REGISTRO DE NUEVO CLIENTE")
                print(f"      {C_RED}[!] Error: El teléfono debe ser un valor numérico.{C_RESET}")

        direccion = input(f"  {C_GREEN}[+]{C_RESET} Ingrese la dirección: ")
        while direccion == "":
            mostrar_encabezado("REGISTRO DE NUEVO CLIENTE")
            print(f"      {C_RED}[!] Error: La dirección no puede quedar vacía.{C_RESET}")
            direccion = input(f"  {C_GREEN}[+]{C_RESET} Ingrese la dirección: ")

        correo = input(f"  {C_GREEN}[+]{C_RESET} Ingrese el correo electrónico: ")
        while correo == "" or "@" not in correo or "." not in correo:
            mostrar_encabezado("REGISTRO DE NUEVO CLIENTE")
            print(f"      {C_RED}[!] Error: El correo debe tener un formato válido.{C_RESET}")
            correo = input(f"  {C_GREEN}[+]{C_RESET} Ingrese el correo electrónico: ")
        
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

        print(f"\n{C_GREEN}══════════════════════════════════════════════════════════════{C_RESET}")
        print(f" {C_GREEN}[✓] ¡Cliente {nombre.upper()} {apellido_paterno.upper()} registrado con éxito!{C_RESET}")
        print(f"{C_GREEN}══════════════════════════════════════════════════════════════{C_RESET}\n")
        input(f"{C_BOLD}Presione Enter para continuar...{C_RESET}")
        return usuarios
    except Exception as error:
        print(f"\n{C_RED}  [!] Error al momento de crear cliente: {error}{C_RESET}")
        input(f"\n{C_BOLD}Presione Enter para continuar...{C_RESET}")
        return usuarios

def vehiculo(usuarios, vehiculos):
    try:
        mostrar_encabezado("REGISTRO DE VEHÍCULO")
        
        if not usuarios:
            print(f"  {C_RED}[!] No hay clientes registrados. Debe registrar un cliente primero.{C_RESET}")
            input(f"\n{C_BOLD}Presione Enter para continuar...{C_RESET}")
            return vehiculos

        print(f"{C_YELLOW}Clientes disponibles (RUT):{C_RESET} {list(usuarios.keys())}\n")

        rut_usuario = input(f"  {C_GREEN}[+]{C_RESET} Ingrese el RUT del propietario: ")
        while rut_usuario not in usuarios:
            mostrar_encabezado("REGISTRO DE VEHÍCULO")
            print(f"      {C_RED}[!] Error: El RUT ingresado no está registrado.{C_RESET}")
            rut_usuario = input(f"  {C_GREEN}[+]{C_RESET} Ingrese el RUT del propietario: ")

        patente = input(f"  {C_GREEN}[+]{C_RESET} Ingrese la patente del vehículo: ").strip().upper()
        while patente == "" or len(patente) < 6 or len(patente) > 7:
            mostrar_encabezado("REGISTRO DE VEHÍCULO")
            print(f"      {C_RED}[!] Error: La patente debe tener entre 6 y 7 caracteres.{C_RESET}")
            patente = input(f"  {C_GREEN}[+]{C_RESET} Ingrese la patente del vehículo: ").strip().upper()

        chasis_valido = False
        while not chasis_valido:
            try:
                chasis = int(input(f"  {C_GREEN}[+]{C_RESET} Ingrese el número de chasis: "))
                if chasis <= 0 or len(str(chasis)) < 6 or len(str(chasis)) > 17:
                    mostrar_encabezado("REGISTRO DE VEHÍCULO")
                    print(f"      {C_RED}[!] Error: El chasis debe tener entre 6 y 17 dígitos.{C_RESET}")
                else:
                    chasis_valido = True
            except ValueError:
                mostrar_encabezado("REGISTRO DE VEHÍCULO")
                print(f"      {C_RED}[!] Error: El chasis debe ser un valor numérico.{C_RESET}")

        motor_valido = False
        while not motor_valido:
            try:
                motor = int(input(f"  {C_GREEN}[+]{C_RESET} Ingrese el número de motor: "))
                if motor <= 0 or len(str(motor)) < 6 or len(str(motor)) > 17:
                    mostrar_encabezado("REGISTRO DE VEHÍCULO")
                    print(f"      {C_RED}[!] Error: El motor debe tener entre 6 y 17 dígitos.{C_RESET}")
                else:
                    motor_valido = True
            except ValueError:
                mostrar_encabezado("REGISTRO DE VEHÍCULO")
                print(f"      {C_RED}[!] Error: El motor debe ser numérico.{C_RESET}")

        marca = input(f"  {C_GREEN}[+]{C_RESET} Ingrese la marca del vehículo: ")
        while marca == "" or not marca.isalpha():
            mostrar_encabezado("REGISTRO DE VEHÍCULO")
            print(f"      {C_RED}[!] Error: La marca no puede quedar vacía y debe contener solo letras.{C_RESET}")
            marca = input(f"  {C_GREEN}[+]{C_RESET} Ingrese la marca del vehículo: ")

        modelo = input(f"  {C_GREEN}[+]{C_RESET} Ingrese el modelo del vehículo: ")
        while modelo == "":
            mostrar_encabezado("REGISTRO DE VEHÍCULO")
            print(f"      {C_RED}[!] Error: El modelo no puede quedar vacío.{C_RESET}")
            modelo = input(f"  {C_GREEN}[+]{C_RESET} Ingrese el modelo del vehículo: ")

        color = input(f"  {C_GREEN}[+]{C_RESET} Ingrese el color del vehículo: ")
        while color == "" or not color.isalpha():
            mostrar_encabezado("REGISTRO DE VEHÍCULO")
            print(f"      {C_RED}[!] Error: El color no puede quedar vacío y debe contener solo letras.{C_RESET}")
            color = input(f"  {C_GREEN}[+]{C_RESET} Ingrese el color del vehículo: ")

        anio_valido = False
        while not anio_valido:
            try:
                anio = int(input(f"  {C_GREEN}[+]{C_RESET} Ingrese el año del vehículo: "))
                if anio <= 0 or anio > datetime.now().year:
                    mostrar_encabezado("REGISTRO DE VEHÍCULO")
                    print(f"      {C_RED}[!] Error: El año no puede ser negativo, cero o mayor al actual.{C_RESET}")
                else:
                    anio_valido = True
            except ValueError:
                mostrar_encabezado("REGISTRO DE VEHÍCULO")
                print(f"      {C_RED}[!] Error: El año debe ser un valor numérico.{C_RESET}")

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
        
        print(f"\n{C_GREEN}══════════════════════════════════════════════════════════════{C_RESET}")
        print(f" {C_GREEN}[✓] ¡Vehículo patente {patente.upper()} registrado con éxito!{C_RESET}")
        print(f"{C_GREEN}══════════════════════════════════════════════════════════════{C_RESET}\n")
        input(f"{C_BOLD}Presione Enter para continuar...{C_RESET}")
        return vehiculos
    except Exception as error:
        mostrar_encabezado("REGISTRO DE VEHÍCULO")
        print(f"\n{C_RED}  [!] Error al momento de crear vehículo: {error}{C_RESET}")
        input(f"\n{C_BOLD}Presione Enter para continuar...{C_RESET}")
        return vehiculos

def poliza(usuarios, vehiculos, polizas):
    try:
        mostrar_encabezado("REGISTRO DE PÓLIZA", mostrar_uf=True)

        if not usuarios:
            print(f"  {C_RED}[!] No hay clientes registrados.{C_RESET}")
            input(f"\n{C_BOLD}Presione Enter para continuar...{C_RESET}")
            return polizas

        rut_agente = input(f"  {C_GREEN}[+]{C_RESET} Ingrese el RUT del agente de ventas: ")
        while rut_agente == "" or len(rut_agente) < 8 or len(rut_agente) > 9 or not rut_agente.isdigit():
            mostrar_encabezado("REGISTRO DE PÓLIZA", mostrar_uf=True)
            print(f"      {C_RED}[!] Error: El RUT del agente debe tener entre 8 y 9 dígitos.{C_RESET}")
            rut_agente = input(f"  {C_GREEN}[+]{C_RESET} Ingrese el RUT del agente de ventas: ")

        id_valido = False
        while not id_valido:
            ultimo_id = max(polizas.keys()) if polizas else 0
            sugerencia = f" (Último registrado: {ultimo_id}, Sugerir: {ultimo_id+1})" if ultimo_id > 0 else ""
            
            try:
                id_poliza = int(input(f"\n  {C_GREEN}[+]{C_RESET} Ingrese el número de la póliza{C_YELLOW}{sugerencia}{C_RESET}: "))
                if id_poliza <= 0:
                    mostrar_encabezado("REGISTRO DE PÓLIZA", mostrar_uf=True)
                    print(f"      {C_RED}[!] Error: El identificador debe ser positivo.{C_RESET}")
                elif id_poliza in polizas:
                    mostrar_encabezado("REGISTRO DE PÓLIZA", mostrar_uf=True)
                    print(f"      {C_RED}[!] Error: Ya existe una póliza con ese ID.{C_RESET}")
                else:
                    id_valido = True
            except ValueError:
                mostrar_encabezado("REGISTRO DE PÓLIZA", mostrar_uf=True)
                print(f"      {C_RED}[!] Error: El identificador debe ser numérico.{C_RESET}")

        rut_usuario = input(f"  {C_GREEN}[+]{C_RESET} Ingrese el RUT del cliente contratante: ")
        while rut_usuario not in usuarios:
            mostrar_encabezado("REGISTRO DE PÓLIZA", mostrar_uf=True)
            print(f"      {C_RED}[!] Error: El RUT no corresponde a un cliente registrado.{C_RESET}")
            rut_usuario = input(f"  {C_GREEN}[+]{C_RESET} Ingrese el RUT del cliente contratante: ")

        tipo_valido = False
        while not tipo_valido:
            print(f"\n  {C_YELLOW}Seleccione el tipo de seguro:{C_RESET}")
            print(f"    [{C_CYAN}1{C_RESET}] Seguro automotriz")
            print(f"    [{C_CYAN}2{C_RESET}] Seguro de vida")
            try:
                opcion = int(input(f"  {C_GREEN}[+]{C_RESET} Opción: "))
                if opcion == 1:
                    tipo_seguro = "Automotriz"
                    tipo_valido = True
                elif opcion == 2:
                    tipo_seguro = "Vida"
                    tipo_valido = True
                else:
                    mostrar_encabezado("REGISTRO DE PÓLIZA", mostrar_uf=True)
                    print(f"      {C_RED}[!] Error: Opción inválida.{C_RESET}")
            except ValueError:
                mostrar_encabezado("REGISTRO DE PÓLIZA", mostrar_uf=True)
                print(f"      {C_RED}[!] Error: Debe ingresar un número.{C_RESET}")

        if tipo_seguro == "Automotriz":
            if not vehiculos:
                print(f"\n  {C_RED}[!] Error: No hay vehículos registrados. Registre uno primero para contratar seguro automotriz.{C_RESET}")
                input(f"\n{C_BOLD}Presione Enter para continuar...{C_RESET}")
                return polizas
                
            patente = input(f"\n  {C_GREEN}[+]{C_RESET} Ingrese la patente del vehículo asegurado: ").strip().upper()
            while patente not in vehiculos:
                mostrar_encabezado("REGISTRO DE PÓLIZA", mostrar_uf=True)
                print(f"      {C_RED}[!] Error: La patente no corresponde a un vehículo registrado.{C_RESET}")
                patente = input(f"  {C_GREEN}[+]{C_RESET} Ingrese la patente del vehículo asegurado: ").strip().upper()
        else:
            patente = "N/A"

        # Fechas de Vigencia
        fecha_ini_valida = False
        while not fecha_ini_valida:
            inicio_str = input(f"\n  {C_GREEN}[+]{C_RESET} Ingrese fecha de inicio de cobertura (DD/MM/AAAA): ")
            try:
                fecha_inicio = datetime.strptime(inicio_str, "%d/%m/%Y").date()
                fecha_ini_valida = True
            except ValueError:
                mostrar_encabezado("REGISTRO DE PÓLIZA", mostrar_uf=True)
                print(f"      {C_RED}[!] Error: Formato de fecha inválido.{C_RESET}")

        vigencia_valida = False
        while not vigencia_valida:
            try:
                vigencia_meses = int(input(f"  {C_GREEN}[+]{C_RESET} Ingrese la duración en meses (Mínimo 12): "))
                if vigencia_meses < 12:
                    mostrar_encabezado("REGISTRO DE PÓLIZA", mostrar_uf=True)
                    print(f"      {C_RED}[!] Error: El periodo mínimo de vigencia es de 12 meses.{C_RESET}")
                else:
                    vigencia_valida = True
            except ValueError:
                mostrar_encabezado("REGISTRO DE PÓLIZA", mostrar_uf=True)
                print(f"      {C_RED}[!] Error: Debe ingresar un número entero.{C_RESET}")

        # Cálculo preciso de la fecha de fin considerando meses
        año_fin = fecha_inicio.year + (fecha_inicio.month + vigencia_meses - 1) // 12
        mes_fin = (fecha_inicio.month + vigencia_meses - 1) % 12 + 1
        _, ultimo_dia_mes = calendar.monthrange(año_fin, mes_fin)
        dia_fin = min(fecha_inicio.day, ultimo_dia_mes)
        fecha_fin = datetime(año_fin, mes_fin, dia_fin).date()

        # Evaluación del Estado
        if fecha_fin < datetime.now().date():
            estado_poliza = "De baja"
            print(f"\n      {C_YELLOW}[!] Aviso: La fecha de fin calculada ({fecha_fin.strftime('%d/%m/%Y')}) ya pasó. La póliza se guardará como 'De baja'.{C_RESET}")
        else:
            estado_poliza = "Vigente"

        # Precios
        valor_valido = False
        while not valor_valido:
            try:
                valor_anual = float(input(f"\n  {C_GREEN}[+]{C_RESET} Ingrese el valor anual de la póliza en UF: "))
                if valor_anual <= 0:
                    mostrar_encabezado("REGISTRO DE PÓLIZA", mostrar_uf=True)
                    print(f"      {C_RED}[!] Error: El valor anual debe ser positivo.{C_RESET}")
                else:
                    valor_valido = True
            except ValueError:
                mostrar_encabezado("REGISTRO DE PÓLIZA", mostrar_uf=True)
                print(f"      {C_RED}[!] Error: El valor anual debe ser numérico.{C_RESET}")
        
        print(f"      {C_CYAN}[i] Equivalente anual: {formato_clp(uf_a_clp(valor_anual))}{C_RESET}\n")

        cobertura_valida = False
        while not cobertura_valida:
            try:
                cobertura = float(input(f"  {C_GREEN}[+]{C_RESET} Ingrese la cobertura máxima de la póliza en UF: "))
                if cobertura <= 0:
                    mostrar_encabezado("REGISTRO DE PÓLIZA", mostrar_uf=True)
                    print(f"      {C_RED}[!] Error: La cobertura debe ser positiva.{C_RESET}")
                else:
                    cobertura_valida = True
            except ValueError:
                mostrar_encabezado("REGISTRO DE PÓLIZA", mostrar_uf=True)
                print(f"      {C_RED}[!] Error: La cobertura debe ser numérica.{C_RESET}")

        print(f"      {C_CYAN}[i] Equivalente cobertura: {formato_clp(uf_a_clp(cobertura))}{C_RESET}\n")

        # LÓGICA DE CANCELACIÓN AUTOMÁTICA DE PÓLIZAS ANTERIORES
        if estado_poliza == "Vigente":
            if tipo_seguro == "Automotriz":
                for p_id, p_datos in polizas.items():
                    if p_datos['patente'] == patente and p_datos['tipo_seguro'] == "Automotriz" and p_datos['estado'] == "Vigente":
                        polizas[p_id]['estado'] = "De baja"
                        print(f"      {C_YELLOW}[!] IMPORTANTE: La póliza automotriz anterior N° {p_id} ha quedado 'De baja' automáticamente.{C_RESET}")
            elif tipo_seguro == "Vida":
                for p_id, p_datos in polizas.items():
                    if p_datos['rut_usuario'] == rut_usuario and p_datos['tipo_seguro'] == "Vida" and p_datos['estado'] == "Vigente":
                        polizas[p_id]['estado'] = "De baja"
                        print(f"      {C_YELLOW}[!] IMPORTANTE: La póliza de vida anterior N° {p_id} ha quedado 'De baja' automáticamente.{C_RESET}")

        polizas[id_poliza] = {
            "rut_agente": rut_agente,
            "id_poliza": id_poliza,
            "rut_usuario": rut_usuario,
            "tipo_seguro": tipo_seguro,
            "patente": patente,
            "fecha_inicio": fecha_inicio,
            "fecha_fin": fecha_fin,
            "valor_anual": valor_anual, 
            "cobertura": cobertura,     
            "estado": estado_poliza
        }
        
        print(f"\n{C_GREEN}══════════════════════════════════════════════════════════════{C_RESET}")
        print(f" {C_GREEN}[✓] ¡Póliza N° {id_poliza} registrada con éxito!{C_RESET}")
        print(f"{C_GREEN}══════════════════════════════════════════════════════════════{C_RESET}\n")
        input(f"{C_BOLD}Presione Enter para continuar...{C_RESET}")
        return polizas
    except Exception as error:
        mostrar_encabezado("REGISTRO DE PÓLIZA", mostrar_uf=True)
        print(f"\n{C_RED}  [!] Error al momento de crear póliza: {error}{C_RESET}")
        input(f"\n{C_BOLD}Presione Enter para continuar...{C_RESET}")
        return polizas

def siniestro(vehiculos, polizas, siniestros):
    try:
        mostrar_encabezado("REGISTRO DE SINIESTRO", mostrar_uf=True)

        if not polizas:
            print(f"  {C_RED}[!] No hay pólizas registradas. Registre una primero.{C_RESET}")
            input(f"\n{C_BOLD}Presione Enter para continuar...{C_RESET}")
            return siniestros

        num_valido = False
        while not num_valido:
            ultimo_id = max(siniestros.keys()) if siniestros else 0
            sugerencia = f" (Último registrado: {ultimo_id}, Sugerir: {ultimo_id+1})" if ultimo_id > 0 else ""
            
            try:
                numero_declaracion = int(input(f"\n  {C_GREEN}[+]{C_RESET} Ingrese el número del siniestro{C_YELLOW}{sugerencia}{C_RESET}: "))
                if numero_declaracion <= 0:
                    mostrar_encabezado("REGISTRO DE SINIESTRO", mostrar_uf=True)
                    print(f"      {C_RED}[!] Error: El número debe ser positivo.{C_RESET}")
                elif numero_declaracion in siniestros:
                    mostrar_encabezado("REGISTRO DE SINIESTRO", mostrar_uf=True)
                    print(f"      {C_RED}[!] Error: Ya existe un siniestro con ese número.{C_RESET}")
                else:
                    num_valido = True
            except ValueError:
                mostrar_encabezado("REGISTRO DE SINIESTRO", mostrar_uf=True)
                print(f"      {C_RED}[!] Error: El número debe ser numérico.{C_RESET}")

        poliza_valida = False
        while not poliza_valida:
            try:
                poliza_asociada = int(input(f"  {C_GREEN}[+]{C_RESET} Ingrese el número de la póliza asociada: "))
                if poliza_asociada not in polizas:
                    mostrar_encabezado("REGISTRO DE SINIESTRO", mostrar_uf=True)
                    print(f"      {C_RED}[!] Error: No existe una póliza registrada con ese ID.{C_RESET}")
                else:
                    poliza_valida = True
            except ValueError:
                mostrar_encabezado("REGISTRO DE SINIESTRO", mostrar_uf=True)
                print(f"      {C_RED}[!] Error: El ID debe ser numérico.{C_RESET}")

        poliza_ref = polizas[poliza_asociada]
        tipo_seguro_asociado = poliza_ref['tipo_seguro']
        cobertura_maxima = poliza_ref['cobertura']

        informacion_siniestro = input(f"  {C_GREEN}[+]{C_RESET} Ingrese descripción del siniestro: ")
        while informacion_siniestro == "":
            mostrar_encabezado("REGISTRO DE SINIESTRO", mostrar_uf=True)
            print(f"      {C_RED}[!] Error: La información no puede quedar vacía.{C_RESET}")
            informacion_siniestro = input(f"  {C_GREEN}[+]{C_RESET} Ingrese descripción del siniestro: ")

        rut_siniestrado = input(f"  {C_GREEN}[+]{C_RESET} Ingrese el RUT del conductor/afectado: ")
        while rut_siniestrado == "" or len(rut_siniestrado) < 8 or len(rut_siniestrado) > 9 or not rut_siniestrado.isdigit():
            mostrar_encabezado("REGISTRO DE SINIESTRO", mostrar_uf=True)
            print(f"      {C_RED}[!] Error: El RUT debe tener entre 8 y 9 dígitos.{C_RESET}")
            rut_siniestrado = input(f"  {C_GREEN}[+]{C_RESET} Ingrese el RUT del conductor/afectado: ")

        fecha_valida = False
        while not fecha_valida:
            fecha = input(f"  {C_GREEN}[+]{C_RESET} Ingrese la fecha de ocurrencia (DD/MM/AAAA): ")
            try:
                fecha_siniestro = datetime.strptime(fecha, "%d/%m/%Y").date()
                if fecha_siniestro > datetime.now().date():
                    mostrar_encabezado("REGISTRO DE SINIESTRO", mostrar_uf=True)
                    print(f"      {C_RED}[!] Error: La fecha no puede ser futura.{C_RESET}")
                else:
                    fecha_valida = True
            except ValueError:
                mostrar_encabezado("REGISTRO DE SINIESTRO", mostrar_uf=True)
                print(f"      {C_RED}[!] Error: Formato de fecha inválido.{C_RESET}")

        if tipo_seguro_asociado == "Automotriz":
            patente = input(f"  {C_GREEN}[+]{C_RESET} Ingrese la patente del vehículo siniestrado: ").strip().upper()
            while patente not in vehiculos:
                mostrar_encabezado("REGISTRO DE SINIESTRO", mostrar_uf=True)
                print(f"      {C_RED}[!] Error: La patente no corresponde a un vehículo registrado.{C_RESET}")
                patente = input(f"  {C_GREEN}[+]{C_RESET} Ingrese la patente del vehículo siniestrado: ").strip().upper()

            taller = input(f"  {C_GREEN}[+]{C_RESET} Ingrese la dirección del taller asignado: ")
            while taller == "":
                mostrar_encabezado("REGISTRO DE SINIESTRO", mostrar_uf=True)
                print(f"      {C_RED}[!] Error: La dirección no puede estar vacía.{C_RESET}")
                taller = input(f"  {C_GREEN}[+]{C_RESET} Ingrese la dirección del taller asignado: ")

            fecha_rep_valida = False
            while not fecha_rep_valida:
                fecha_rep = input(f"  {C_GREEN}[+]{C_RESET} Ingrese fecha estimada de reparación (DD/MM/AAAA): ")
                try:
                    fecha_reparacion = datetime.strptime(fecha_rep, "%d/%m/%Y").date()
                    fecha_rep_valida = True
                except ValueError:
                    mostrar_encabezado("REGISTRO DE SINIESTRO", mostrar_uf=True)
                    print(f"      {C_RED}[!] Error: Formato de fecha inválido.{C_RESET}")
        else:
            patente = "N/A"
            fecha_reparacion = None
            taller = input(f"  {C_GREEN}[+]{C_RESET} Ingrese el lugar de ocurrencia/institución: ")
            while taller == "":
                mostrar_encabezado("REGISTRO DE SINIESTRO", mostrar_uf=True)
                print(f"      {C_RED}[!] Error: El lugar no puede estar vacío.{C_RESET}")
                taller = input(f"  {C_GREEN}[+]{C_RESET} Ingrese el lugar de ocurrencia/institución: ")

        # Menú interno para consultar el estado de pago del siniestro
        pago_valido = False
        while not pago_valido:
            print(f"\n  {C_YELLOW}Estado de pago del siniestro:{C_RESET}")
            print(f"    [{C_CYAN}1{C_RESET}] Siniestro Pagado")
            print(f"    [{C_CYAN}2{C_RESET}] Pendiente de pago")
            try:
                opc_pago = int(input(f"  {C_GREEN}[+]{C_RESET} Opción: "))
                if opc_pago == 1:
                    estado_pago = "Pagado"
                    pago_valido = True
                elif opc_pago == 2:
                    estado_pago = "Pendiente de pago"
                    pago_valido = True
                else:
                    mostrar_encabezado("REGISTRO DE SINIESTRO", mostrar_uf=True)
                    print(f"      {C_RED}[!] Error: Opción inválida.{C_RESET}")
            except ValueError:
                mostrar_encabezado("REGISTRO DE SINIESTRO", mostrar_uf=True)
                print(f"      {C_RED}[!] Error: Debe ingresar un número.{C_RESET}")

        if estado_pago == "Pagado":
            monto_valido = False
            while not monto_valido:
                try:
                    monto_pagado = float(input(f"\n  {C_GREEN}[+]{C_RESET} Ingrese el monto pagado en UF (Max: {cobertura_maxima} UF): "))
                    if monto_pagado < 0:
                        mostrar_encabezado("REGISTRO DE SINIESTRO", mostrar_uf=True)
                        print(f"      {C_RED}[!] Error: El monto no puede ser negativo.{C_RESET}")
                    elif monto_pagado > cobertura_maxima:
                        mostrar_encabezado("REGISTRO DE SINIESTRO", mostrar_uf=True)
                        print(f"      {C_RED}[!] Error: El monto supera la cobertura máxima ({cobertura_maxima} UF).{C_RESET}")
                    else:
                        monto_valido = True
                except ValueError:
                    mostrar_encabezado("REGISTRO DE SINIESTRO", mostrar_uf=True)
                    print(f"      {C_RED}[!] Error: El monto debe ser numérico.{C_RESET}")
            print(f"      {C_CYAN}[i] Equivalente pagado: {formato_clp(uf_a_clp(monto_pagado))}{C_RESET}\n")
        else:
            monto_pagado = 0
            print(f"      {C_CYAN}[i] Siniestro registrado como pendiente (Monto actual: 0 UF).{C_RESET}\n")

        siniestros[numero_declaracion] = {
            "numero_declaracion": numero_declaracion,
            "informacion_siniestro": informacion_siniestro,
            "poliza_asociada": poliza_asociada,
            "tipo_seguro": tipo_seguro_asociado,
            "rut_siniestrado": rut_siniestrado,
            "patente": patente,
            "fecha_siniestro": fecha_siniestro,
            "taller": taller,
            "fecha_reparacion": fecha_reparacion,
            "monto_pagado": monto_pagado, 
            "estado_pago": estado_pago    
        }
        
        print(f"\n{C_GREEN}══════════════════════════════════════════════════════════════{C_RESET}")
        print(f" {C_GREEN}[✓] ¡Siniestro N° {numero_declaracion} registrado con éxito!{C_RESET}")
        print(f"{C_GREEN}══════════════════════════════════════════════════════════════{C_RESET}\n")
        input(f"{C_BOLD}Presione Enter para continuar...{C_RESET}")
        return siniestros
    except Exception as error:
        mostrar_encabezado("REGISTRO DE SINIESTRO", mostrar_uf=True)
        print(f"\n{C_RED}  [!] Error al momento de crear siniestro: {error}{C_RESET}")
        input(f"\n{C_BOLD}Presione Enter para continuar...{C_RESET}")
        return siniestros


# ============================================================
# 2. MÓDULOS DE CONSULTA Y LISTADO
# ============================================================

def consultar_usuario(usuarios, polizas):
    """Opción 5: Consulta cliente por RUT e indica pólizas asociadas."""
    mostrar_encabezado("CONSULTAR CLIENTE")
    
    if not usuarios:
        print(f"  {C_YELLOW}⚠ No hay clientes registrados.{C_RESET}")
        input(f"\n{C_BOLD}Presione Enter para regresar...{C_RESET}")
        return
        
    rut = input(f"  {C_GREEN}[+]{C_RESET} Ingrese el RUT a buscar: ")
    while rut == "" or len(rut) < 8 or len(rut) > 9 or not rut.isdigit():
        mostrar_encabezado("CONSULTAR CLIENTE")
        print(f"      {C_RED}[!] Error: El RUT debe tener entre 8 y 9 dígitos.{C_RESET}")
        rut = input(f"  {C_GREEN}[+]{C_RESET} Ingrese el RUT a buscar: ")

    cliente = usuarios.get(rut)
    
    if not cliente:
        print(f"\n  {C_RED}[!] No se encontró ningún cliente con el RUT {rut}{C_RESET}")
    else:
        print(f"\n  {C_CYAN}=== DATOS DEL CLIENTE ==={C_RESET}")
        print(f"  {C_BOLD}RUT:{C_RESET}         {cliente['rut']}")
        print(f"  {C_BOLD}Nombre:{C_RESET}      {cliente['nombre']} {cliente['apellido_paterno']} {cliente['apellido_materno']}")
        print(f"  {C_BOLD}Nacimiento:{C_RESET}  {cliente['fecha_nacimiento'].strftime('%d/%m/%Y')}")
        print(f"  {C_BOLD}Teléfono:{C_RESET}    +56 {cliente['telefono']}")
        print(f"  {C_BOLD}Dirección:{C_RESET}   {cliente['direccion']}")
        print(f"  {C_BOLD}Correo:{C_RESET}      {cliente['correo']}")
        
        # Búsqueda de pólizas asociadas al RUT
        polizas_asociadas = [p for p in polizas.values() if p['rut_usuario'] == rut]
        if polizas_asociadas:
            print(f"\n  {C_BOLD}Pólizas Asociadas:{C_RESET}")
            for p in polizas_asociadas:
                color_estado = C_GREEN if p['estado'].lower() == 'vigente' else C_RED
                print(f"    - Póliza {p['id_poliza']} ({p['tipo_seguro']}) | Estado: {color_estado}{p['estado']}{C_RESET}")
        else:
            print(f"\n  {C_BOLD}Pólizas Asociadas:{C_RESET} Ninguna")
            
        print(f"  {C_CYAN}========================={C_RESET}")
        
    input(f"\n{C_BOLD}Presione Enter para regresar...{C_RESET}")

def listar_usuarios(usuarios, polizas):
    """Opción 6: Listar todos los clientes y mostrar pólizas vinculadas."""
    mostrar_encabezado("LISTADO DE CLIENTES")

    if not usuarios:
        print(f"  {C_YELLOW}⚠ No hay clientes registrados en el sistema.{C_RESET}")
        input(f"\n{C_BOLD}Presione Enter para regresar...{C_RESET}")
        return

    lista_ruts = list(usuarios.keys())
    registros_por_pagina = 2
    total_registros = len(lista_ruts)

    for i in range(0, total_registros, registros_por_pagina):
        if i > 0: 
            mostrar_encabezado("LISTADO DE CLIENTES")
            
        pagina_actual = (i // registros_por_pagina) + 1
        total_paginas = (total_registros + registros_por_pagina - 1) // registros_por_pagina

        print(f"  {C_YELLOW}Página {pagina_actual} de {total_paginas} (Total: {total_registros}){C_RESET}\n")

        bloque = lista_ruts[i: i + registros_por_pagina]
        for num, rut in enumerate(bloque, start=i + 1):
            datos = usuarios[rut]
            nombre_completo = f"{datos['nombre']} {datos['apellido_paterno']} {datos['apellido_materno']}"
            fecha_str = datos['fecha_nacimiento'].strftime('%d/%m/%Y')

            print(f"  {C_CYAN}[{num}] RUT: {datos['rut']}{C_RESET}")
            print(f"      {C_BOLD}Nombre:{C_RESET}     {nombre_completo}")
            print(f"      {C_BOLD}Nacimiento:{C_RESET} {fecha_str}")
            print(f"      {C_BOLD}Teléfono:{C_RESET}   +56 {datos['telefono']}")
            print(f"      {C_BOLD}Dirección:{C_RESET}  {datos['direccion']}")
            print(f"      {C_BOLD}Correo:{C_RESET}     {datos['correo']}")
            
            polizas_asociadas = [p for p in polizas.values() if p['rut_usuario'] == rut]
            if polizas_asociadas:
                print(f"\n      {C_BOLD}Pólizas Contratadas:{C_RESET}")
                for p in polizas_asociadas:
                    color_est = C_GREEN if p['estado'].lower() == 'vigente' else C_RED
                    print(f"        - Póliza {p['id_poliza']} ({p['tipo_seguro']}) | {color_est}{p['estado']}{C_RESET}")
            else:
                print(f"      {C_BOLD}Pólizas Contratadas:{C_RESET} Ninguna")
                
            print(f"  {C_BLUE}------------------------------------------------------------{C_RESET}")

        if i + registros_por_pagina < total_registros:
            input(f"\n{C_BOLD}Presione ENTER para ver la siguiente página...{C_RESET}")

    print(f"\n  {C_GREEN}Fin del listado.{C_RESET}")
    input(f"{C_BOLD}Presione Enter para regresar al menú principal...{C_RESET}")

def consultar_vehiculo_por_patente(vehiculos, usuarios, polizas):
    """Opción 7: Consulta vehículo por patente e indica si tiene pólizas."""
    mostrar_encabezado("CONSULTAR VEHÍCULO")

    if not vehiculos:
        print(f"  {C_YELLOW}⚠ No hay vehículos registrados en el sistema.{C_RESET}")
        input(f"\n{C_BOLD}Presione Enter para regresar...{C_RESET}")
        return

    try:
        patente = input(f"  {C_GREEN}[+]{C_RESET} Ingrese la patente a buscar: ").strip().upper()
        while patente == "" or len(patente) < 6 or len(patente) > 7:
            mostrar_encabezado("CONSULTAR VEHÍCULO")
            print(f"      {C_RED}[!] Error: La patente debe tener entre 6 y 7 caracteres.{C_RESET}")
            patente = input(f"  {C_GREEN}[+]{C_RESET} Ingrese la patente a buscar: ").strip().upper()

        vehiculo_encontrado = vehiculos.get(patente)

        if vehiculo_encontrado is None:
            print(f"\n  {C_RED}[!] No se encontró ningún vehículo con patente {patente}{C_RESET}")
        else:
            propietario_rut = vehiculo_encontrado["rut_duenio"]
            propietario = usuarios.get(propietario_rut)
            nombre_propietario = f"{propietario['nombre']} {propietario['apellido_paterno']}" if propietario else "Desconocido"

            print(f"\n  {C_CYAN}=== DATOS DEL VEHÍCULO ==={C_RESET}")
            print(f"  {C_BOLD}Patente:{C_RESET}     {vehiculo_encontrado['patente']}")
            print(f"  {C_BOLD}Marca:{C_RESET}       {vehiculo_encontrado['marca']}")
            print(f"  {C_BOLD}Modelo:{C_RESET}      {vehiculo_encontrado['modelo']}")
            print(f"  {C_BOLD}Año:{C_RESET}         {vehiculo_encontrado['anio']}")
            print(f"  {C_BOLD}Color:{C_RESET}       {vehiculo_encontrado['color']}")
            print(f"  {C_BOLD}Chasis:{C_RESET}      {vehiculo_encontrado['chasis']}")
            print(f"  {C_BOLD}Motor:{C_RESET}       {vehiculo_encontrado['motor']}")
            print(f"  {C_BOLD}Propietario:{C_RESET} {nombre_propietario} (RUT: {propietario_rut})")
            
            polizas_asociadas = [p for p in polizas.values() if p['patente'] == patente]
            if polizas_asociadas:
                print(f"\n  {C_BOLD}Pólizas Asociadas:{C_RESET}")
                for p in polizas_asociadas:
                    color_est = C_GREEN if p['estado'].lower() == 'vigente' else C_RED
                    print(f"    - Póliza {p['id_poliza']} | Estado: {color_est}{p['estado']}{C_RESET}")
            else:
                print(f"\n  {C_BOLD}Pólizas Asociadas:{C_RESET} Ninguna")

            print(f"  {C_CYAN}=========================={C_RESET}")
            
    except Exception as error:
        print(f"\n{C_RED}  [!] Error al momento de realizar la consulta: {error}{C_RESET}")

    input(f"\n{C_BOLD}Presione Enter para regresar...{C_RESET}")

def listar_vehiculos(vehiculos, usuarios, polizas):
    """Opción 8: Listar todos los vehículos y sus seguros asociados."""
    mostrar_encabezado("LISTADO DE VEHÍCULOS")

    if not vehiculos:
        print(f"  {C_YELLOW}⚠ No hay vehículos registrados.{C_RESET}")
        input(f"\n{C_BOLD}Presione Enter para regresar...{C_RESET}")
        return

    lista_patentes = list(vehiculos.keys())
    registros_por_pagina = 2
    total_registros = len(lista_patentes)

    for i in range(0, total_registros, registros_por_pagina):
        if i > 0: 
            mostrar_encabezado("LISTADO DE VEHÍCULOS")
            
        pagina_actual = (i // registros_por_pagina) + 1
        total_paginas = (total_registros + registros_por_pagina - 1) // registros_por_pagina

        print(f"  {C_YELLOW}Página {pagina_actual} de {total_paginas} (Total: {total_registros}){C_RESET}\n")

        bloque = lista_patentes[i: i + registros_por_pagina]
        for num, pat in enumerate(bloque, start=i + 1):
            datos = vehiculos[pat]
            propietario_rut = datos["rut_duenio"]
            propietario = usuarios.get(propietario_rut)
            nombre_prop = f"{propietario['nombre']} {propietario['apellido_paterno']}" if propietario else "Desconocido"

            print(f"  {C_CYAN}[{num}] Patente: {datos['patente']}{C_RESET}")
            print(f"      {C_BOLD}Marca:{C_RESET}       {datos['marca']}")
            print(f"      {C_BOLD}Modelo:{C_RESET}      {datos['modelo']}")
            print(f"      {C_BOLD}Año:{C_RESET}         {datos['anio']}")
            print(f"      {C_BOLD}Color:{C_RESET}       {datos['color']}")
            print(f"      {C_BOLD}Propietario:{C_RESET} {nombre_prop}")
            
            polizas_asociadas = [p for p in polizas.values() if p['patente'] == pat]
            if polizas_asociadas:
                print(f"\n      {C_BOLD}Pólizas Vinculadas:{C_RESET}")
                for p in polizas_asociadas:
                    color_est = C_GREEN if p['estado'].lower() == 'vigente' else C_RED
                    print(f"        - Póliza {p['id_poliza']} | {color_est}{p['estado']}{C_RESET}")
            else:
                print(f"      {C_BOLD}Pólizas Vinculadas:{C_RESET} Ninguna")

            print(f"  {C_BLUE}------------------------------------------------------------{C_RESET}")

        if i + registros_por_pagina < total_registros:
            input(f"\n{C_BOLD}Presione ENTER para ver la siguiente página...{C_RESET}")

    print(f"\n  {C_GREEN}Fin del listado.{C_RESET}")
    input(f"{C_BOLD}Presione Enter para regresar al menú principal...{C_RESET}")

def consultar_poliza(polizas):
    """Opción 9: Consultar póliza por número."""
    mostrar_encabezado("CONSULTAR PÓLIZA", mostrar_uf=True)

    if not polizas:
        print(f"  {C_YELLOW}⚠ No hay pólizas registradas.{C_RESET}")
        input(f"\n{C_BOLD}Presione Enter para regresar...{C_RESET}")
        return

    id_valido = False
    while not id_valido:
        try:
            id_poliza = int(input(f"  {C_GREEN}[+]{C_RESET} Ingrese el número de la póliza: "))
            if id_poliza <= 0:
                mostrar_encabezado("CONSULTAR PÓLIZA", mostrar_uf=True)
                print(f"      {C_RED}[!] Error: El número debe ser positivo.{C_RESET}")
            else:
                id_valido = True
        except ValueError:
            mostrar_encabezado("CONSULTAR PÓLIZA", mostrar_uf=True)
            print(f"      {C_RED}[!] Error: El número debe ser numérico.{C_RESET}")

    poliza_encontrada = polizas.get(id_poliza)

    if poliza_encontrada is None:
        print(f"\n  {C_RED}[!] No se encontró ninguna póliza con el número {id_poliza}{C_RESET}")
    else:
        valor_uf = poliza_encontrada['valor_anual']
        cobert_uf = poliza_encontrada['cobertura']
        tipo_seg = poliza_encontrada['tipo_seguro']
        color_est = C_GREEN if poliza_encontrada['estado'].lower() == 'vigente' else C_RED
        
        print(f"\n  {C_CYAN}=== DATOS DE LA PÓLIZA ==={C_RESET}")
        print(f"  {C_BOLD}Tipo de seguro:{C_RESET} {tipo_seg}")
        if tipo_seg == "Automotriz":
            print(f"  {C_BOLD}Patente:{C_RESET}        {poliza_encontrada['patente']}")
        print(f"  {C_BOLD}RUT Cliente:{C_RESET}    {poliza_encontrada['rut_usuario']}")
        print(f"  {C_BOLD}RUT Agente:{C_RESET}     {poliza_encontrada['rut_agente']}")
        print(f"  {C_BOLD}Inicio Cobert:{C_RESET}  {poliza_encontrada['fecha_inicio'].strftime('%d/%m/%Y')}")
        print(f"  {C_BOLD}Fin Cobertura:{C_RESET}  {poliza_encontrada['fecha_fin'].strftime('%d/%m/%Y')}")
        print(f"  {C_BOLD}Valor Anual:{C_RESET}    {valor_uf} UF  ->  {C_GREEN}{formato_clp(uf_a_clp(valor_uf))}{C_RESET}")
        print(f"  {C_BOLD}Cobertura Max:{C_RESET}  {cobert_uf} UF  ->  {C_GREEN}{formato_clp(uf_a_clp(cobert_uf))}{C_RESET}")
        print(f"  {C_BOLD}Estado:{C_RESET}         {color_est}{poliza_encontrada['estado']}{C_RESET}")
        print(f"  {C_CYAN}=========================={C_RESET}")
        
    input(f"\n{C_BOLD}Presione Enter para regresar...{C_RESET}")

def listar_polizas(polizas):
    """Opción 10: Listar todas las pólizas con su estado y vigencia."""
    mostrar_encabezado("LISTADO DE PÓLIZAS", mostrar_uf=True)

    if not polizas:
        print(f"  {C_YELLOW}⚠ No hay pólizas registradas.{C_RESET}")
        input(f"\n{C_BOLD}Presione Enter para regresar...{C_RESET}")
        return

    lista_ids = list(polizas.keys())
    registros_por_pagina = 3
    total_registros = len(lista_ids)

    for i in range(0, total_registros, registros_por_pagina):
        if i > 0: 
            mostrar_encabezado("LISTADO DE PÓLIZAS", mostrar_uf=True)
            
        pagina_actual = (i // registros_por_pagina) + 1
        total_paginas = (total_registros + registros_por_pagina - 1) // registros_por_pagina

        print(f"  {C_YELLOW}Página {pagina_actual} de {total_paginas} (Total: {total_registros}){C_RESET}\n")

        bloque = lista_ids[i: i + registros_por_pagina]
        for num, id_pol in enumerate(bloque, start=i + 1):
            datos = polizas[id_pol]
            tipo_seg = datos['tipo_seguro']
            color_est = C_GREEN if datos['estado'].lower() == 'vigente' else C_RED
            
            print(f"  {C_CYAN}[{num}] Póliza N°: {datos['id_poliza']}{C_RESET}")
            print(f"      {C_BOLD}Tipo:{C_RESET}        {tipo_seg}")
            if tipo_seg == "Automotriz":
                print(f"      {C_BOLD}Vehículo:{C_RESET}    {datos['patente']}")
            print(f"      {C_BOLD}Cliente:{C_RESET}     {datos['rut_usuario']}")
            print(f"      {C_BOLD}Periodo:{C_RESET}     {datos['fecha_inicio'].strftime('%d/%m/%Y')} al {datos['fecha_fin'].strftime('%d/%m/%Y')}")
            print(f"      {C_BOLD}Valor:{C_RESET}       {datos['valor_anual']} UF ({formato_clp(uf_a_clp(datos['valor_anual']))})")
            print(f"      {C_BOLD}Estado:{C_RESET}      {color_est}{datos['estado']}{C_RESET}")
            print(f"  {C_BLUE}------------------------------------------------------------{C_RESET}")

        if i + registros_por_pagina < total_registros:
            input(f"\n{C_BOLD}Presione ENTER para ver la siguiente página...{C_RESET}")

    print(f"\n  {C_GREEN}Fin del listado.{C_RESET}")
    input(f"{C_BOLD}Presione Enter para regresar al menú principal...{C_RESET}")

def consultar_siniestro(siniestros):
    """Opción 11: Consultar siniestro por número."""
    mostrar_encabezado("CONSULTAR SINIESTRO", mostrar_uf=True)

    if not siniestros:
        print(f"  {C_YELLOW}⚠ No hay siniestros registrados.{C_RESET}")
        input(f"\n{C_BOLD}Presione Enter para regresar...{C_RESET}")
        return

    id_valido = False
    while not id_valido:
        try:
            id_siniestro = int(input(f"  {C_GREEN}[+]{C_RESET} Ingrese el número del siniestro: "))
            if id_siniestro <= 0:
                mostrar_encabezado("CONSULTAR SINIESTRO", mostrar_uf=True)
                print(f"      {C_RED}[!] Error: El número debe ser positivo.{C_RESET}")
            else:
                id_valido = True
        except ValueError:
            mostrar_encabezado("CONSULTAR SINIESTRO", mostrar_uf=True)
            print(f"      {C_RED}[!] Error: El número debe ser numérico.{C_RESET}")

    siniestro_encontrado = siniestros.get(id_siniestro)

    if siniestro_encontrado is None:
        print(f"\n  {C_RED}[!] No se encontró ningún siniestro con el número {id_siniestro}{C_RESET}")
    else:
        monto_uf = siniestro_encontrado.get('monto_pagado', 0)
        tipo_seg = siniestro_encontrado.get('tipo_seguro', 'Desconocido')
        estado_pago = siniestro_encontrado.get('estado_pago', 'Pendiente de pago')
        
        print(f"\n  {C_CYAN}=== DATOS DEL SINIESTRO ==={C_RESET}")
        print(f"  {C_BOLD}Tipo de Seguro:{C_RESET}   {tipo_seg}")
        print(f"  {C_BOLD}Póliza Asociada:{C_RESET}  {siniestro_encontrado['poliza_asociada']}")
        
        if tipo_seg == "Automotriz":
            fecha_rep = siniestro_encontrado['fecha_reparacion'].strftime('%d/%m/%Y') if siniestro_encontrado.get('fecha_reparacion') else "N/A"
            print(f"  {C_BOLD}Patente Vehículo:{C_RESET} {siniestro_encontrado['patente']}")
            print(f"  {C_BOLD}Taller Destino:{C_RESET}   {siniestro_encontrado['taller']}")
            print(f"  {C_BOLD}Fecha Reparación:{C_RESET} {fecha_rep}")
        else:
            print(f"  {C_BOLD}Lugar Suceso:{C_RESET}     {siniestro_encontrado['taller']}")

        print(f"  {C_BOLD}RUT Siniestrado:{C_RESET}  {siniestro_encontrado['rut_siniestrado']}")
        print(f"  {C_BOLD}Fecha Ocurrencia:{C_RESET} {siniestro_encontrado['fecha_siniestro'].strftime('%d/%m/%Y')}")
        print(f"  {C_BOLD}Descripción:{C_RESET}      {siniestro_encontrado['informacion_siniestro']}")
        
        if estado_pago == "Pagado":
            print(f"  {C_BOLD}Estado Financiero:{C_RESET}{C_GREEN} Pagado{C_RESET}")
            print(f"  {C_BOLD}Monto Pagado:{C_RESET}     {monto_uf} UF  ->  {C_GREEN}{formato_clp(uf_a_clp(monto_uf))}{C_RESET}")
        else:
            print(f"  {C_BOLD}Estado Financiero:{C_RESET}{C_YELLOW} Pendiente de pago{C_RESET}")
            print(f"  {C_BOLD}Monto Registrado:{C_RESET} 0 UF  ->  $0")

        print(f"  {C_CYAN}==========================={C_RESET}")

    input(f"\n{C_BOLD}Presione Enter para regresar...{C_RESET}")

def listar_siniestros(siniestros):
    """Opción 12: Listar todos los siniestros."""
    mostrar_encabezado("LISTADO DE SINIESTROS", mostrar_uf=True)

    if not siniestros:
        print(f"  {C_YELLOW}⚠ No hay siniestros registrados.{C_RESET}")
        input(f"\n{C_BOLD}Presione Enter para regresar...{C_RESET}")
        return

    lista_ids = list(siniestros.keys())
    registros_por_pagina = 2
    total_registros = len(lista_ids)

    for i in range(0, total_registros, registros_por_pagina):
        if i > 0: 
            mostrar_encabezado("LISTADO DE SINIESTROS", mostrar_uf=True)
            
        pagina_actual = (i // registros_por_pagina) + 1
        total_paginas = (total_registros + registros_por_pagina - 1) // registros_por_pagina

        print(f"  {C_YELLOW}Página {pagina_actual} de {total_paginas} (Total: {total_registros}){C_RESET}\n")

        bloque = lista_ids[i: i + registros_por_pagina]
        for num, id_sin in enumerate(bloque, start=i + 1):
            datos = siniestros[id_sin]
            monto_uf = datos.get('monto_pagado', 0)
            tipo_seg = datos.get('tipo_seguro', 'Desconocido')
            estado_pago = datos.get('estado_pago', 'Pendiente de pago')
            
            print(f"  {C_CYAN}[{num}] Siniestro N°: {datos['numero_declaracion']}{C_RESET}")
            print(f"      {C_BOLD}Póliza Asociada:{C_RESET}  {datos['poliza_asociada']} ({tipo_seg})")
            if tipo_seg == "Automotriz":
                print(f"      {C_BOLD}Patente Vehículo:{C_RESET} {datos['patente']}")
            print(f"      {C_BOLD}Fecha Ocurrencia:{C_RESET} {datos['fecha_siniestro'].strftime('%d/%m/%Y')}")
            print(f"      {C_BOLD}Descripción:{C_RESET}      {datos['informacion_siniestro']}")
            
            if estado_pago == "Pagado":
                print(f"      {C_BOLD}Estado Pago:{C_RESET}      {C_GREEN}Pagado{C_RESET}")
                print(f"      {C_BOLD}Monto Pagado:{C_RESET}     {monto_uf} UF ({formato_clp(uf_a_clp(monto_uf))})")
            else:
                print(f"      {C_BOLD}Estado Pago:{C_RESET}      {C_YELLOW}Pendiente de pago{C_RESET}")
                print(f"      {C_BOLD}Monto Registrado:{C_RESET} 0 UF ($0)")

            print(f"  {C_BLUE}------------------------------------------------------------{C_RESET}")

        if i + registros_por_pagina < total_registros:
            input(f"\n{C_BOLD}Presione ENTER para ver la siguiente página...{C_RESET}")

    print(f"\n  {C_GREEN}Fin del listado.{C_RESET}")
    input(f"{C_BOLD}Presione Enter para regresar al menú principal...{C_RESET}")


# ============================================================
# 3. MÓDULOS FINANCIEROS Y DE BALANCE
# ============================================================

def mostrar_monto_polizas(polizas):
    """Opción 13: Mostrar monto total de pólizas vendidas por tipo."""
    mostrar_encabezado("MONTO TOTAL DE PÓLIZAS VENDIDAS", mostrar_uf=True)

    total_uf_automotriz = 0
    total_uf_vida = 0

    for p in polizas.values():
        if p['tipo_seguro'] == "Automotriz":
            total_uf_automotriz += p['valor_anual']
        elif p['tipo_seguro'] == "Vida":
            total_uf_vida += p['valor_anual']

    total_uf_general = total_uf_automotriz + total_uf_vida

    print(f"  {C_CYAN}=== RESUMEN DE VENTAS ==={C_RESET}\n")
    
    print(f"  {C_YELLOW}■ SEGURO AUTOMOTRIZ{C_RESET}")
    print(f"    Total UF: {total_uf_automotriz}")
    print(f"    Total CLP: {C_GREEN}{formato_clp(uf_a_clp(total_uf_automotriz))}{C_RESET}\n")
    
    print(f"  {C_YELLOW}■ SEGURO DE VIDA{C_RESET}")
    print(f"    Total UF: {total_uf_vida}")
    print(f"    Total CLP: {C_GREEN}{formato_clp(uf_a_clp(total_uf_vida))}{C_RESET}\n")
    
    print(f"  {C_BLUE}---------------------------------------{C_RESET}")
    print(f"  {C_BOLD}TOTAL GENERAL UF:{C_RESET}  {total_uf_general}")
    print(f"  {C_BOLD}TOTAL GENERAL CLP:{C_RESET} {C_GREEN}{formato_clp(uf_a_clp(total_uf_general))}{C_RESET}")
    print(f"\n  {C_CYAN}========================={C_RESET}")
    
    input(f"\n{C_BOLD}Presione Enter para regresar...{C_RESET}")

def mostrar_monto_siniestros(siniestros):
    """Opción 14: Mostrar monto total de siniestros pagados."""
    mostrar_encabezado("MONTO TOTAL DE SINIESTROS PAGADOS", mostrar_uf=True)

    total_uf_siniestros = 0
    for s in siniestros.values():
        if s.get('estado_pago') == "Pagado":
            total_uf_siniestros += s.get('monto_pagado', 0)

    print(f"  {C_CYAN}=== RESUMEN DE DESEMBOLSOS ==={C_RESET}\n")
    print(f"  {C_BOLD}Total Desembolsado en UF:{C_RESET}  {total_uf_siniestros}")
    print(f"  {C_BOLD}Equivalente Total en CLP:{C_RESET}  {C_GREEN}{formato_clp(uf_a_clp(total_uf_siniestros))}{C_RESET}")
    print(f"\n  {C_CYAN}=============================={C_RESET}")
    print(f"  {C_YELLOW}*Nota: Sólo se contabilizan los siniestros con estado 'Pagado'.{C_RESET}")
    
    input(f"\n{C_BOLD}Presione Enter para regresar...{C_RESET}")

def mostrar_balance_general(polizas, siniestros):
    """Opción 15: Balance de Ingresos vs Gastos y Reporte de Ventas por Agente."""
    mostrar_encabezado("BALANCE GENERAL Y VENTAS POR AGENTE", mostrar_uf=True)
    
    ingresos_uf = sum(p['valor_anual'] for p in polizas.values())
    gastos_uf = sum(s.get('monto_pagado', 0) for s in siniestros.values() if s.get('estado_pago') == "Pagado")
    balance_uf = ingresos_uf - gastos_uf

    # Calcular ventas por agente
    ventas_agentes = {}
    for p in polizas.values():
        ag = p['rut_agente']
        ventas_agentes[ag] = ventas_agentes.get(ag, 0) + p['valor_anual']
    
    print(f"  {C_CYAN}=== VENTAS POR AGENTE ==={C_RESET}")
    if not ventas_agentes:
        print(f"    {C_YELLOW}No hay ventas registradas en el sistema.{C_RESET}")
    else:
        # Ordenamos los agentes de mayor a menor venta
        for ag, monto in sorted(ventas_agentes.items(), key=lambda x: x[1], reverse=True):
            print(f"    {C_BOLD}Agente RUT {ag}:{C_RESET} {monto} UF ({C_GREEN}{formato_clp(uf_a_clp(monto))}{C_RESET})")
    
    print(f"\n  {C_CYAN}=== BALANCE GENERAL ==={C_RESET}")
    print(f"  {C_BOLD}Total Ingresos (Pólizas Vendidas):{C_RESET} {ingresos_uf} UF")
    print(f"  {C_BOLD}Total Gastos (Siniestros Pagados):{C_RESET} {gastos_uf} UF")
    print(f"  {C_BLUE}--------------------------------------------------{C_RESET}")
    
    color_bal = C_GREEN if balance_uf >= 0 else C_RED
    print(f"  {C_BOLD}BALANCE NETO UF:{C_RESET}   {color_bal}{balance_uf} UF{C_RESET}")
    print(f"  {C_BOLD}BALANCE NETO CLP:{C_RESET}  {color_bal}{formato_clp(uf_a_clp(balance_uf))}{C_RESET}")
    print(f"  {C_CYAN}======================={C_RESET}")
    
    input(f"\n{C_BOLD}Presione Enter para regresar...{C_RESET}")


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
    limpiar_consola()
    print(f"{C_BLUE}╔════════════════════════════════════════════════════════════╗{C_RESET}")
    print(f"{C_BLUE}║{C_CYAN}{C_BOLD}               SISTEMA DE GESTIÓN DE SEGUROS                {C_RESET}{C_BLUE}║{C_RESET}")
    print(f"{C_BLUE}╠════════════════════════════════════════════════════════════╣{C_RESET}")
    print(f"{C_BLUE}║{C_RESET}                                                            {C_BLUE}║{C_RESET}")
    
    # SECCIÓN 1: REGISTROS
    print(f"{C_BLUE}║{C_YELLOW}{C_BOLD}  ■ REGISTROS                                               {C_RESET}{C_BLUE}║{C_RESET}")
    print(f"{C_BLUE}║{C_RESET}    [ {C_GREEN}1{C_RESET} ] Registrar cliente                                 {C_BLUE}║{C_RESET}")
    print(f"{C_BLUE}║{C_RESET}    [ {C_GREEN}2{C_RESET} ] Registrar vehículo                                {C_BLUE}║{C_RESET}")
    print(f"{C_BLUE}║{C_RESET}    [ {C_GREEN}3{C_RESET} ] Registrar póliza                                  {C_BLUE}║{C_RESET}")
    print(f"{C_BLUE}║{C_RESET}    [ {C_GREEN}4{C_RESET} ] Registrar siniestro                               {C_BLUE}║{C_RESET}")
    print(f"{C_BLUE}║{C_RESET}                                                            {C_BLUE}║{C_RESET}")
    
    # SECCIÓN 2: CONSULTAS Y LISTADOS
    print(f"{C_BLUE}║{C_YELLOW}{C_BOLD}  ■ CONSULTAS Y LISTADOS                                    {C_RESET}{C_BLUE}║{C_RESET}")
    print(f"{C_BLUE}║{C_RESET}    [ {C_GREEN}5{C_RESET} ] Consultar cliente por rut                         {C_BLUE}║{C_RESET}")
    print(f"{C_BLUE}║{C_RESET}    [ {C_GREEN}6{C_RESET} ] Listar todos los clientes                         {C_BLUE}║{C_RESET}")
    print(f"{C_BLUE}║{C_RESET}    [ {C_GREEN}7{C_RESET} ] Consulta vehículo por patente                     {C_BLUE}║{C_RESET}")
    print(f"{C_BLUE}║{C_RESET}    [ {C_GREEN}8{C_RESET} ] Listar todos los vehículos                        {C_BLUE}║{C_RESET}")
    print(f"{C_BLUE}║{C_RESET}    [ {C_GREEN}9{C_RESET} ] Consultar póliza por número                       {C_BLUE}║{C_RESET}")
    print(f"{C_BLUE}║{C_RESET}    [ {C_GREEN}10{C_RESET}] Listar todas las pólizas                          {C_BLUE}║{C_RESET}")
    print(f"{C_BLUE}║{C_RESET}    [ {C_GREEN}11{C_RESET}] Consultar siniestro por número                    {C_BLUE}║{C_RESET}")
    print(f"{C_BLUE}║{C_RESET}    [ {C_GREEN}12{C_RESET}] Listar todos los siniestros                       {C_BLUE}║{C_RESET}")
    
    # SECCIÓN 3: MÓDULO FINANCIERO
    print(f"{C_BLUE}║{C_YELLOW}{C_BOLD}  ■ MÓDULO FINANCIERO                                       {C_RESET}{C_BLUE}║{C_RESET}")
    print(f"{C_BLUE}║{C_RESET}    [ {C_GREEN}13{C_RESET}] Mostrar monto pólizas vendidas por tipo           {C_BLUE}║{C_RESET}")
    print(f"{C_BLUE}║{C_RESET}    [ {C_GREEN}14{C_RESET}] Mostrar monto de siniestros pagados               {C_BLUE}║{C_RESET}")
    print(f"{C_BLUE}║{C_RESET}    [ {C_GREEN}15{C_RESET}] Mostrar balance general y ventas por agente       {C_BLUE}║{C_RESET}")
    print(f"{C_BLUE}║{C_RESET}                                                            {C_BLUE}║{C_RESET}")
    
    print(f"{C_BLUE}╠════════════════════════════════════════════════════════════╣{C_RESET}")
    print(f"{C_BLUE}║{C_RESET}    [ {C_RED}0{C_RESET} ] Salir del sistema                                 {C_BLUE}║{C_RESET}")
    print(f"{C_BLUE}╚════════════════════════════════════════════════════════════╝{C_RESET}")
    print("")

    try:
        opcion = input(f"{C_BOLD}Seleccione una opción [{C_GREEN}0-15{C_RESET}{C_BOLD}]: {C_RESET}")
        opcion = int(opcion)
    except ValueError:
        limpiar_consola()
        mostrar_encabezado("SISTEMA DE GESTIÓN DE SEGUROS")
        print(f"\n{C_RED}  [!] ¡Error! Debes ingresar un número entero.{C_RESET}")
        input(f"{C_BOLD}Presiona Enter para reintentar...{C_RESET}")
        continue

    # ==========================
    # RUTEO DEL MENÚ
    # ==========================
    if opcion == 1:
        usuarios = usuario(usuarios)
    elif opcion == 2:
        vehiculos = vehiculo(usuarios, vehiculos)
    elif opcion == 3:
        polizas = poliza(usuarios, vehiculos, polizas)
    elif opcion == 4:
        siniestros = siniestro(vehiculos, polizas, siniestros)
    elif opcion == 5:
        consultar_usuario(usuarios, polizas)
    elif opcion == 6:
        listar_usuarios(usuarios, polizas)
    elif opcion == 7:
        consultar_vehiculo_por_patente(vehiculos, usuarios, polizas)
    elif opcion == 8:
        listar_vehiculos(vehiculos, usuarios, polizas)
    elif opcion == 9:
        consultar_poliza(polizas)
    elif opcion == 10:
        listar_polizas(polizas)
    elif opcion == 11:
        consultar_siniestro(siniestros)
    elif opcion == 12:
        listar_siniestros(siniestros)
    elif opcion == 13:
        mostrar_monto_polizas(polizas)
    elif opcion == 14:
        mostrar_monto_siniestros(siniestros)
    elif opcion == 15:
        mostrar_balance_general(polizas, siniestros)
    elif opcion == 0:
        limpiar_consola()
        print(f"{C_CYAN}╔════════════════════════════════════════════════════════════╗{C_RESET}")
        print(f"{C_CYAN}║           Gracias por utilizar el sistema. ¡Adiós!         ║{C_RESET}")
        print(f"{C_CYAN}╚════════════════════════════════════════════════════════════╝{C_RESET}\n")
        break
    else:
        limpiar_consola()
        mostrar_encabezado("SISTEMA DE GESTIÓN DE SEGUROS")
        print(f"\n{C_RED}  [!] Opción no válida. Elige un número del 0 al 15.{C_RESET}")
        input(f"{C_BOLD}Presiona Enter para reintentar...{C_RESET}")