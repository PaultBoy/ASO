#Realiza un programa donde se pidan números indefinidamente y pare cuando el número
# que se ha introducido sea menor a la suma de los dos anteriores


num1 = input("Por favor, introduce el primer número: ")
while not num1.isnumeric():
    num1 = input("Por favor, introduce el primer número: ")
else:
    num2 = input("Por favor, introduce el segundo número: ")
    while not num2.isnumeric():
        num2 = input("Por favor, introduce el segundo número: ")
    else:
        num3 = input("Por favor, introduce el tercer número: ")
        while not num3.isnumeric():
            num3 = input("Por favor, introduce el tercer número: ")
        else:
            num1 = int(num1)
            num2 = int(num2)
            num3 = int(num3)
            while num3 >= num1 + num2:
                num1=num2
                num2=num3
                num3=input("Por favor, introduce algún número: ")
                while not num3.isnumeric():
                    num3=input("Por favor, introduce algún NÚMERO: ")
                else:
                    num3=int(num3)

