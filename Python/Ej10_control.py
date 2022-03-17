#Implementa un script en Python que calcule el factorial de un número introducido
# por la entrada estándar.

num = input("Por favor, introduce un número: ")
numOrig = num
while not num.isnumeric():
    num = input("Por favor, introduce un NÚMERO: ")
else:
    num = int(num)
    if num == 0:
        print(numOrig,"!","=", 1)
    elif num == 1:
        print(numOrig,"!","=", 1)
    elif num < 0:
        print("No existe factorial de números menores que 0")
    else:
        for n in range(num-1,1,-1):
            num = num * n
        print(numOrig,"!","=", num)
