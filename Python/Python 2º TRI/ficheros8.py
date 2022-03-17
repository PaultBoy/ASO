#Modificacion del 7
#cortamos por un delimitador concreto la linea
with open("/etc/passwd","r") as f:
    for line in f:
        stripped_line = line.strip()
        cutted_field = stripped_line.split(":")
        print(cutted_field)