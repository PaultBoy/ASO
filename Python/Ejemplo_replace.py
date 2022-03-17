## Ejemplo para ver el funcionamiento de replace() en un string.
#string.replace(buscar,reemplazar,nº ocurrencias)
#replace() no modifica por defecto la variable original
#Sólo se pueden reemplazar las ocurrencias empezando por la primera
#-1 reemplaza todas las ocurrencias
str="El aliento de mi gato huele a comida de gato"
str = str.replace("gato","perro",1)
print(str.replace("gato","perro"))
print(str)
