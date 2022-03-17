#Implementar un script que calcule los divisores de un número entero introducido por 
# el usuario. Al terminar el script, deberá indicar si el número es primo o no.
integer = input("Introduce un entero: ")
primo = True
while not integer.isnumeric():
        integer = input("Introduce, por favor, un entero: ")
else:
        integer = int(integer)
        print("Divisor: ", 1)
        for div in range(2,integer):
                if integer % div == 0:
                    primo = False
                    print("Divisor:", div) 
        print("Divisor:", integer)   
        if primo:
                print("El número", integer , "es primo")
        else:
                print("El número", integer , "no es primo")
        
