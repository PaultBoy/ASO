#Implementa un script que reciba por la entrada estándar el nombre del usuario
#y los compare con el tuyo. Deberas darle la bienvenida al curso, pero se lo
#dirás de manera especial si se llama como tú: "Bienvenido al curso de ASO tocay@"

nombre = input("¿Cómo te llamas? ")

if nombre != "Pablo":
    print("Bienvenido al curso de ASO " + nombre)
else:  
    print("Bienvenido al curso de ASO tocay@")
