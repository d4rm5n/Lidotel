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
                }
                
                # Datos de la habitación
                habitacion = {
                    "tipo": campos[6],
                    "precio": int(campos[7])
                }
                
                # Fecha de registro
                fecha_registro = campos[8]
                
                # Creo el registro base
                registro = {
                    "cliente": cliente,
                    "habitacion": habitacion,
                    "fecha_registro": fecha_registro
                }
                
                # Datos específicos según el tipo de reservación
                if tipo_reservacion == "Acompañado" and len(campos) > 9:
                    acompanante = {
                        "cedula": campos[9],
                        "nombre": campos[10],
                        "apellido": campos[11],
                        "email": campos[12],
                        "telefono": campos[13]
                    }
                    registro["acompanante"] = acompanante
                
                elif tipo_reservacion == "Grupo/Familia" and len(campos) > 9:
                    # Cantidad de adultos adicionales
                    cant_adultos = int(campos[9])
                    
                    if cant_adultos > 0:
                        adultos = []
                        indice = 10
                        
                        for i in range(cant_adultos):
                            adulto = {
                                "cedula": campos[indice],
                                "nombre": campos[indice + 1],
                                "apellido": campos[indice + 2]
                            }
                            adultos.append(adulto)
                            indice += 3
                        
                        registro["adultos"] = adultos
                        
                        # Cantidad de niños
                        if indice < len(campos):
                            cant_ninos = int(campos[indice])
                            indice += 1
                            
                            if cant_ninos > 0:
                                ninos = []
                                
                                for i in range(cant_ninos):
                                    nino = {
                                        "nombre": campos[indice],
                                        "apellido": campos[indice + 1],
                                        "edad": int(campos[indice + 2])
                                    }
                                    ninos.append(nino)
                                    indice += 3
                                
                                registro["ninos"] = ninos
                
                registros.append(registro)
    except:
        pass
    
    return registros

# Muestra los detalles de un registro
def mostrar_registro(registro, tipo_reservacion):
    print("\n=== Detalles del Registro ===")
    print(f"Tipo de Reservación: {tipo_reservacion}")
    print(f"Fecha de Registro: {registro['fecha_registro']}")
    
    print("\n--- Cliente Principal ---")
    print(f"Nombre: {registro['cliente']['nombre']} {registro['cliente']['apellido']}")
    print(f"Cédula: {registro['cliente']['cedula']}")
    print(f"Email: {registro['cliente']['email']}")
    print(f"Teléfono: {registro['cliente']['telefono']}")
    print(f"Días de Estadía: {registro['cliente']['dias_estadia']}")
    
    print("\n--- Habitación ---")
    print(f"Tipo: {registro['habitacion']['tipo']}")
    print(f"Precio por Noche: ${registro['habitacion']['precio']}")
    
    total = registro['cliente']['dias_estadia'] * registro['habitacion']['precio']
    print(f"Total a Pagar: ${total}")
    
    if tipo_reservacion == "Acompañado" and "acompanante" in registro:
        print("\n--- Acompañante ---")
        print(f"Nombre: {registro['acompanante']['nombre']} {registro['acompanante']['apellido']}")
        print(f"Cédula: {registro['acompanante']['cedula']}")
        print(f"Email: {registro['acompanante']['email']}")
        print(f"Teléfono: {registro['acompanante']['telefono']}")
    
    elif tipo_reservacion == "Grupo/Familia":
        if "adultos" in registro and registro["adultos"]:
            print(f"\n--- Adultos Adicionales ({len(registro['adultos'])}) ---")
            for i, adulto in enumerate(registro["adultos"], 1):
                print(f"{i}. {adulto['nombre']} {adulto['apellido']} - Cédula: {adulto['cedula']}")
        
        if "ninos" in registro and registro["ninos"]:
            print(f"\n--- Niños ({len(registro['ninos'])}) ---")
            for i, nino in enumerate(registro["ninos"], 1):
                print(f"{i}. {nino['nombre']} {nino['apellido']} - Edad: {nino['edad']}")

# Busca un cliente por nombre, apellido o cédula
def buscar_cliente(tipo_reservacion):
    registros = cargar_datos(tipo_reservacion)
    
    if not registros:
        print(f"No hay registros de tipo {tipo_reservacion}.")
        return None
    
    print("\n=== Buscar Cliente ===")
    print("1. Buscar por nombre")
    print("2. Buscar por apellido")
    print("3. Buscar por cédula")
    
    opcion = validar_numero("\nSeleccione una opción (1-3): ", "entero")
    
    if opcion == 1:  # Buscar por nombre
        nombre = input("\nIngrese el nombre a buscar: ")
        resultados = []
        
        for i, reg in enumerate(registros):
            if nombre.lower() in reg["cliente"]["nombre"].lower():
                resultados.append((i, reg))
    
    elif opcion == 2:  # Buscar por apellido
        apellido = input("\nIngrese el apellido a buscar: ")
        resultados = []
        
        for i, reg in enumerate(registros):
            if apellido.lower() in reg["cliente"]["apellido"].lower():
                resultados.append((i, reg))
    
    elif opcion == 3:  # Buscar por cédula
        cedula = input("\nIngrese la cédula a buscar: ")
        resultados = []
        
        for i, reg in enumerate(registros):
            if cedula == reg["cliente"]["cedula"]:
                resultados.append((i, reg))
    
    else:
        print("Opción inválida.")
        return None
    
    if not resultados:
        print("No se encontraron coincidencias.")
        return None
    
    print(f"\nSe encontraron {len(resultados)} coincidencias:")
    
    for i, (indice, reg) in enumerate(resultados, 1):
        print(f"{i}. {reg['cliente']['nombre']} {reg['cliente']['apellido']} - Cédula: {reg['cliente']['cedula']}")
    
    if len(resultados) == 1:
        seleccion = 1
    else:
        seleccion = validar_numero("\nSeleccione un cliente (1-" + str(len(resultados)) + "): ", "entero")
        
        if seleccion < 1 or seleccion > len(resultados):
            print("Selección inválida.")
            return None
    
    indice_seleccionado = resultados[seleccion - 1][0]
    registro_seleccionado = resultados[seleccion - 1][1]
    
    mostrar_registro(registro_seleccionado, tipo_reservacion)
    
    return indice_seleccionado

# Guarda todos los registros en un archivo
def guardar_todos_registros(tipo_reservacion, registros):
    if tipo_reservacion == "Individual":
        nombre_archivo = ARCHIVO_INDIVIDUAL
    elif tipo_reservacion == "Acompañado":
        nombre_archivo = ARCHIVO_ACOMPANADO
    else:  # Grupo/Familia
        nombre_archivo = ARCHIVO_GRUPO_FAMILIA
    
    try:
        # Crear una copia temporal
        nombre_temp = nombre_archivo + ".temp"
        
        with open(nombre_temp, 'w') as archivo:
            for reg in registros:
                # Datos del cliente principal
                linea = f"{reg['cliente']['cedula']}{SEPARADOR}"
                linea += f"{reg['cliente']['nombre']}{SEPARADOR}"
                linea += f"{reg['cliente']['apellido']}{SEPARADOR}"
                linea += f"{reg['cliente']['email']}{SEPARADOR}"
                linea += f"{reg['cliente']['telefono']}{SEPARADOR}"
                linea += f"{reg['cliente']['dias_estadia']}{SEPARADOR}"
                
                # Datos de la habitación
                linea += f"{reg['habitacion']['tipo']}{SEPARADOR}"
                linea += f"{reg['habitacion']['precio']}{SEPARADOR}"
                
                # Fecha de registro
                linea += f"{reg['fecha_registro']}{SEPARADOR}"
                
                # Datos específicos según el tipo de reservación
                if tipo_reservacion == "Acompañado" and "acompanante" in reg:
                    linea += f"{reg['acompanante']['cedula']}{SEPARADOR}"
                    linea += f"{reg['acompanante']['nombre']}{SEPARADOR}"
                    linea += f"{reg['acompanante']['apellido']}{SEPARADOR}"
                    linea += f"{reg['acompanante']['email']}{SEPARADOR}"
                    linea += f"{reg['acompanante']['telefono']}{SEPARADOR}"
                
                elif tipo_reservacion == "Grupo/Familia":
                    # Cantidad de adultos adicionales
                    if "adultos" in reg and reg["adultos"]:
                        linea += f"{len(reg['adultos'])}{SEPARADOR}"
                        for adulto in reg["adultos"]:
                            linea += f"{adulto['cedula']}{SEPARADOR}"
                            linea += f"{adulto['nombre']}{SEPARADOR}"
                            linea += f"{adulto['apellido']}{SEPARADOR}"
                    else:
                        linea += f"0{SEPARADOR}"
                    
                    # Cantidad de niños
                    if "ninos" in reg and reg["ninos"]:
                        linea += f"{len(reg['ninos'])}{SEPARADOR}"
                        for nino in reg["ninos"]:
                            linea += f"{nino['nombre']}{SEPARADOR}"
                            linea += f"{nino['apellido']}{SEPARADOR}"
                            linea += f"{nino['edad']}{SEPARADOR}"
                    else:
                        linea += f"0{SEPARADOR}"
                
                archivo.write(linea + "\n")
        
        # Renombrar el archivo temporal
        with open(nombre_temp, 'r') as temp:
            contenido = temp.read()
        
        with open(nombre_archivo, 'w') as final:
            final.write(contenido)
        
        # Intentar eliminar el archivo temporal
        try:
            with open(nombre_temp, 'w') as temp:
                pass  # Vaciar el archivo
        except:
            pass
        
        return True
    
    except Exception as e:
        print(f"Error al guardar los registros: {e}")
        return False

# Gestiona las opciones disponibles para un registro
def gestionar_opciones_registro(tipo_reservacion, indice):
    registros = cargar_datos(tipo_reservacion)
    
    if indice < 0 or indice >= len(registros):
        print("Índice de registro inválido.")
        return
    
    while True:
        print("\n=== Opciones de Registro ===")
        print("1. Ver registro anterior")
        print("2. Ver registro siguiente")
        print("3. Modificar datos del cliente")
        print("4. Añadir personas (solo para Grupo/Familia)")
        print("5. Terminar operación")
        
        opcion = validar_numero("\nSeleccione una opción (1-5): ", "entero")
        
        if opcion == 1:  # Ver registro anterior
            if indice > 0:
                indice -= 1
                mostrar_registro(registros[indice], tipo_reservacion)
            else:
                print("Este es el primer registro.")
                mostrar_registro(registros[indice], tipo_reservacion)
        
        elif opcion == 2:  # Ver registro siguiente
            if indice < len(registros) - 1:
                indice += 1
                mostrar_registro(registros[indice], tipo_reservacion)
            else:
                print("Este es el último registro.")
                mostrar_registro(registros[indice], tipo_reservacion)
        
        elif opcion == 3:  # Modificar datos del cliente
            print("\n=== Modificar Datos del Cliente ===")
            print("1. Nombre")
            print("2. Apellido")
            print("3. Email")
            print("4. Teléfono")
            print("5. Días de estadía")

                        
            sub_opcion = validar_numero("\nSeleccione el dato a modificar (1-5): ", "entero")
            
            if sub_opcion == 1:  # Modificar nombre
                while True:
                    nuevo_nombre = input("\nNuevo nombre: ")
                    if validar_nombre(nuevo_nombre):
                        registros[indice]["cliente"]["nombre"] = nuevo_nombre
                        break
                    print("Error: El nombre debe contener solo letras y espacios.")
            
            elif sub_opcion == 2:  # Modificar apellido
                while True:
                    nuevo_apellido = input("\nNuevo apellido: ")
                    if validar_nombre(nuevo_apellido):
                        registros[indice]["cliente"]["apellido"] = nuevo_apellido
                        break
                    print("Error: El apellido debe contener solo letras y espacios.")
            
            elif sub_opcion == 3:  # Modificar email
                while True:
                    nuevo_email = input("\nNuevo email: ")
                    if validar_email(nuevo_email):
                        registros[indice]["cliente"]["email"] = nuevo_email
                        break
                    print("Error: Formato de email inválido.")
            
            elif sub_opcion == 4:  # Modificar teléfono
                while True:
                    nuevo_telefono = input("\nNuevo teléfono: ")
                    if validar_telefono(nuevo_telefono):
                        registros[indice]["cliente"]["telefono"] = nuevo_telefono
                        break
                    print("Error: El teléfono debe tener 10 u 11 dígitos.")
            
            elif sub_opcion == 5:  # Modificar días de estadía
                nuevos_dias = validar_numero("\nNuevos días de estadía: ", "entero")
                registros[indice]["cliente"]["dias_estadia"] = nuevos_dias
            
            else:
                print("Opción inválida.")
                continue
            
            # Guardo los cambios
            if guardar_todos_registros(tipo_reservacion, registros):
                print("Datos modificados correctamente.")
                mostrar_registro(registros[indice], tipo_reservacion)
        
        elif opcion == 4:  # Añadir personas (solo para Grupo/Familia)
            if tipo_reservacion != "Grupo/Familia":
                print("Esta opción solo está disponible para reservaciones de tipo Grupo/Familia.")
                continue
            
            print("\n=== Añadir Personas ===")
            print("1. Añadir adulto")
            print("2. Añadir niño")
            
            sub_opcion = validar_numero("\nSeleccione una opción (1-2): ", "entero")
            
            if sub_opcion == 1:  # Añadir adulto
                print("\nDatos del nuevo adulto:")
                datos_adulto = obtener_datos_cliente()
                
                if "adultos" not in registros[indice]:
                    registros[indice]["adultos"] = []
                registros[indice]['adultos'].append(datos_adulto)
                
                # Guardo los cambios
                if guardar_todos_registros(tipo_reservacion, registros):
                    print("Adulto añadido correctamente.")
                    mostrar_registro(registros[indice], tipo_reservacion)
            
            elif sub_opcion == 2:  # Añadir niño
                print("\nDatos del nuevo niño:")
                datos_nino = obtener_datos_nino()
                
                if "ninos" not in registros[indice]:
                    registros[indice]["ninos"] = []
                registros[indice]['ninos'].append(datos_nino)
                
                # Guardo los cambios
                if guardar_todos_registros(tipo_reservacion, registros):
                    print("Niño añadido correctamente.")
                    mostrar_registro(registros[indice], tipo_reservacion)
        
        elif opcion == 5:  # Terminar operación
            mostrar_despedida()
            return None
        
        else:
            print("Opción inválida. Intente de nuevo.")

# Registra un cliente individual
def registrar_individual():
    limpiar_pantalla()
    
    print("\n=== Registro de Cliente Individual ===")
    
    # Verifico si existen registros previos
    verificar_registros_existentes("Individual")
    
    # Obtengo los datos del cliente
    datos_cliente = obtener_datos_cliente()
    
    # Pido al cliente que seleccione una habitación
    habitacion = seleccionar_habitacion()
    
    # Creo el registro completo
    registro = {
        "cliente": datos_cliente,
        "habitacion": habitacion
    }
    
    # Guardo los datos y obtengo el índice
    indice = guardar_datos("Individual", registro)
    
    # Muestro el registro
    mostrar_registro(registro, "Individual")
    
    # Devuelvo el tipo de reservación y el índice
    return "Individual", indice

# Registra un cliente acompañado
def registrar_acompanado():
    limpiar_pantalla()
    
    print("\n=== Registro de Cliente Acompañado ===")
    
    # Verifico si existen registros previos
    verificar_registros_existentes("Acompañado")
    
    # Obtengo los datos del cliente principal
    print("\nDatos del cliente principal:")
    datos_cliente = obtener_datos_cliente()
    
    # Obtengo los datos del acompañante
    print("\nDatos del acompañante:")
    datos_acompanante = obtener_datos_cliente()
    
    # Pido al cliente que seleccione una habitación
    habitacion = seleccionar_habitacion()
    
    # Creo el registro completo
    registro = {
        "cliente": datos_cliente,
        "acompanante": datos_acompanante,
        "habitacion": habitacion
    }
    
    # Guardo los datos y obtengo el índice
    indice = guardar_datos("Acompañado", registro)
    
    # Muestro el registro
    mostrar_registro(registro, "Acompañado")
    
    # Devuelvo el tipo de reservación y el índice
    return "Acompañado", indice

# Registra un grupo o familia
def registrar_grupo_familia():
    limpiar_pantalla()
    
    print("\n=== Registro de Grupo/Familia ===")
    
    # Verifico si existen registros previos
    verificar_registros_existentes("Grupo/Familia")
    
    # Obtengo los datos del cliente principal
    print("\nDatos del cliente principal:")
    datos_cliente = obtener_datos_cliente()
    
    # Pregunto si hay adultos adicionales
    hay_adultos = input("\n¿Hay adultos adicionales? (S/N): ").upper() == "S"
    adultos = []
    
    if hay_adultos:
        cant_adultos = validar_numero("¿Cuántos adultos adicionales? ", "entero")
        
        for i in range(cant_adultos):
            print(f"\nDatos del adulto adicional #{i+1}:")
            datos_adulto = obtener_datos_cliente()
            adultos.append(datos_adulto)
    
    # Pregunto si hay niños
    hay_ninos = input("\n¿Hay niños? (S/N): ").upper() == "S"
    ninos = []
    
    if hay_ninos:
        cant_ninos = validar_numero("¿Cuántos niños? ", "entero")
        
        for i in range(cant_ninos):
            print(f"\nDatos del niño #{i+1}:")
            datos_nino = obtener_datos_nino()
            ninos.append(datos_nino)
    
    # Pido al cliente que seleccione una habitación
    habitacion = seleccionar_habitacion()
    
    # Creo el registro completo
    registro = {
        "cliente": datos_cliente,
        "habitacion": habitacion
    }
    
    if adultos:
        registro["adultos"] = adultos
    
    if ninos:
        registro["ninos"] = ninos
    
    # Guardo los datos y obtengo el índice
    indice = guardar_datos("Grupo/Familia", registro)
    
    # Muestro el registro
    mostrar_registro(registro, "Grupo/Familia")
    
    # Devuelvo el tipo de reservación y el índice
    return "Grupo/Familia", indice

# Muestra el menú principal
def mostrar_menu_principal():
    print("\n=== Sistema de Reservaciones Hotel Lidotel Boutique Margarita ===")
    print("1. Registrar cliente individual")
    print("2. Registrar cliente acompañado")
    print("3. Registrar grupo/familia")
    print("4. Buscar cliente")
    print("5. Salir")

# Función principal
def main():
    # Inicializo los archivos
    inicializar_archivos()
    
    while True:
        limpiar_pantalla()
        mostrar_menu_principal()
        
        opcion = validar_numero("\nSeleccione una opción (1-5): ", "entero")
        
        if opcion == 1:  # Registrar cliente individual
            tipo, indice = registrar_individual()
            
            if indice >= 0:
                gestionar_opciones_registro(tipo, indice)
        
        elif opcion == 2:  # Registrar cliente acompañado
            tipo, indice = registrar_acompanado()
            
            if indice >= 0:
                gestionar_opciones_registro(tipo, indice)
        
        elif opcion == 3:  # Registrar grupo/familia
            tipo, indice = registrar_grupo_familia()
            
            if indice >= 0:
                gestionar_opciones_registro(tipo, indice)
        
        elif opcion == 4:  # Buscar cliente
            print("\n=== Buscar Cliente ===")
            print("1. Cliente individual")
            print("2. Cliente acompañado")
            print("3. Grupo/familia")
            
            sub_opcion = validar_numero("\nSeleccione el tipo de cliente (1-3): ", "entero")
            
            if sub_opcion == 1:  # Cliente individual
                indice = buscar_cliente("Individual")
                
                if indice is not None:
                    gestionar_opciones_registro("Individual", indice)
            
            elif sub_opcion == 2:  # Cliente acompañado
                indice = buscar_cliente("Acompañado")
                
                if indice is not None:
                    gestionar_opciones_registro("Acompañado", indice)
            
            elif sub_opcion == 3:  # Grupo/familia
                indice = buscar_cliente("Grupo/Familia")
                
                if indice is not None:
                    gestionar_opciones_registro("Grupo/Familia", indice)
            
            else:
                print("Opción inválida.")
        
        elif opcion == 5:  # Salir
            mostrar_despedida()
            break
        
        else:
            print("Opción inválida. Intente de nuevo.")

# Ejecuto la función principal
if __name__ == "__main__":
    main()