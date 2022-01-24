# Dotfiles
---

## Installation

#### Installing yay
```bash
sudo pacman -Syyu
sudo pacman -Sy --noconfirm git
cd ~/Downloads
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
```

#### Installing Required Packages
```bash
yay -S rofi feh alacritty ranger polybar lightdm picom-jonaburg-git vscodium ttf-dejavu ttf-liberation noto-fonts
```

#### Downloading Dotfiles content
```bash
curl -sL https://raw.githubusercontent.com/MrKioZ/dotfiles/master/download.sh | bash
```
