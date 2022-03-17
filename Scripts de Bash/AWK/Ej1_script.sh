#!/bin/bash
awk 'BEGIN {print "----REPORTE EVENTOS MENSUALES----"}
{
    if ($0 ~ /Jun.*shutdown[[:space:]]-h.*/){
        eventsJun=eventsJun+1
        eventsTot=eventsTot+1
    }
    else if ($0 ~ /Jun.*shutdown[[:space:]]-c.*/){
        eventsJun=eventsJun-1
        eventsTot=eventsTot-1
    }
    else if ($0 ~ /Jul.*shutdown[[:space:]]-h.*/){
        eventsJul=eventsJul+1
        eventsTot=eventsTot+1
    }
    else if ($0 ~ /Jul.*shutdown[[:space:]]-c.*/){
        eventsJul=eventsJul-1
        eventsTot=eventsTot-1
    }
    else if ($0 ~ /Aug.*shutdown[[:space:]]-h.*/){
        eventsAug=eventsAug+1
        eventsTot=eventsTot+1
    }
    else if ($0 ~ /Aug.*shutdown[[:space:]]-c.*/){
        eventsAug=eventsAug-1
        eventsTot=eventsTot-1
    }
    else if ($0 ~ /Sep.*shutdown[[:space:]]-h.*/){
        eventsSep=eventsSep+1
        eventsTot=eventsTot+1
    }
    else if ($0 ~ /Sep.*shutdown[[:space:]]-c.*/){
        eventsSep=eventsSep-1
        eventsTot=eventsTot-1
    }

}END {
    print "Apagados en junio: " eventsJun
    print "Apagados en julio: " eventsJul
    print "Apagados en agosto: " eventsAug
    print "Apagados en septiembre: " eventsSep
    print "Apagados totales: " eventsTot
}' auth.log
