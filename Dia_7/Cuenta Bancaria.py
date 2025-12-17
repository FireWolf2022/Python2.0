from random import random
cuentas = {}
vips = {}
class Cliente:
    cuenta_actual = None

    """
    *1- Falta agregar la opcion de VIP a cada accion y mostrarla para el usuario vip   
    *2- Pedir una contraseña para el usuario admin pa que sea mas realista, por lo demas creo que esta bien
    3- Intentar crear archivos para guardar las cuentas, y cuando se cierre y abra el programa no se pierdan
    """
    
    def __init__(self, nombre, apellido, balance, password, num) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.balance = balance
        self.password = password
        self.num = num
        self.vip = False
        
    def log_in(self):
        dato2 = input(f'Bien {self.nombre}, ahora verifiquemos la contraseña antes de seguir: ')
        if dato2 == self.password:
            print("Usted se ha logueado con exito")
            self.menu_acciones()
        else:
            print('Contraseña incorrecta !!')
              
    def menu_acciones(self):
        print('A continuacion se le mostraran una serie de acciones que puede realizar: ')
        op = -1
        print("Opciones:\n1-Mostrar la informacion del usuario\n2-Depositar\n3-Retirar\n4-Transferir\n5-Historial (VIPs only)\n6-Salir")
        while True:
            try:
                op = int(input('Que desea hacer: '))
            except ValueError:
                print('Ha ocurrido un error, intentelo de nuevo')
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
                        input()
                case 6:
                    tiene_cuenta()
                    break
                case _:
                    print('Ha ocurrido un error')
                    continue
            op = input('Desea seguir realizando cambios? :').lower()
            if op in ['no', 'n']:
                break
        
    def info(self):
        print(f'{self.nombre} {self.apellido}, # {self.num}, Balance actual: {self.balance}')
        input()

    def depositar(self):
        deposito = input('Cuanto desea depositar? :')
        try:
            deposito = int(deposito)
            if deposito > 0:
                self.balance += deposito
                print(f'Deposito realizado con exito, monto actual {self.balance}')
            else:
                print('Ha ocurrido un error, el deposito debe ser mayor a 0')
            if self.vip:
                vips[self.num].append(f"El usuario ha realizado un depostio de {deposito}. Balance actual: {cuentas[self.num].balance}")
        except ValueError:
            print('La cifra solo debe contener caracteres numericos')
        input()
                      
    def retirar(self):
        print(f'Balance actual: {self.balance}')
        retiro = input('Cuanto desea retirar:')
        try:
            retiro = int(retiro)
            if retiro <= self.balance:
                self.balance -= retiro
                print(f'Balance actual: {self.balance}')
            else:
                print('Ha ocurrido un error, no puede retirar mas de lo que tiene en la cuenta')
            if self.vip:
                vips[self.num].append(f'El usuario ha retirado ${retiro}.Balance de la cuenta {cuentas[self.num].balance}')

        except ValueError:
            print('La cifra solo debe contener caracteres numericos')
        input()
    
    def transferir(self):
        print(f"Bien {self.nombre}, a continuación se le mostraran las cuentas disponibles para la transferencia:")
        for i in cuentas.keys():
            print(f"# Cuentas: {i}, Propietario: {cuentas[i].nombre} {cuentas[i].apellido}")
        print(f"Ingrese 000 para realizar una donacion".center(60, "-"))
        try:
            a = int(input("Ingrese el # de cuenta a la que desea realizar la transferencia: "))
            b = int(input(f"Ingrese la cantidad que desea transferir, dispone de {self.balance}: "))
            if b <= self.balance:
                if a == 000:
                    if not self.vip:
                        print(f"Muchas gracias {self.nombre}, usted a decidido realizar una donacion :)")
                        cuentas['admin'].balance += b
                        self.balance -= b
                        self.vip = True
                        vips[self.num] = ["El cliente se ha convertido en VIP"]
                        print("Estimado cliente, gracias por su donacion, como regalo, hemos desbloqueado su cuenta VIP!!!, disfrute...")
                    else:
                        print("Gracias por su donacion, estamos muy agradecidos!!!")
                        vips[self.num].append(f"El usuario ha realizado una donacion de {b}, balance de la cuenta: {self.balance}")
                        cuentas['admin'].balance += b
                        self.balance -= b


            elif a in cuentas.keys():
                cuentas[a].balance += b
                self.balance -= b
                if self.vip:
                    vips[self.num].append(f"El usuario ha realizado una transferencia de ${b} al usuario {cuentas[a].nombre} {cuentas[a].apellido} #{cuentas[a].num}")
                print(f"Transferencia realizada con exito, balance actual: {self.balance}, balance de cuenta beneficiada: {cuentas[a].balance}")
            else:
                print(f"No puede transferir un monto mayor del que dispone T:{b}, M:{self.balance}")
        except ValueError:
            print("Error al intentar identificar el numero de cuenta")
        input()

    def historial(self):
        print(f"Historial de acciones de la cuenta #{self.num}")
        if len(vips[self.num]) == 1:
            print(f"1-{vips[self.num][0]}")
        else:
            for a,b in enumerate(vips[self.num],1):
                print(f'{a}-{b}')

    #Esta funcion esta aqui por gusto pero no la borro por si acaso :)
    @staticmethod
    def salir():
        tiene_cuenta()
    
    def admin(self):
        print('Que deseas hacer Leo')
        while True:
            print('1-Mostrar cuentas existentes\n2-Realizar una transferencia\n3-Mostrar datos de la cuenta admin\n4-Salir')
            op = int(input('#:'))
            match int(op):
                case 1:
                    self.info_admin()
                case 2:
                    self.info_admin()
                    print("Ingresa '0' para salir.")
                    a = int(input('Elija el numero de cuenta que desea editar: '))
                    if a == 0:
                        self.admin()
                    b = int(input(f"Cuanto daño desea hacer?, esta cuenta dispone de {cuentas[a].balance} : "))
                    if b <= cuentas[a].balance:
                        cuentas[a].balance -= b
                        cuentas['admin'].balance += b
                        print(f'Transferencia realizada con exito, monto final de la cuenta seleccionada : {cuentas[a].balance}')
                    else:
                        print('No se puede ser tan ambicioso')
                case 3:
                    print(f'Balance: {cuentas["admin"].balance}')
                case 4:
                    break
        tiene_cuenta()

    @staticmethod
    def info_admin():
        for client in cuentas.keys():
                    if client != 'admin':
                        print(f'# Cuenta: {client}, {cuentas[client].nombre} {cuentas[client].apellido}, {cuentas[client].balance}')
                 
#Pa saber si tiene una cuenta o no, si no la tiene se le crea una, si ya tiene se va al logueo
def tiene_cuenta():
    resp = ''
    while resp not in ["s", "n", "salir"]:
        resp = input('Ya tiene una cuenta?\nSi(s) o No(n):').lower()
        
    if resp == 'n':
        crear_cliente()
    elif resp == 's':
        print('A continuacion ingrese los datos solicitados para iniciar secion')
        dato1 = input('Por favor, ingrese su numero de cuenta: ')
        if dato1 == 'admin':
            if input('Contraseña ??: ') == 'lp2006':
                cuentas['admin'].admin()
        
        elif int(dato1) in cuentas.keys():
            cuentas[int(dato1)].log_in()
        else:
            print('La cuenta no existe o hubo un error')
            tiene_cuenta()
            
    elif resp == 'salir':
        print('Haz salido del programa con exito')
    
#Crear la cuenta papu
numeros_cuentas = set()
def crear_cliente():
    num = 'No estoooy'
    while num not in numeros_cuentas:#Numero radomm
        num = round(random() * 10000)
        if len(str(num)) < 4:
            continue
        elif num in numeros_cuentas:
            continue
        else:
            numeros_cuentas.add(num)
    #Pidiendole los datos ak usuario para la cuenta
    nombre = input('Introduzca su nombre: ')
    apellido = input(f'Bien {nombre}, ahora su apellido: ')
    balance = input('Por ultimo, el saldo que desea ingresar a su nueva cuenta: ')
    print(f'Muy bien, todo listo, su nuevo numero de cuenta es {num}, por favor anotelo, de perderlo, no podra recuperar su cuenta')
    password = 0
    while len(str(password)) < 4 or len(str(password)) > 8:
        password = input('Ahora, elija una contrasenia segura, entre 4 y 8 caracteres: ')
    
    #posicion = len(Cliente.cuentas)
    #Cliente.cuentas[posicion] = Cliente()
    
    #Aqui se crea la cuenta o la instancia como te de la gana decirlo
    cuentas[num] = Cliente(nombre, apellido, int(balance), password, num)
    cuentas[num].menu_acciones()

cuentas['admin'] = Cliente('The Fucking Boss','Here', 1000000, 'AllForMe', 'admin')
tiene_cuenta()
