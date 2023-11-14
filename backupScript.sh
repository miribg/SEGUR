#!/bin/bash
# Definir el origen y el destino de la copia. Cambiar por tu nombre de usuario
origen=/home/mb/Descargas/SEGUR/bigarren/Segurtasuna
destino=/var/tmp/Backup

# Obtener la fecha actual en formato YYYY-MM-DD
fecha=$(date +%F)

# Crear el directorio destino con el nombre de la fecha
mkdir -p $destino/$fecha

# Usar rsync para sincronizar el origen con el destino, creando enlaces duros a los archivos que no han cambiado
rsync -a --link-dest=$destino/$(date -d yesterday +%F) $origen/ $destino/$fecha/
