def lee_fichero(fichero):
    with open(fichero,"r", encoding="utf-8") as f:
        lines = f.readlines()
        #Versión de José Miguel
        #print("".join(lines))
        #Esta solución de arriba une los elementos de una lista en un solo string
        for line in lines:
            linea_limpia=line.strip()
            print(linea_limpia)

archivo = input("Escribe archivo a escribir: ")
lee_fichero(archivo)
