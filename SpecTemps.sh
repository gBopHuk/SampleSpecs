#!/bin/bash

SPECSPATH=./Templates
if [ -d $SPECSPATH ];
	then ls $SPECSPATH | sed 's%\.spec%%'
	else echo " SPECSPATH doesn't xist "
	     exit 1
fi

echo " Please, enter the Name of Spec: "
#if [ $1 =~ .[0-9] ];
#	then spectempl=$1
#fi

read spectempl
PWD=$(pwd)

if [ -f "$SPECSPATH/$spectempl.spec" ];
	then echo " You are choose a $spectempl "
	else echo " $spectempl doesn't exist"
fi

cp $SPECSPATH/$spectempl.spec $PWD

exit 0
