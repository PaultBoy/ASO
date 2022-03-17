#!/bin/bash
awk 'BEGIN {print "----REPORTE EVENTOS MENSUALES----"}
{
    if ($0 ~ /Jun/){
        eventsJun=eventsJun+1
        eventsTot=eventsTot+1
    }
    else if ($0 ~ /Jul/){
        eventsJul=eventsJul+1
        eventsTot=eventsTot+1
    }
    else if ($0 ~ /Aug/){
        eventsAug=eventsAug+1
        eventsTot=eventsTot+1
    }
    else if ($0 ~ /Sep/){
        eventsSep=eventsSep+1
        eventsTot=eventsTot+1
    }
}END {
    print "Apagados en junio: " eventsJun
    print "Apagados en julio: " eventsJul
    print "Apagados en agosto: " eventsAug
    print "Apagados en septiembre: " eventsSep
    print "Apagados totales: " eventsTot
}' auth.log

