#Ejemplo iteración con un bucle for

str1="Hello World"
str2=""

for char in str1:
    if char == " ":
        str2 += "*"
    else:
        str2 += char
print(str2)