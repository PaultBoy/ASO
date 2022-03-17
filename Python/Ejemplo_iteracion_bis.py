#Ejemplo de iterar usando el indice range
str1="Hello World"
str2=""
# Char en este caso se almacena como un índice, no moco un carácter, ya que se lo ha metido en range
for char in range (0,len(str1)):
    if str1[char] == " ":
        str2 += "*"
    else:
        str2 += str1[char]
print(str2)