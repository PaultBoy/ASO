import subprocess
#Asignamos la salida del subprocess.run a una variable
#Empleamos el atributo DEVNULL para referirnos a /dev/null
#/dev/null es un dispositivo especial que es "la nada"
out = subprocess.check_output(["ls","."])
#usamos el returncode para saber si se ha ejecutado OK
#Muestra salida como string
#print(out)
#Salida la muestra convertida en una cadena
#print(out.decode())
strout = out.decode()
lst = strout.split()
print(lst)

#if out.returncode == 0:
#    print("Ejecutado OK")
#else:
#    print("Ejecutado MAL")