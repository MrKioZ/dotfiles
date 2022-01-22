#!/bin/bash

sudo pacman -Syyu
sudo pacman -Sy --noconfirm --needed git go

if ! yay
then
    echo "[x] Please make sure you have yay installed"
    echo "[*] Use the following commands:"
    echo "[*] git clone https://aur.archlinux.org/yay.git"
    echo "[*] cd yay"
    echo "[*] makepkg -si"
    exit
fi

pacman -Sy --noconfirm --needed rofi lightdm alacritty ranger
# vscodium-bin
