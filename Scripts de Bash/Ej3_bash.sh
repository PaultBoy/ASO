#!/bin/bash

read -p "Introduce la ruta de un fichero: " fich

if [[ ! -f $fich ]]; then
    echo "Fichero no encontrado"
    exit 1
else
    
fi
exit 0