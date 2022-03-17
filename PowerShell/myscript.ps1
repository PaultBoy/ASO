# Si quieres forzar un tipo de valor para una variable, 
#has de especificarlo entre corchetes antes de la variable
[int] $age = Read-Host "Por favor, introduce tu edad: "
Write-Host $age

#En powershell todo son objetos
$loc = Get-Variable
Write-Host $loc
#Obtener tipos de variables
$age.GetType()

#Cómo acceder a la lista de variables de entorno
Get-ChildItem Env:
#Llamar a las variables de entorno
$env:COMPUTERNAME

Get-Location | Get-Member -Type Properties

#Obtener servicios

Get-Service | Get-Member -Type Property
#Elegir columnas a mostrar con Select-Object
Get-Service | Select-Object Status,DisplayName
Get-Service | Select-Object Status,DisplayName -First 3
Get-Service | Select-Object Status,DisplayName -Last 3 

#Realizar grep en powershell, para poder obtener valores concretos (con Where-Object)
Get-Service | Where-Object { $_.Name -eq "wuauserv" }
Get-Service | Where-Object { $_.Status -ne "Running" } | Select-Object DisplayName
# -like te permite buscar palabras que cumplan patrones, no palabras exactas
Get-Service | Where-Object { $_.Status -like "Run*"}
# -notlike busca lo que no coincide con el patrón especificado
Get-Service | Where-Object { $_.Name -notlike "E*"}
# Con -or , -and, -xor o -not puedes concatenar condiciones a cumplir
Get-Service | Where-Object { $_.Name -like "E*" -and $_.Status -eq "Running" }

Get-Service | Where-Object { $_.Name -like "E*" -and $_.Status -eq "Running" } | Select-Object Status, Name, StartType, DisplayName