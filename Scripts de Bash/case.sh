#!/bin/bash

#echo "¿Estás de acuerdo?: S o N"
read -p "¿Estás de acuerdo?: S o N: " -r inp

case "$inp" in
	"S")
		echo "Yes"
		;;
	"N")
		echo "No"
		;;
	*)
		echo "Opción no válida"
		;;
esac
