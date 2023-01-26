#!/bin/bash

# Get the argument passed to the script or set default value for imagesize
if [ -z "$1" ]; then
    argument1=64
else
    argument1=$1
fi
# Get the argument passed to the script or set default value for iterations
if [ -z "$2" ]; then
    argument2=20
else
    argument2=$2
fi

# Pass the argument to the "imagesize" variable in the command
imagesize=$argument1 iterations=$argument2 python manage.py runserver 0.0.0.0:8000