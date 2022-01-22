#!/bin/bash

sudo pacman -Syyu
sudo pacman -S --noconfirm git go
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
