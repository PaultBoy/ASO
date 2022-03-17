#Implementa un script que introducido un string por la entrada estándar muestre
#por la salida estándar los dos caracteres centrales de dicho string.
#Si el string tiene una longitud impar deberá mostrar un único carácter central.
# Sin embargo, un string de longitud par deberá mostrar los dos caracteres centrales.
# Si introduce un string vacío deberá mostrar un aviso al usuario.
#Ejemplo:
# Para la entrada HUESCA deberá devolver ES. Para la entrada GUARA deberá devolver A.

str = input("Introduce una cadena de caracteres: ")

while len(str) == 0:
    str= input("No se admiten cadenas vacías: ")
else:
    cent=''
    for c in range(len(str)):
        if len(str)%2 == 1 and len(str)//2 == c:
            cent=str[c]
        elif len(str)%2 == 0 and len(str)/2 == c:
            cent=str[c-1] + str[c]
print(cent)

#Solución alternativa
# Mitad = len(str) // 2;
# elif len(str) % 2 == 0:
#   print(str[Mitad - 1:Mitad + 1])
# else:
#   print(str[Mitad:Mitad+1])