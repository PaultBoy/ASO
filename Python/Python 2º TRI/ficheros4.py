with open("/etc/passwd","r") as f:
    mlines = f.readlines()
    for line in mlines:
        stripped_line = line.strip()
#Imprime todos los elementos de la lista (Print dentro del for)
        print(stripped_line)