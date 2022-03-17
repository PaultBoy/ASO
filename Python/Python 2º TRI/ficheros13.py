#escribir contenido en unfichero
with open("lineas.txt","w") as f:
    #f.write("Este es un fichero de lineas")
    print("Este es mi fichero",file=f)