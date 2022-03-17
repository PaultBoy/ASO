#Escribe un programa en Python que solicite al usuario su nombre y su edad.
# Si la edad es menor de 25 años, diremos que es un alumno y, si no, que es 
# un profesor. Si la edad es mayor de 65 al saludarle le desearemos una buena
# jubilación. Esto es, debes dirigirte al usuario con educación y discriminando
# el saludo si es alumno, profesor o jubilado
nombre = input("¿Cómo se llama? ")
edad = int(input("¿Cuántos años tiene? "))

if edad < 25:
    print("Buenos días, alumno "+nombre)
elif edad <= 65:
    print("Buenos días, profesor "+nombre)
else:
    print("Feliz jubilación, "+nombre)