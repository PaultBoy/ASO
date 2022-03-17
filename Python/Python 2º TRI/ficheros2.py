with open("/etc/passwd","r") as f:
    multi_lines = f.readlines()
    print(multi_lines)