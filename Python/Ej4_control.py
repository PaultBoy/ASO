#Vamos a mejorar el script del ejercicio 2 incluyendo control de errores
# Se quiere evitar que el usuario ponga una letra en vez de meter un número y,
# además, debes seguir preguntándole hasta que escriba la edad bien (con dígitos).
# Nota: Python dispone de un método para comprobar si se han introducido dígitos.
nombre = input("¿Cómo se llama? ")
edad = input("¿Cuántos años tiene? ")
#isdigit() comprueba que un valor de una variable string es un número en realidad
while not edad.isdigit():
    edad = input("Introduzca un dígito: ")
else:
    edad = int(edad)
if edad < 25:
    print("Buenos días, alumno "+nombre)
elif edad <= 65:
    print("Buenos días, profesor "+nombre)
else:
    print("Feliz jubilación, "+nombre)