with open("/etc/passwd","r") as f:
    mlines = f.readlines()
    for line in mlines:
        stripped_line = line.strip()
#Imprime ultimo elemento de la lista (Print fuera del for)
    print(stripped_line)