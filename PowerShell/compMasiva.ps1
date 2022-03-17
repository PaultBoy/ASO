try{
    $deptfile = Import-Csv "C:\Users\Administrador\Documents\Departamentos.csv"
}
catch {
    Write-Output "Error al importar el archivo"
}

# Cómo actuar ante excepciones
$ErrorActionPreference = "Stop" #SilentlyContinue: para no printar el mensaje de error por pantalla.
                                # Equivalente a llevar la salida a /dev/null
# Array de errores
# $error[1]
# ¿Qué se ha de ejecutar una vez?
# ¿Que se ha de ejecutar por cada línea del fichero - en el bucle?
foreach ($line in $deptfile){
    # Variables a utilizar en la iteración
    $departamento = $line.NombreDepartamento
    try{
        # En CSV los nombres de campos se llaman con punto, como los objetos
    # 1.1 - Crear el directorio compartido
    New-Item -Type Directory -Path ("C:\Compartida\" + $departamento)
    }
    catch [System.IO.IOException]{
        Write-Output "El directorio ya está creado"
    }
    try{
        # 1.2 - Crear grupos de AD, y que el nombre a mostrar sea el mismo que el de creación
        New-ADGroup -Name $departamento -GroupScope Global -DisplayName $departamento
    }
    catch{
        Write-Output "Grupo ya creado"
    }
    try {
        # 1.3 - Crear la compartición SMB de cada grupo y fichero.
        # Concatenar un string en Powershell se hace entre paréntesis si se pasa en forma de parámetro
        New-SmbShare -Name $departamento -Path ("C:\Compartida\" + $departamento) -ErrorAction Stop
    }
    catch {
        Write-Output "Compartición ya creada"
    }
    
    # 1.4 - Dar permisos de acceso a la compartición a cad grupo y eliminar a quien no debe acceder
    # Dar permisos de modificación al grupo de los departamentos
    Grant-SmbShareAccess -Name ($departamento) -AccountName $departamento -AccessRight Change -Force | Out-Null
    # Negar acceso a los usuarios no especificados
    Revoke-SmbShareAccess -Name ($departamento) -AccountName Todos -Force | Out-Null

    #1.5 - Crear las unidades organizativas de cada departamento
    try{
        New-ADOrganizationalUnit -Name ("UO"+$departamento) -ProtectedFromAccidentalDeletion $false
    }
    catch{
        Write-Output ("UO"+$departamento+" ya existe") 
    }

}