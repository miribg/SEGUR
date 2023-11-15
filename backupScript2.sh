#!/bin/bash

# Definir las variables de origen, destino, fecha y referencia
SOURCE_DIR=/home/mb/Descargas/SEGUR/bigarren/Segurtasuna2/ # Para copiar solo lo de dentro de La carpeta de tu ordenador que quieres copiar
BACKUP_DIR=/var/tmp/Backups # La carpeta del servidor remoto donde quieres guardar la copia
DATETIME=$(date +%F) # La fecha del día en formato año-mes-día
BACKUP_PATH=$BACKUP_DIR/$DATETIME # La ruta completa de la copia con la fecha
LATEST_LINK=$BACKUP_DIR/$(date -d yesterday +%F) # La ruta de la carpeta de referencia, que es la copia del día anterior

# Crear el directorio de destino si no existe
ssh mb@35.246.21.16 mkdir -p $BACKUP_PATH
ssh mb@35.246.21.16 mkdir -p $LATEST_LINK


# Ejecutar el comando rsync con las opciones adecuadas
rsync -av -e ssh --link-dest=$LATEST_LINK $SOURCE_DIR mb@35.246.21.16:$BACKUP_PATH
