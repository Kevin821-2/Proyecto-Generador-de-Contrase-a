import random
import string

usuarios = {}

#MENU PRINCIPAL

def menu_principal():
    while True:
        print("==============================")
        print(" GENERADOR DE CONTRASEÑAS")
        print("==============================")
        print("1. Iniciar sesión")
        print("2. Crear cuenta")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            if iniciar_sesion():
                pantalla_generador()

        elif opcion == "2":
            crear_cuenta()

        elif opcion == "3":
            print("Cerrando aplicación...")
            print("FIN")
            break

        else:
            print("Opción incorrecta.")

menu_principal()

def crear_cuenta():
    print("\n--- CREAR CUENTA ---")
    usuario = input("Crea tu usuario: ")
    contrasena = input("Crea tu contraseña: ")
    confirmar = input("Confirma tu contraseña: ")

    if usuario in usuarios:
        print("Error: El usuario ya existe.")
    elif contrasena != confirmar:
        print("Error: Las contraseñas no coinciden.")
    else:
        usuarios[usuario] = contrasena
        print("Cuenta creada correctamente.")

def iniciar_sesion():
    print("\n--- INICIAR SESIÓN ---")
    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")

    if usuario not in usuarios:
        print("Error: Usuario no registrado.")
        return False

    if usuarios[usuario] != contrasena:
        print("Error: Contraseña incorrecta.")
        return False

    print("Inicio de sesión exitoso.")
    print("Bienvenido al sistema.")
    return True

def generar_contrasena(longitud, mayusculas, minusculas, numeros, simbolos):
    caracteres = ""

    if mayusculas:
        caracteres += string.ascii_uppercase

    if minusculas:
        caracteres += string.ascii_lowercase

    if numeros:
        caracteres += string.digits

    if simbolos:
        caracteres += "!@#$%^&*"

    if caracteres == "":
        return None

    contrasena = ""

    for i in range(longitud):
        contrasena += random.choice(caracteres)

    return contrasena

def solicitar_preferencias():
    print("\n--- PREFERENCIAS DE LA CONTRASEÑA ---")

    while True:
        longitud = int(input("Ingrese la longitud de la contraseña (8-128): "))

        if longitud >= 8 and longitud <= 128:
            break
        else:
            print("Error: La longitud debe estar entre 8 y 128.")

    mayusculas = input("¿Incluir mayúsculas? (si/no): ").lower() == "si"
    minusculas = input("¿Incluir minúsculas? (si/no): ").lower() == "si"
    numeros = input("¿Incluir números? (si/no): ").lower() == "si"
    simbolos = input("¿Incluir símbolos? (si/no): ").lower() == "si"

    if not mayusculas and not minusculas and not numeros and not simbolos:
        print("Error: Debes seleccionar al menos un tipo de carácter.")
        return solicitar_preferencias()

    return longitud, mayusculas, minusculas, numeros, simbolos

def pantalla_generador():
    ultima_contrasena = ""

    while True:
        preferencias = solicitar_preferencias()

        longitud = preferencias[0]
        mayusculas = preferencias[1]
        minusculas = preferencias[2]
        numeros = preferencias[3]
        simbolos = preferencias[4]

        ultima_contrasena = generar_contrasena(
            longitud,
            mayusculas,
            minusculas,
            numeros,
            simbolos
        )

        print("\nContraseña generada:", ultima_contrasena)

        while True:
            print("\n--- OPCIONES ---")
            print("1. Generar otra contraseña")
            print("2. Copiar al portapapeles")
            print("3. Ajustar preferencias")
            print("4. Cerrar sesión / Salir")

            opcion = input("Elige una opción: ")

            if opcion == "1":
                print("\nGenerando nueva contraseña con las mismas preferencias...")
                ultima_contrasena = generar_contrasena(
                    longitud,
                    mayusculas,
                    minusculas,
                    numeros,
                    simbolos
                )
                print("Contraseña generada:", ultima_contrasena)

            elif opcion == "2":
                print("Contraseña copiada al portapapeles:", ultima_contrasena)

            elif opcion == "3":
                print("Volviendo a la pantalla de preferencias...")
                break

            elif opcion == "4":
                print("Cerrando sesión y volviendo al menú principal...")
                return

            else:
                print("Opción incorrecta.")


