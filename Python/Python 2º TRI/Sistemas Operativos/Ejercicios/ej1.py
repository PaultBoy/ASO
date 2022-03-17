from asyncio import subprocess
import sys
import subprocess
import os

archivo = input("Introduce ruta de archivo a verificar: ")

print("Se ejecuta en ", sys.platform)
try:
    if sys.platform == "linux":
        os.system("uname -r")
        os.system("pwd")
        os.system("ls .")
    
    else:
        subprocess.run(["powershell", "pwd"])
        subprocess.run(["powershell", "ls", "."])

    if not os.path.exists(archivo):
        raise ValueError
except ValueError:
    print("El archivo ",archivo," no existe")