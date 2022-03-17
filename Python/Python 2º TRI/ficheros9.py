with open("/etc/passwd","r") as f:
    mlines = f.readlines()
    for line in mlines:
        stripped_line = line.strip()
        cutted_field = stripped_line.split(":")[6]
        print(cutted_field)