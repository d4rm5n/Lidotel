import re
from datetime import datetime

# Constantes
ARCHIVO_INDIVIDUAL = "individual.txt"
ARCHIVO_ACOMPANADO = "acompanado.txt"
ARCHIVO_GRUPO_FAMILIA = "grupo_familia.txt"
SEPARADOR = "|"

# Variables globales
TIPOS_RESERVACION = ["Individual", "Acompañado", "Grupo/Familia"]
precios_habitaciones = {
    "FAMILY ROOM": 200,
    "SENCILLA": 60,
    "DOBLE": 120,
    "SUITE": 300
}

# Esta función crea los archivos si no existen
def inicializar_archivos():
    archivos = [ARCHIVO_INDIVIDUAL, ARCHIVO_ACOMPANADO, ARCHIVO_GRUPO_FAMILIA]
    
    for archivo in archivos:
        try:
            with open(archivo, 'a') as f:
                pass
        except:
            print(f"Error al crear el archivo {archivo}")
    
    print("Sistema inicializado correctamente.")

# Limpia la pantalla imprimiendo varias líneas en blanco
def limpiar_pantalla():
    print("\n" * 50)

# Muestra un mensaje de despedida
def mostrar_despedida():
    print("\n¡Gracias por utilizar el Sistema de Reservaciones!")
    print("Hotel Lidotel Boutique Margarita")
    print("Desarrollado por: [Tu Nombre]")
    print("Fecha: 31/03/2025")
    print("Versión: 1.0")

# Esta función me ayuda a validar números
def validar_numero(mensaje, tipo="entero"):
    while True:
        try:
            entrada = input(mensaje)
            
            if tipo == "entero":
                valor = int(entrada)
            else:  # Debe ser float
                valor = float(entrada)
                
            return valor
        except ValueError:
            print("Error: Debe ingresar un número válido.")

# Valida el formato del email usando expresiones regulares
def validar_email(email):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, email) is not None

# Valida que el teléfono tenga el formato correcto
def validar_telefono(telefono):
    patron = r'^\d{10,11}$'
    return re.match(patron, telefono) is not None

# Valida que la cédula tenga el formato correcto
def validar_cedula(cedula):
    patron = r'^\d{7,10}$'
    return re.match(patron, cedula) is not None

# Valida que el nombre tenga el formato correcto
def validar_nombre(nombre):
    if not nombre.strip():
        return False
    # Permitir letras y espacios
    for c in nombre:
        if not (c.isalpha() or c.isspace()):
            return False
    return True

# Función para obtener los datos de un cliente
def obtener_datos_cliente():
    print("\n--- Registro de Cliente ---")
    
    while True:
        nombre = input("Nombre: ")
        if validar_nombre(nombre):
            break
        print("Error: El nombre debe contener solo letras y espacios.")
    
    while True:
        apellido = input("Apellido: ")
        if validar_nombre(apellido):
            break
        print("Error: El apellido debe contener solo letras y espacios.")
    
    while True:
        cedula = input("Número de cédula: ")
        if validar_cedula(cedula):
            break
        print("Error: La cédula debe contener entre 7 y 10 dígitos.")
    
    while True:
        email = input("Email: ")
        if validar_email(email):
            break
        print("Error: Formato de email inválido.")
    
    while True:
        telefono = input("Número de teléfono: ")
        if validar_telefono(telefono):
            break
        print("Error: El teléfono debe tener 10 u 11 dígitos.")
    
    dias_estadia = validar_numero("Días de estadía: ", "entero")
    
    return {
        "nombre": nombre,
        "apellido": apellido,
        "cedula": cedula,
        "email": email,
        "telefono": telefono,
        "dias_estadia": dias_estadia
    }

# Función para obtener los datos de un niño
def obtener_datos_nino():
    while True:
        nombre = input("Nombre: ")
        if validar_nombre(nombre):
            break
        print("Error: El nombre debe contener solo letras y espacios.")
    
    while True:
        apellido = input("Apellido: ")
        if validar_nombre(apellido):
            break
        print("Error: El apellido debe contener solo letras y espacios.")
    
    while True:
        edad = validar_numero("Edad: ", "entero")
        if 0 <= edad <= 17:  # Rango razonable para niños
            break
        print("Error: La edad debe estar entre 0 y 17 años.")
    
    return {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad
    }

# Muestra los tipos de habitaciones disponibles
def mostrar_habitaciones():
    print("\n--- Tipos de Habitaciones ---")
    print("1. FAMILY ROOM - 200$ por noche")
    print("   Cálida y confortable habitación decorada con un estilo vanguardista...")
    print("2. SENCILLA - 60$ por noche")
    print("   Amplia y confortable habitación decorada con un estilo vanguardista...")
    print("3. DOBLE - 120$ por noche")
    print("   Amplia y confortable habitación decorada con un estilo vanguardista...")
    print("4. SUITE - 300$ por noche")
    print("   Cálida y confortable habitación decorada con un estilo vanguardista...")

# Función para que el usuario seleccione una habitación
def seleccionar_habitacion():
    habitaciones = {
        1: {"tipo": "FAMILY ROOM", "precio": 200, "descripcion": "Cálida y confortable habitación..."},
        2: {"tipo": "SENCILLA", "precio": 60, "descripcion": "Amplia y confortable habitación..."},
        3: {"tipo": "DOBLE", "precio": 120, "descripcion": "Amplia y confortable habitación..."},
        4: {"tipo": "SUITE", "precio": 300, "descripcion": "Cálida y confortable habitación..."}
    }
    
    mostrar_habitaciones()
    
    while True:
        opcion = validar_numero("\nSeleccione el tipo de habitación (1-4): ", "entero")
        if 1 <= opcion <= 4:
            return habitaciones[opcion]
        print("Error: Seleccione una opción válida (1-4).")

# Verifica si existen registros previos
def verificar_registros_existentes(tipo_reservacion):
    if tipo_reservacion == "Individual":
        nombre_archivo = ARCHIVO_INDIVIDUAL
    elif tipo_reservacion == "Acompañado":
        nombre_archivo = ARCHIVO_ACOMPANADO
    else:  # Grupo/Familia
        nombre_archivo = ARCHIVO_GRUPO_FAMILIA
    
    try:
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            
            if lineas:
                print(f"\nSe encontraron {len(lineas)} registros previos de tipo {tipo_reservacion}.")
            else:
                print(f"\nNo hay registros previos de tipo {tipo_reservacion}.")
    except:
        print(f"\nNo hay registros previos de tipo {tipo_reservacion}.")

# Guarda los datos en el archivo correspondiente
def guardar_datos(tipo_reservacion, datos):
    if tipo_reservacion == "Individual":
        nombre_archivo = ARCHIVO_INDIVIDUAL
    elif tipo_reservacion == "Acompañado":
        nombre_archivo = ARCHIVO_ACOMPANADO
    else:  # Grupo/Familia
        nombre_archivo = ARCHIVO_GRUPO_FAMILIA
    
    # Agrego fecha y hora de registro
    datos["fecha_registro"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        with open(nombre_archivo, 'a') as archivo:
            # Datos del cliente principal
            linea = f"{datos['cliente']['cedula']}{SEPARADOR}"
            linea += f"{datos['cliente']['nombre']}{SEPARADOR}"
            linea += f"{datos['cliente']['apellido']}{SEPARADOR}"
            linea += f"{datos['cliente']['email']}{SEPARADOR}"
            linea += f"{datos['cliente']['telefono']}{SEPARADOR}"
            linea += f"{datos['cliente']['dias_estadia']}{SEPARADOR}"
            
            # Datos de la habitación
            linea += f"{datos['habitacion']['tipo']}{SEPARADOR}"
            linea += f"{datos['habitacion']['precio']}{SEPARADOR}"
            
            # Fecha de registro
            linea += f"{datos['fecha_registro']}{SEPARADOR}"
            
            # Datos específicos según el tipo de reservación
            if tipo_reservacion == "Acompañado" and "acompanante" in datos:
                linea += f"{datos['acompanante']['cedula']}{SEPARADOR}"
                linea += f"{datos['acompanante']['nombre']}{SEPARADOR}"
                linea += f"{datos['acompanante']['apellido']}{SEPARADOR}"
                linea += f"{datos['acompanante']['email']}{SEPARADOR}"
                linea += f"{datos['acompanante']['telefono']}{SEPARADOR}"
            
            elif tipo_reservacion == "Grupo/Familia":
                # Cantidad de adultos adicionales
                if "adultos" in datos and datos["adultos"]:
                    linea += f"{len(datos['adultos'])}{SEPARADOR}"
                    for adulto in datos["adultos"]:
                        linea += f"{adulto['cedula']}{SEPARADOR}"
                        linea += f"{adulto['nombre']}{SEPARADOR}"
                        linea += f"{adulto['apellido']}{SEPARADOR}"
                else:
                    linea += f"0{SEPARADOR}"
                
                # Cantidad de niños
                if "ninos" in datos and datos["ninos"]:
                    linea += f"{len(datos['ninos'])}{SEPARADOR}"
                    for nino in datos["ninos"]:
                        linea += f"{nino['nombre']}{SEPARADOR}"
                        linea += f"{nino['apellido']}{SEPARADOR}"
                        linea += f"{nino['edad']}{SEPARADOR}"
                else:
                    linea += f"0{SEPARADOR}"
            
            archivo.write(linea + "\n")
        
        # Obtengo el índice del registro guardado
        registros = cargar_datos(tipo_reservacion)
        return len(registros) - 1
    
    except Exception as e:
        print(f"Error al guardar datos: {e}")
        return -1

# Carga los datos desde el archivo correspondiente
def cargar_datos(tipo_reservacion):
    if tipo_reservacion == "Individual":
        nombre_archivo = ARCHIVO_INDIVIDUAL
    elif tipo_reservacion == "Acompañado":
        nombre_archivo = ARCHIVO_ACOMPANADO
    else:  # Grupo/Familia
        nombre_archivo = ARCHIVO_GRUPO_FAMILIA
    
    registros = []
    
    try:
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            
            for linea in lineas:
                campos = linea.strip().split(SEPARADOR)
                
                if not campos:
                    continue
                
                # Datos del cliente principal
                cliente = {
                    "cedula": campos[0],
                    "nombre": campos[1],
                    "apellido": campos[2],
                    "email": campos[3],
                    "telefono": campos[4],
                    "dias_estadia": int(campos[5])