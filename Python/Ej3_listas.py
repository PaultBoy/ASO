# Implementa un programa en Python que muestre por la salida estándar la palabra
# de mayor longitud de una lista de 3 strings que estará prefijada en el código del
# script y siempre será la misma

lst = ["Paulo", "Cohelo", "Reverte"]

leng = 0
string = ""
for i in range(len(lst)):
    if len(lst[i]) >= leng:
        leng = len(lst[i])

for j in range(len(lst)):
    if len(lst[j]) == leng:
        string = lst[j]

print(leng, string)