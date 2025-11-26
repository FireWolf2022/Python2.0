from pathlib import Path, PureWindowsPath

archivo = Path("/home/leo/PycharmProjects/PythonProject/Dia_6/archivo.txt")
print(archivo.read_text())

ruta_windows = PureWindowsPath(archivo)
print(ruta_windows)