#Get-Service | Where-Object { $_.Status -eq "Running" } | Export-Csv "servicios_running.csv"
#Conversión a CSV
#Get-Service | Select-Object Name, StartType, Status | Where-Object { $_.Status -eq "Running" } | Export-Csv "servicios_running.csv"
#Conversión a JSON
#Get-Service | Select-Object Name, StartType, Status | Where-Object { $_.Status -eq "Running" } | ConvertTo-Json | Out-File "servicios.json"
#Get-Service | Select-Object Name, StartType, Status | Where-Object { $_.Status -eq "Running" } | ConvertTo-Html | Out-File "servicios.html"
gci -recurse 'C:\Program Files' -Name '*.exe'
Get-ChildItem | Get-Member -MemberType Propery
gci -recurse 'C:\Program Files' | Where-object { $_.Extension -eq ".exe" }