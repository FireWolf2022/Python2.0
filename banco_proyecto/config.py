# ═════════════════════════════════════════════════════════════
# CONFIGURACIÓN DEL BANCO - config.py
# ═════════════════════════════════════════════════════════════

# 🔐 CREDENCIALES ADMIN
CONTRASENA_ADMIN = 'lp2006'
NOMBRE_ADMIN = 'The Fucking Boss'
APELLIDO_ADMIN = 'Here'
BALANCE_ADMIN_INICIAL = 1000000
PASSWORD_ADMIN = 'AllForMe'

# 💳 CONFIGURACIÓN DE DONACIONES/VIP
NUMERO_DONACION = 0  # Número de cuenta especial para donar
BONUS_DONACION_MINIMO = 100  # Monto mínimo para ser VIP
MENSAJE_VIP = "El cliente se ha convertido en VIP"

# 💰 CONFIGURACIÓN DE TRANSACCIONES
COMISION_TRANSFERENCIA_INTERNACIONAL = 0.02  # 2%
MINIMO_DEPOSITO = 1
MINIMO_RETIRO = 1

# 🎯 CONFIGURACIÓN DE CUENTAS
NUMERO_MINIMO_DIGITOS = 4  # Numeros de cuenta deben tener al menos 4 digitos
LONGITUD_PASSWORD_MIN = 4
LONGITUD_PASSWORD_MAX = 8
NUMERO_MAXIMO_CUENTA = 10000  # random() * 10000

# 📊 MENSAJES DEL SISTEMA
MENSAJE_BIENVENIDA = "Bienvenido al Banco Digital"
MENSAJE_LOGUEADO = "Usted se ha logueado con exito"
MENSAJE_CONTRASENA_INCORRECTA = "Contraseña incorrecta ! !"
MENSAJE_TRANSFERENCIA_EXITOSA = "Transferencia realizada con exito"
MENSAJE_ERROR_NUMERO = "Error al intentar identificar el numero de cuenta"
MENSAJE_FONDOS_INSUFICIENTES = "No puede transferir un monto mayor del que dispone"

# 📁 ARCHIVOS DE PERSISTENCIA
ARCHIVO_CUENTAS = 'cuentas.json'
ARCHIVO_HISTORIAL_VIP = 'historial_vip.json'
ARCHIVO_AUDITORIA = 'auditoria.log'

# ✨ OTRAS CONFIGURACIONES
ANCHO_LINEA_DECORATIVA = 60
CARACTER_DECORATIVO = "-"