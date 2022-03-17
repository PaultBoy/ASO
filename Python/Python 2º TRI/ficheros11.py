#variación del 8. Imprimir solo los del /bin/bash
with open("/etc/passwd","r") as f:
    for line in f:
        stripped_line = line.strip()
        if stripped_line.endswith("/bin/bash") == True:
            print(stripped_line.split(":")[0:6])