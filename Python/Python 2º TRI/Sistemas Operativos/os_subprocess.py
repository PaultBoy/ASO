import subprocess
#Asignamos la salida del subprocess.run a una variable
#Empleamos el atributo DEVNULL para referirnos a /dev/null
#/dev/null es un dispositivo especial que es "la nada"
varl = subprocess.run(["ls","."], stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
#usamos el returncode para saber si se ha ejecutado OK

if varl.returncode == 0:
    print("Ejecutado OK")
else:
    print("Ejecutado MAL")