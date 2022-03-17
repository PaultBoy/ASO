#Modifica el ejercicio anterior de manera que el usuario introduzca por la entrada estándar las palabras que desea
#comprobar.
#El script deberá devolver la longitd de la palabra más larga que ha introducido y la cantidad de palabras que 
#ha introducido.
#Nota: El script detectará que el usuario ha dejado de introducir palabras
# cuando el usuario introduzca una cadena compuesta únicamente de un punto"."
palabra=""
palabras=""
while palabra != ".":
    palabra = input("Introduzca palabra: ")
    palabras = palabras + " "+ palabra
lst2 = palabras.split()
leng = 0
string = ""
for i in range(len(lst2)):
    if len(lst2[i]) >= leng:
        leng = len(lst2[i])

for j in range(len(lst2)):
    if len(lst2[j]) == leng:
        string = lst2[j]
print("Palabra más larga del conjunto (", lst2, ")", string)