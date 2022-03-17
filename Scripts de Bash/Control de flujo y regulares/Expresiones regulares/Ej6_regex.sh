#!/bin/bash
case $1 in
#Apartado A
'a')cat Municipios_Huesca.txt | cut -f 1,3 -d ";";;
#Apartado B
'b')cat Municipios_Huesca.txt | sort -t ";" -k 3 -n -r | tail -n 21 | cut -f 1 -d ";" | sed '21d';;
#Apartado C
'c')cat Municipios_Huesca.txt | awk -F ";" '{  
    if ($2 > 200){
        print $1,$3,$2
    }
}'
;;
#Apartado D
'd')cat Municipios_Huesca.txt | awk -F ";" '{  
    if ($2 > 200){
        print $1,$3,$2
    }
}' | sort -k 1
;;
#Apartado E
'e')cat Municipios_Huesca.txt | sort -t ";" -k 2 -n -r | awk -F ";" '{  
    if ($2 > 200){
        print $1,$3
    }
}'
;;
#Apartado F
'f')cat Municipios_Huesca.txt | sort -t ";" -k 3 -n -r | tail -n 20 |awk -F ";" '{
    print $2
    ext=ext + $2    
} END { print ext }'
;;
esac
