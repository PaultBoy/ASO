#Añadir características de Windows desde PowerShell
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
#Ver todas las características de Windows
Get-WindowsCapability -Online
#Comando específico PowerShell para ver IP 
Get-NetIPAddress
Get-NetIPConfiguration
#InterfaceAlias selecciona interfaz, y AddressFamily selecciona IPv4
Get-NetIPAddress -InterfaceAlias Ethernet -AddressFamily IPv4
#Iniciar servicio sshd en PowerShell
Set-Service -Name sshd -Status Running
#Cambiar modo de inicio ssh
Set-Service -Name sshd -StartMode Automatic
#Crear archivos
New-Item "Fichero con espacios en medio.txt"