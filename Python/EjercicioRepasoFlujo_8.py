num1 = input("Introduce el primer número: ")
while not num1.isnumeric():
    num1 = input("Introduce el primer NÚMERO: ")
else:
    num2 = input("Introduce el segundo número: ")
    while not num2.isnumeric():
        num2 = input("Introduce el segundo NÚMERO: ")
    else:
        num1int = int(num1)
        num2int = int(num2)
        if num1int > num2int:
            for i in range(num1int,num2int,3):
                print(i)
        elif num2int > num1int:
            for j in range(num2int,num1int,3):
                print(j)
        else:
            print("No se mostrará ningún número")