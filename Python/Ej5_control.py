#Implementa un script en Python que muestre por la salida estándar si el usuario
# ha introducido un carácer en mayúsculas, minúsculas, número o carácter especial.
#Si el usuario no introduce un único carácter el script deberá mostrar un mensaje
# de error
#Nota: Python dispone de varios métodos incluidos para realizar estas comprobaciones

string = input("Introduzca un carácter: ")
# El bucle while-else sirve, en este caso, para control de errores sin necesidad de cerrar el programa
while not len(string) == 1:
    string = input("Debes introducir un carácter: ")
else:
    if string.isupper():
        print(string, "Mayúsculas");
    elif string.islower():
        print(string, "Minúsculas")
    elif string.isnumeric():
        print(string, "Número")
    else:
        print(string," Carácter especial")

