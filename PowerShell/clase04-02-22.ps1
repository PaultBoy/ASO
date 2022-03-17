#Crear ámbito DHCP
Add-DhcpServerv4Scope -Name "asir" -StartRange 192.168.30.2 -EndRange 192.168.30.29 -SubnetMask 255.255.255.224 -LeaseDuration 1:30:00
#Determiniar puerta de enlace para las asignaciones de IP en un ámbito DHCP
Set-DhcpServerv4OptionValue -Router 192.168.30.1 -DnsServer 192.168.30.30,8.8.8.8
#Crear unidad organizativa en Active directory
New-ADOrganizationalUnit
# Consultar ayuda online de un comando
Get-Help New-ADOrganizationalUnit -Online
#Crear unidad organizativa de Active directory. DC contiene cada palabra separada por puntos
New-ADOrganizationalUnit -Name "DptoInformatica" -Path "DC=asir,DC=lan"
#Unidad organizativa dentro de unidad organizativa
New-ADOrganizationalUnit -Name "IT Portatiles" -Path "OU=DptoInformatica,DC=asir,DC=lan"
#Observar nuevas unidades organizativas
Get-ADOrganizationalUnit -Filter 'Name -like "IT*"'

#Como cualquier comando, se puede parsear. El path ha de ir de más específico a menos

#Mover objeto a otra unidad organizativa. CN=Contenedor
Move-ADObject -Identity "CN=asir01,CN=Users,DC=asir,DC=lan" -TargetPath "OU=IT Usuarios,OU=DptoInformatica,DC=asir,DC=lan"