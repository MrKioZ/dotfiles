#!/bin/bash
if [ -z "$1" ]
then
    echo "=================================================="
    echo "specify a package to install duhh"
    echo "=================================================="
    exit 1
else
    if ! git clone "https://aur.archlinux.org/$1.git"
    then
        echo "=================================================="
        echo "FATAL: No such pacakge found on aur"
        echo "=================================================="
        exit 1
    else
        echo "=================================================="
        echo "Starting package build"
        echo "=================================================="
        cd $1
        if ! /bin/bash makepkg -si
        then
            echo "=================================================="
            echo "FATAL: Could not build the package, removing directory..."
            echo "=================================================="
            cd ..
            if ! rm -rf $1
            then
                echo "=================================================="
                echo "ERROR: Could not delete the source directory, you can delete it yourself tho"
                echo "=================================================="
                exit 1
            else
                echo "=================================================="
                echo "successfully removed dir $1"
                echo "=================================================="
                exit 0
            fi
            exit 1
        else
            echo "=================================================="
            echo "Sucessfully built package! Removing src directory"
            echo "=================================================="
            cd ..
            if ! rm -rf $1
            then
                echo "=================================================="
                echo "ERROR: Could not delete the source directory, you can delete it yourself tho"
                echo "=================================================="
                exit 1
            else
                echo "=================================================="
                echo "successfully installed $1!!"
                echo "=================================================="
                exit 0
            fi
        fi
    fi
fi
