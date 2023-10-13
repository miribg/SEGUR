#!/bin/bash

hash="e5ed313192776744b9b93b1320b5e268"

for f in ~/Descargas/irudia/*.jpg;do
	var=$(sudo md5sum "$f" | cut -d ' ' -f 1)
	if [ "$var" = "$hash" ];then
		echo "$f"
	fi
done
