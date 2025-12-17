# ═════════════════════════════════════════════════════════════
# CLASE CLIENTE - cliente.py
# ═════════════════════════════════════════════════════════════

from config import (
    NUMERO_DONACION, MENSAJE_VIP, MENSAJE_BIENVENIDA,
    MENSAJE_LOGUEADO, MENSAJE_CONTRASENA_INCORRECTA,
    MENSAJE_TRANSFERENCIA_EXITOSA, MENSAJE_ERROR_NUMERO,
    MENSAJE_FONDOS_INSUFICIENTES, LONGITUD_PASSWORD_MIN,
    LONGITUD_PASSWORD_MAX
)
from utils import validar_numero, validar_texto, formatear_dinero, esperar_enter

# Diccionarios globales para almacenar cuentas e historial VIP
cuentas = {}
vips = {}


class Cliente:
    """Clase que representa un cliente del banco"""

    cuenta_actual = None

    def __init__(self, nombre, apellido, balance, password, num) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.balance = balance
        self.password = password
        self.num = num
        self.vip = False

    def log_in(self):
        """Verifica la contrasena del usuario"""
        dato2 = input(f'Bien {self.nombre}, ahora verifiquemos la contrasena antes de seguir: ')
        if dato2 == self.password:
            print(MENSAJE_LOGUEADO)
            self.menu_acciones()
        else:
            print(MENSAJE_CONTRASENA_INCORRECTA)
            esperar_enter()

    def menu_acciones(self):
        """Menu principal con opciones de operaciones bancarias"""
        print('A continuacion se le mostraran una serie de acciones que puede realizar:  ')
        op = -1
        print(
            "Opciones:\n1-Mostrar la informacion del usuario\n2-Depositar\n3-Retirar\n4-Transferir\n5-Historial (VIPs only)\n6-Salir")

        while True:
            try:
                op = int(input('Que desea hacer:  '))
            except ValueError:
                print('Ha ocurrido un error, intentelo de nuevo')
                continue

            match op:
                case 1:
                    self.info()
                case 2:
                    self.depositar()
                case 3:
                    self.retirar()
                case 4:
                    self.transferir()
                case 5:
                    if self.vip:
                        self.historial()
                    else:
                        print('Esta opcion solo esta disponible para miembros VIP')
                        esperar_enter()
                case 6:
                    break
                case _:
                    print('Ha ocurrido un error')
                    continue

            op = input('Desea seguir realizando cambios? : ').lower()
            if op in ['no', 'n']:
                break

    def info(self):
        """Muestra la informacion del usuario"""
        print(f'{self.nombre} {self.apellido}, # {self.num}, Balance actual: {formatear_dinero(self.balance)}')
        esperar_enter()

    def depositar(self):
        """Realiza un deposito en la cuenta"""
        try:
            deposito = int(input('Cuanto desea depositar? : '))
            if deposito > 0:
                self.balance += deposito
                print(f'Deposito realizado con exito, monto actual {formatear_dinero(self.balance)}')
                if self.vip:
                    vips[self.num].append(
                        f"El usuario ha realizado un deposito de {formatear_dinero(deposito)}.  Balance actual: {formatear_dinero(self.balance)}")
            else:
                print('Ha ocurrido un error, el deposito debe ser mayor a 0')
        except ValueError:
            print('La cifra solo debe contener caracteres numericos')
        esperar_enter()

    def retirar(self):
        """Realiza un retiro de la cuenta"""
        print(f'Balance actual: {formatear_dinero(self.balance)}')
        try:
            retiro = int(input('Cuanto desea retirar: '))
            if retiro <= self.balance:
                self.balance -= retiro
                print(f'Balance actual:  {formatear_dinero(self.balance)}')
                if self.vip:
                    vips[self.num].append(
                        f'El usuario ha retirado {formatear_dinero(retiro)}. Balance de la cuenta {formatear_dinero(self.balance)}')
            else:
                print('Ha ocurrido un error, no puede retirar mas de lo que tiene en la cuenta')
        except ValueError:
            print('La cifra solo debe contener caracteres numericos')
        esperar_enter()

    def transferir(self):
        """Realiza una transferencia a otra cuenta"""
        print(f"Bien {self.nombre}, a continuacion se le mostraran las cuentas disponibles para la transferencia:")
        for i in cuentas.keys():
            if i != 'admin':
                print(f"# Cuenta:  {i}, Propietario: {cuentas[i].nombre} {cuentas[i].apellido}")

        print(f"Ingrese 000 para realizar una donacion".center(60, "-"))

        try:
            a = int(input("Ingrese el # de cuenta a la que desea realizar la transferencia: "))
            b = int(input(f"Ingrese la cantidad que desea transferir, dispone de {formatear_dinero(self.balance)}: "))

            if b <= self.balance:
                if a == 000:
                    # Donacion para ser VIP
                    if not self.vip:
                        print(f"Muchas gracias {self.nombre}, usted a decidido realizar una donacion : )")
                        cuentas['admin'].balance += b
                        self.balance -= b
                        self.vip = True
                        vips[self.num] = [MENSAJE_VIP]
                        print(
                            "Estimado cliente, gracias por su donacion, como regalo, hemos desbloqueado su cuenta VIP!! !, disfrute...")
                    else:
                        print("Gracias por su donacion, estamos muy agradecidos!! !")
                        vips[self.num].append(
                            f"El usuario ha realizado una donacion de {formatear_dinero(b)}, balance de la cuenta:  {formatear_dinero(self.balance)}")
                        cuentas['admin'].balance += b
                        self.balance -= b

                elif a in cuentas.keys():
                    cuentas[a].balance += b
                    self.balance -= b
                    if self.vip:
                        vips[self.num].append(
                            f"El usuario ha realizado una transferencia de {formatear_dinero(b)} al usuario {cuentas[a].nombre} {cuentas[a].apellido} #{cuentas[a].num}")
                    print(
                        f"Transferencia realizada con exito, balance actual:  {formatear_dinero(self.balance)}, balance de cuenta beneficiada: {formatear_dinero(cuentas[a].balance)}")
                else:
                    print("Cuenta no encontrada")
            else:
                print(f"No puede transferir un monto mayor del que dispone T:{b}, M:{formatear_dinero(self.balance)}")
        except ValueError:
            print(MENSAJE_ERROR_NUMERO)
        esperar_enter()

    def historial(self):
        """Muestra el historial de transacciones para usuarios VIP"""
        print(f"Historial de acciones de la cuenta #{self.num}")
        if len(vips[self.num]) == 1:
            print(f"1-{vips[self.num][0]}")
        else:
            for a, b in enumerate(vips[self.num], 1):
                print(f'{a}-{b}')
        esperar_enter()

    def info_admin(self):
        """Muestra informacion de todas las cuentas (solo admin)"""
        print("═" * 60)
        print("INFORMACION DE CUENTAS DEL BANCO")
        print("═" * 60)
        for client in cuentas.keys():
            if client != 'admin':
                print(
                    f'# Cuenta: {client}, {cuentas[client].nombre} {cuentas[client].apellido}, Balance: {formatear_dinero(cuentas[client].balance)}')
        print("═" * 60)
        esperar_enter()

    def menu_admin(self):
        """Menu de administrador para gestionar el banco"""
        while True:
            print('Que deseas hacer Leo')
            print(
                '1-Mostrar cuentas existentes\n2-Realizar una transferencia\n3-Mostrar datos de la cuenta admin\n4-Salir')
            try:
                op = int(input('#: '))
                match op:
                    case 1:
                        self.info_admin()
                    case 2:
                        self.info_admin()
                        print("Ingresa '0' para salir.")
                        try:
                            a = int(input('Elija el numero de cuenta que desea editar: '))
                            if a == 0:
                                continue
                            b = int(input(
                                f"Cuanto desea transferir?, esta cuenta dispone de {formatear_dinero(cuentas[a].balance)}: "))
                            if b <= cuentas[a].balance:
                                cuentas[a].balance -= b
                                cuentas['admin'].balance += b
                                print(
                                    f'Transferencia realizada con exito, monto final de la cuenta seleccionada: {formatear_dinero(cuentas[a].balance)}')
                            else:
                                print('No se puede ser tan ambicioso')
                        except (ValueError, KeyError):
                            print("Error al procesar la transferencia")
                        esperar_enter()
                    case 3:
                        print(f'Balance del admin: {formatear_dinero(cuentas["admin"].balance)}')
                        esperar_enter()
                    case 4:
                        break
                    case _:
                        print('Opcion invalida')
            except ValueError:
                print("Por favor ingrese un numero valido")