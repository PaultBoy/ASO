#Implementa un script en Python en el que se borrarán el primer y el último carácter
#de un string introducido por la entrada estándar.
#El string resultante deberá ser mostrado por a salida estándar.
#Deberás comprobar que el usuario no introduzca un string de longitud 
#menor o igual a 2 caracteres.
str=input("Introduce un string: ")
while not len(str) > 2:
    str=input("Error. Introduzca una cadena más larga: ")
else:
    print(str[1:-1])