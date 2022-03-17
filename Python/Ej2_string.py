#Ejercicio 2 strings
#Implementa un script que muestre por la salida estándar un string formado
# por los dos primeros y los dos últimos caracteres de un string introducido por la salida estándar
#El script deberá mostrar un string vacío en caso de que la longitud del string introducido sea menor que dos

string = input("Introduce un string: ")
while not len(string) > 2:
    string = input("Introduce un string más largo: ")
else:
    strInicial = string[:2]
    strFinal = string[-2:]
    str = strInicial + strFinal
    print(str)

#if len(string) > 2:
#   print(string[:2] + string[-2:])
