#!/bin/bash

sudo pacman -Syyu
sudo pacman -Sy --noconfirm git
./aur.sh yay
