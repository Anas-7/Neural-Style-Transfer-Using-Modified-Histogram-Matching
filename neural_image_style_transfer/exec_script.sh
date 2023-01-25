#!/bin/bash

# Get the argument passed to the script or set default value
if [ -z "$1" ]; then
    argument=64
else
    argument=$1
fi

# Pass the argument to the "imagesize" variable in the command
imagesize=$argument python manage.py runserver 0.0.0.0:8000