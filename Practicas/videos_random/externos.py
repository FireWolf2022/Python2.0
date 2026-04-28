from pathlib import Path

def dispositivos_externos():
    externos = Path("/media/leo")
    if externos.exists():
        dispositivos = list(externos.iterdir())
        print("Dispositivos :")
        for index,item in enumerate(dispositivos,1):
            print(index, item.stem)
        
    else:
        print("Error al intentar encontrar el usuario...")
        return
    
    op = -1
    print("Elija uno de los dispositivos disponibles")
    while True:
        try:
            op = int(input("$-"))
            if op not in [i for i in range(1,len(dispositivos)+1)]:
                print("Elija un opcion valida")
                continue
        except:
            print("Por favor elija una opcion valida")
            continue
        
        match(op):
            case 1:
            #Antes de mandar a llamar la funcion hay que verificar que tipo de dispositivo es (mobil o memoria)
                usb(dispositivos[op - 1])
        

    
    

def usb(device):
    print(device.stem)
