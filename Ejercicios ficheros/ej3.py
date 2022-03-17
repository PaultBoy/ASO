import random

def linea_aleatoria(fichero):
    lineas_limpias = list()
    with open(fichero, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            stripped_line=line.strip()
            lineas_limpias.append(stripped_line)
    texto_unido = ''.join(lineas_limpias)
    texto_separado_por_puntos = texto_unido.split(".")
    return random.choice(texto_separado_por_puntos)
    
numCeledonio = 0

for i in range(10):
    linea = linea_aleatoria("la_regenta.txt")
    if linea.find("Celedonio") != -1:
        print(linea)
        numCeledonio=numCeledonio+1
print("Total Celedonios: ",numCeledonio)
