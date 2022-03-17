$exe_32= Get-ChildItem -Recurse "C:\Program Files (x86)\" | Where-Object {$_.Extension -eq ".exe"} 
$exe_64= Get-ChildItem -Recurse "C:\Program Files\" | Where-Object {$_.Extension -eq ".exe"} 

$num_32=0
$num_64=0

foreach ($exe in $exe_32){
    $num_32++
}
foreach ($exe64 in $exe_64){
    $num_64++
}

Write-Host "Ejecutables de 32 bits: " $num_32
Write-Host "Ejecutables de 64 bits: " $num_64

if ($num_32 -lt $num_64){
    Write-Output "Hay un mayor número de binarios de 64 bits que de 32"
}
elseif ($num_32 -eq $num_64) {
    Write-Output "Hay el mismo número de binarios de 64 bits que de 32"
}
else{
    Write-Output "Hay un mayor número de binarios de 32 bits que de 64"
}