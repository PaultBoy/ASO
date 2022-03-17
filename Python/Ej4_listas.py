# Dado un string de palabras prefijado en el string, obtén la longitud de la palabra más corta que contiene.

lst = "Paulo Cohelo Reverte"
lst2 = lst.split()
leng = 0
string = ""
for i in range(len(lst2)):
    if len(lst2[i]) >= leng:
        leng = len(lst2[i])

for k in range(len(lst2)):
    if len(lst2[k]) <= leng:
        leng = len(lst2[k])

for l in range(len(lst2)):
    if len(lst2[l]) == leng:
        string = lst2[l]
print(leng, string)

