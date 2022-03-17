#variación. Imprimir solo los del /bin/bash
with open("/etc/passwd","r") as f:
    mlines = f.readlines()
    for line in mlines:
        stripped_line = line.strip()
        cutted_field = stripped_line.split(":")[6]
        #print(cutted_field)
        if cutted_field == "/bin/bash":
            print(stripped_line.split(":")[0])