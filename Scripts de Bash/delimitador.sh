#!/bin/bash

#script para modificar el IFS
#por defecto, IFS es un espacio

#IFS tendrá el valor de ","
IFS=","
read -p "Introduce tu nombre, apellidos: " nombre apellido1 apellido2
echo "El nombre es $nombre y el apellido primero es $apellido1"
