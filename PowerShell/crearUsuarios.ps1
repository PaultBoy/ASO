$userfile = Import-Csv -Path "C:\Users\Administrador\UsuariosWindowsServer.csv"
Get-LocalGroup -Name Administrativo 2> nul

if (!$?){
    New-LocalGroup -Name "Administrativo"
}
foreach ($item in $userfile){
    if ($item.Departamento -eq "Administrativo"){
        $SecString = ConvertTo-SecureString $item.Password -AsPlainText -Force
        Get-LocalUser -Name $item.NombreUsuario 2> nul
        if (!$?){
            New-LocalUser -Name $item.NombreUsuario -Password $SecString
            Add-LocalGroupMember -Group $item.Departamento -Member $item.NombreUsuario
        }
        
    }
}