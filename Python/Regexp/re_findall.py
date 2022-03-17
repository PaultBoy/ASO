import re

st = "Mis 2 números favoritos son 13 y 48"

lst = re.findall("[0-9]+",st)
print(lst)