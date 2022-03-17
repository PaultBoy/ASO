$servicios = Get-Service | Where-Object { $_.Status -eq "Running" }
$count = 0

foreach ($servicio in $servicios){
    #count = $count + 1
    $count++
}

write-host "Servicios en ejecución: "$count

$colorpicker = @('blue','white','yellow','black')

foreach ($color in $colorpicker){
    Write-Output $color
}