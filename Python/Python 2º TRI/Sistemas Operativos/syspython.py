import sys
if sys.platform == 'linux':
    print("Estoy en Linux")
elif sys.platform == 'win32':
    print("Ahora estoy en Windows")

print(sys.argv[0])

""" if len(sys.argv) != 2:
    print("Error: tienes que ejecutarlo sin argumentos")
    sys.exit()
elif sys.argv[1] == "3":
    print("El argumento 0 es el nombre del fichero") """

print("Longitud de los args: ",len(sys.argv))
print(sys.argv[1:4])