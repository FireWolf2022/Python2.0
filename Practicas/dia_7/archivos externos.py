from pathlib import Path
directorio = Path(Path.cwd(), "Practicas", "dia_7")

if Path(directorio, "base").exists:
    print("El directorio existe")
else:
    Path(directorio, "base").mkdir()
    print("La carpeta fue creada con exito")
