with open("/etc/passwd","r") as f:
    for line in f:
        stripped_line = line.strip()
        print(stripped_line)