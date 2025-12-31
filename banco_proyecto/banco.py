# ═════════════════════════════════════════════════════════════
# FUNCIONES DEL BANCO - banco. py
# ═════════════════════════════════════════════════════════════

from random import random
from cliente import Cliente, cuentas, vips
from config import (
    NUMERO_MINIMO_DIGITOS, NUMERO_MAXIMO_CUENTA,
    LONGITUD_PASSWORD_MIN, LONGITUD_PASSWORD_MAX,
    CONTRASENA_ADMIN, NOMBRE_ADMIN, APELLIDO_ADMIN,
    BALANCE_ADMIN_INICIAL, PASSWORD_ADMIN
)
from utils import validar_numero, validar_texto, formatear_dinero, esperar_enter

# Conjunto para almacenar numeros de cuenta generados
numeros_cuentas = set()


def tiene_cuenta():
    """Pregunta si el usuario tiene una cuenta existente o necesita crear una"""
    resp = ''
    while resp not in ["s", "n", "salir"]:
        resp = input('Ya tiene una cuenta?\nSi(s) o No(n): ').lower()

    if resp == 'n':
        crear_cliente()
    elif resp == 's':
        print('A continuacion ingrese los datos solicitados para iniciar sesion')
        dato1 = input('Por favor, ingrese su numero de cuenta: ')

        if dato1 == 'admin':
            # Login como administrador
            contrasena = input('Contrasena: ')
            if contrasena == CONTRASENA_ADMIN:
                cuentas['admin'].menu_admin()
            else:
                print('Contrasena de admin incorrecta')
                esperar_enter()
                tiene_cuenta()

        else:
            try:
                numero_cuenta = int(dato1)
                if numero_cuenta in cuentas.keys():
                    cuentas[numero_cuenta].log_in()
                else:
                    print('La cuenta no existe o hubo un error')
                    esperar_enter()
                    tiene_cuenta()
            except ValueError:
                print('Numero de cuenta invalido')
                esperar_enter()
                tiene_cuenta()

    elif resp == 'salir':
        print('Haz salido del programa con exito')


def crear_cliente():
    """Crea una nueva cuenta bancaria"""
    num = 'No estoy listo'

    # Generar un numero de cuenta unico
    while num not in numeros_cuentas:
        num = round(random() * NUMERO_MAXIMO_CUENTA)
        if len(str(num)) < NUMERO_MINIMO_DIGITOS:
            continue
        elif num in numeros_cuentas:
            continue
        else:
            numeros_cuentas.add(num)

    # Solicitar datos del usuario
    print("═" * 60)
    print("CREAR NUEVA CUENTA")
    print("═" * 60)

    nombre = validar_texto('Introduzca su nombre: ')
    apellido = validar_texto(f'Bien {nombre}, ahora su apellido:  ')

    try:
        balance = int(input('Por ultimo, el saldo que desea ingresar a su nueva cuenta: '))
        if balance < 0:
            print('El saldo no puede ser negativo')
            esperar_enter()
            crear_cliente()
            return
    except ValueError:
        print('Saldo invalido')
        esperar_enter()
        crear_cliente()
        return

    print(
        f'Muy bien, todo listo, su nuevo numero de cuenta es {num}, por favor anotelo, de perderlo, no podra recuperar su cuenta')
    esperar_enter()

    # Solicitar contrasena segura
    password = ''
    while len(password) < LONGITUD_PASSWORD_MIN or len(password) > LONGITUD_PASSWORD_MAX:
        password = input(
            f'Ahora, elija una contrasena segura, entre {LONGITUD_PASSWORD_MIN} y {LONGITUD_PASSWORD_MAX} caracteres: ')
        if len(password) < LONGITUD_PASSWORD_MIN or len(password) > LONGITUD_PASSWORD_MAX:
            print(f'La contrasena debe tener entre {LONGITUD_PASSWORD_MIN} y {LONGITUD_PASSWORD_MAX} caracteres')

    # Crear la cuenta
    cuentas[num] = Cliente(nombre, apellido, balance, password, num)
    print(f'\nCuenta creada exitosamente!')
    print(f'Numero de cuenta: {num}')
    print(f'Nombre: {nombre} {apellido}')
    print(f'Balance inicial: {formatear_dinero(balance)}')
    esperar_enter()

    # Mostrar menu de acciones
    cuentas[num].menu_acciones()


def inicializar_banco():
    """Inicializa el banco creando la cuenta del admin"""
    cuentas['admin'] = Cliente(
        NOMBRE_ADMIN,
        APELLIDO_ADMIN,
        BALANCE_ADMIN_INICIAL,
        PASSWORD_ADMIN,
        'admin'
    )
    print('Banco inicializado correctamente')
