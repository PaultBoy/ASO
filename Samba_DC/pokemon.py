import pandas
#Marco de datos (data frame) para leer archivos
df = pandas.read_csv("/root/pokemon.csv")
# En PowerShell: $df = Import-Csv -Path "pokemon.csv"

# Pruebas de prints con el DATAFRAME
#print(df.columns) # Llamar a todas las columnas
#print(df.columns[1]) #accede a valor de la columna 1
#print(df.values) #Muestra los valores del CSV
#print(df) #Saca todos los valores en forma de listas

lst = df.values.tolist() #Almacena todas las filas de valores en forma de listas para cada fila, siendo 
                         # en sí una lista que contiene todas
#print(lst)

#Muestra por pantalla el nombre de cada uno de los pokemon
#for item in lst:
#    print(item[1])

#Mostrar los pokemon con ataque > 150

for item in lst:
    if item[5] > 150:
        print(item[1])