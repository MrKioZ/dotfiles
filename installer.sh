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

sudo pacman -Sy --noconfirm --needed rofi lightdm alacritty ranger
sudo yay -S awesome rofi picom i3lock-fancy xclip ttf-roboto polkit-gnome materia-theme lxappearance flameshot pnmixer network-manager-applet xfce4-power-manager qt5-styleplugins papirus-icon-theme -y
# vscodium-bin
