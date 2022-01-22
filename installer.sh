#!/bin/bash

sudo pacman -Syyu
sudo pacman -Sy --noconfirm git go
/bin/bash ./aur.sh yay-bin
