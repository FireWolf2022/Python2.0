# ═════════════════════════════════════════════════════════════
# PERSISTENCIA DE DATOS - persistencia.py
# ═════════════════════════════════════════════════════════════

import json
import os
from datetime import datetime
from config import (
    ARCHIVO_CUENTAS, ARCHIVO_HISTORIAL_VIP, ARCHIVO_AUDITORIA
)


def guardar_cuentas(cuentas):
    """Guarda todas las cuentas en un archivo JSON"""
    try:
        datos_cuentas = {}
        for num, cliente in cuentas.items():
            if num != 'admin':
                datos_cuentas[str(num)] = {
                    'nombre': cliente.nombre,
                    'apellido': cliente.apellido,
                    'balance': cliente.balance,
                    'password': cliente.password,
                    'vip': cliente.vip
                }
            else:
                # Guardar cuenta admin
                datos_cuentas['admin'] = {
                    'nombre': cliente.nombre,
                    'apellido': cliente.apellido,
                    'balance': cliente.balance,
                    'password': cliente.password,
                    'vip': False
                }

        with open(ARCHIVO_CUENTAS, 'w', encoding='utf-8') as f:
            json.dump(datos_cuentas, f, indent=4, ensure_ascii=False)
        print(f"✓ Cuentas guardadas exitosamente en {ARCHIVO_CUENTAS}")
        return True
    except Exception as e:
        print(f"✗ Error al guardar cuentas:   {e}")
        return False


def cargar_cuentas(cuentas):
    """Carga todas las cuentas desde el archivo JSON"""
    try:
        if not os.path.exists(ARCHIVO_CUENTAS):
            print(f"Archivo {ARCHIVO_CUENTAS} no encontrado.  Iniciando con cuentas vacias.")
            return False

        with open(ARCHIVO_CUENTAS, 'r', encoding='utf-8') as f:
            datos_cuentas = json.load(f)

        # Importar aqui para evitar circular imports
        from cliente import Cliente

        for num, info in datos_cuentas.items():
            if num == 'admin':
                num_key = 'admin'
            else:
                num_key = int(num)

            cliente = Cliente(
                info['nombre'],
                info['apellido'],
                info['balance'],
                info['password'],
                num_key
            )
            cliente.vip = info.get('vip', False)
            cuentas[num_key] = cliente

        print(f"✓ Cuentas cargadas exitosamente desde {ARCHIVO_CUENTAS}")
        return True
    except Exception as e:
        print(f"✗ Error al cargar cuentas:  {e}")
        return False


def guardar_historial_vip(vips):
    """Guarda el historial de transacciones de usuarios VIP"""
    try:
        datos_vips = {}
        for num, historial in vips.items():
            datos_vips[str(num)] = historial

        with open(ARCHIVO_HISTORIAL_VIP, 'w', encoding='utf-8') as f:
            json.dump(datos_vips, f, indent=4, ensure_ascii=False)
        print(f"✓ Historial VIP guardado exitosamente")
        return True
    except Exception as e:
        print(f"✗ Error al guardar historial VIP: {e}")
        return False


def cargar_historial_vip(vips):
    """Carga el historial de transacciones de usuarios VIP"""
    try:
        if not os.path.exists(ARCHIVO_HISTORIAL_VIP):
            print(f"Archivo {ARCHIVO_HISTORIAL_VIP} no encontrado.")
            return False

        with open(ARCHIVO_HISTORIAL_VIP, 'r', encoding='utf-8') as f:
            datos_vips = json.load(f)

        for num, historial in datos_vips.items():
            vips[int(num)] = historial

        print(f"✓ Historial VIP cargado exitosamente")
        return True
    except Exception as e:
        print(f"✗ Error al cargar historial VIP: {e}")
        return False


def registrar_auditoria(accion, usuario, detalles=""):
    """Registra una accion en el archivo de auditoria"""
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        registro = f"[{timestamp}] Usuario: {usuario} | Accion: {accion} | Detalles: {detalles}\n"

        with open(ARCHIVO_AUDITORIA, 'a', encoding='utf-8') as f:
            f.write(registro)
        return True
    except Exception as e:
        print(f"✗ Error al registrar en auditoria: {e}")
        return False


def cargar_auditoria():
    """Carga y muestra el archivo de auditoria (solo admin)"""
    try:
        if not os.path.exists(ARCHIVO_AUDITORIA):
            print("No hay registros de auditoria aun.")
            return

        with open(ARCHIVO_AUDITORIA, 'r', encoding='utf-8') as f:
            registros = f.readlines()

        print("═" * 80)
        print("REGISTRO DE AUDITORIA")
        print("═" * 80)
        for registro in registros:
            print(registro.strip())
        print("═" * 80)
    except Exception as e:
        print(f"✗ Error al cargar auditoria: {e}")


def hacer_backup():
    """Crea un backup de todos los archivos de datos"""
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        carpeta_backup = f"backup_{timestamp}"

        if not os.path.exists(carpeta_backup):
            os.makedirs(carpeta_backup)

        archivos = [ARCHIVO_CUENTAS, ARCHIVO_HISTORIAL_VIP, ARCHIVO_AUDITORIA]

        for archivo in archivos:
            if os.path.exists(archivo):
                with open(archivo, 'r', encoding='utf-8') as f:
                    contenido = f.read()
                with open(f"{carpeta_backup}/{archivo}", 'w', encoding='utf-8') as f:
                    f.write(contenido)

        print(f"✓ Backup creado exitosamente en carpeta: {carpeta_backup}")
        return True
    except Exception as e:
        print(f"✗ Error al crear backup: {e}")
        return False


def limpiar_datos():
    """Elimina todos los archivos de datos (CUIDADO)"""
    try:
        confirmacion = input("Esto eliminara todos los datos del banco.  Escriba 'SI' para confirmar: ")
        if confirmacion.upper() == 'SI':
            archivos = [ARCHIVO_CUENTAS, ARCHIVO_HISTORIAL_VIP, ARCHIVO_AUDITORIA]
            for archivo in archivos:
                if os.path.exists(archivo):
                    os.remove(archivo)
            print("✓ Todos los datos han sido eliminados")
            return True
        else:
            print("Operacion cancelada")
            return False
    except Exception as e:
        print(f"✗ Error al limpiar datos: {e}")
        return False