#!/bin/bash

sudo pacman -Syyu
sudo pacman -Sy --noconfirm git
/bin/bash ./aur.sh yay
