# ═════════════════════════════════════════════════════════════
# PUNTO DE ENTRADA DEL PROGRAMA - main.py
# ═════════════════════════════════════════════════════════════

from cliente import cuentas, vips
from banco import tiene_cuenta, inicializar_banco
from persistencia import (
    guardar_cuentas, cargar_cuentas,
    guardar_historial_vip, cargar_historial_vip,
    hacer_backup
)
from utils import limpiar_pantalla


def main():
    """Funcion principal que inicia el programa"""

    limpiar_pantalla()
    print("═" * 60)
    print("BIENVENIDO AL BANCO DIGITAL")
    print("═" * 60)
    print()

    # Inicializar banco (crear cuenta admin)
    inicializar_banco()
    print()

    # Cargar datos previos si existen
    print("Cargando datos del banco...")
    cargar_cuentas(cuentas)
    cargar_historial_vip(vips)
    print()

    # Iniciar programa principal
    try:
        tiene_cuenta()
    except KeyboardInterrupt:
        print("\n\n¡Interrupcion del usuario detectada!")
    except Exception as e:
        print(f"\n✗ Error inesperado: {e}")
    finally:
        # Guardar datos antes de cerrar
        print("\nGuardando datos...")
        hacer_backup()
        guardar_cuentas(cuentas)
        guardar_historial_vip(vips)
        print("✓ Datos guardados correctamente")
        print("\n¡Gracias por usar el Banco Digital!")
        print("═" * 60)


if __name__ == "__main__":
    main()