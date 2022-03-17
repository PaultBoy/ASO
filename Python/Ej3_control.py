#Escribe un programa en Python que reciba un año por la entrada estándar y
# devuelva si es un año bisiesto o no.
#El programa deberá informar al usuario si introduce un valor de año no válido
# considerando que el calendario gregoriano data de 1582
#Nota: Un año bisiesto es divisible por 4. Sin embargo, un año divisible por 100 es un año bisiesto
# si es divisible por 400 también

anyo = int(input("Escribe un año: "))

if anyo % 4 == 0 and anyo >= 1582:
    if anyo % 100 == 0:
        if anyo % 400 == 0:
            print("Año bisiesto")
        else:
            print("Año no bisiesto")
    else:
        print("Año bisiesto") 
elif anyo % 4 != 0 and anyo >= 1582:
    print("Año no bisiesto")
else:
    print("Fecha antigua")