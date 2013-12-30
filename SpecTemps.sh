#!/bin/bash

ls ../

echo " Please, enter Name of Spec: "
#if [ $1 =~ .[0-9] ];
#	then spectempl=$1
#fi

read spectempl
PWD=$(pwd)

if [ -f "../$spectempl" ];
	then echo " You are choose a $spectempl "
	else echo " $spectempl doesn't exist"
fi
#cp $SPECTMPPATH/spectempl $PWD
