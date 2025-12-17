# ═════════════════════════════════════════════════════════════
# FUNCIONES UTILITARIAS - utils.py
# ═════════════════════════════════════════════════════════════

import os
from config import ANCHO_LINEA_DECORATIVA, CARACTER_DECORATIVO

def limpiar_pantalla():
    """Limpia la pantalla de la consola"""
    os.system('cls' if os.name == 'nt' else 'clear')

def linea_decorativa(texto=""):
    """Dibuja una linea decorativa con texto opcional"""
    if texto:
        print(f"{texto}". center(ANCHO_LINEA_DECORATIVA, CARACTER_DECORATIVO))
    else:
        print(CARACTER_DECORATIVO * ANCHO_LINEA_DECORATIVA)

def validar_numero(prompt, minimo=None, maximo=None):
    """Valida que el usuario ingrese un numero valido"""
    while True:
        try:
            numero = int(input(prompt))
            if minimo is not None and numero < minimo:
                print(f"El numero debe ser mayor a {minimo}")
                continue
            if maximo is not None and numero > maximo:
                print(f"El numero debe ser menor a {maximo}")
                continue
            return numero
        except ValueError:
            print("Por favor ingrese un numero valido")

def validar_texto(prompt):
    """Valida que el usuario ingrese texto (no vacio)"""
    while True:
        texto = input(prompt).strip()
        if texto:
            return texto
        print("El campo no puede estar vacio")

def formatear_dinero(cantidad):
    """Formatea un numero como dinero con separadores de miles"""
    return f"${cantidad:,.2f}"

def esperar_enter():
    """Pausa el programa hasta que el usuario presione Enter"""
    input("Presione Enter para continuar...")