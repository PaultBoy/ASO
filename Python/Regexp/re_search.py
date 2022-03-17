import re

st = "Madrid es maravillosa"

#if re.search("^Huesca", st):
#En ocasiones es recomendable escribir r para que sepa evitar errores
if re.search(r"maravillosa$", st):
    print("Patrón localizado")
else:
    print("Patrón no encontrado")