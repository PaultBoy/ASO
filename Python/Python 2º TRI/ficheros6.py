with open("lineas.txt","r") as f:
    for line in f:
        line = f.readline()
        print(line.strip())