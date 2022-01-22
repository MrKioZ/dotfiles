#!/bin/bash

sudo pacman -Syyu
sudo pacman -Sy --noconfirm git
cd ~/Downloads
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
