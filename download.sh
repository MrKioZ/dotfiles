#!/usr/bin/env bash
set -eu

# Arch Linux Install Script (alis) installs unattended, automated
# and customized Arch Linux system.
# Copyright (C) 2022 picodotdev

GITHUB_USER="MrKioZ"
BRANCH="master"

while getopts "u:" arg; do
  case ${arg} in
    u)
      GITHUB_USER=${OPTARG}
      ;;
    ?)
      echo "Invalid option: -${OPTARG}."
      exit 1
      ;;
  esac
done

cd ~/Downloads

rm -f installer.sh
rm -f aur.sh

curl -O https://raw.githubusercontent.com/$GITHUB_USER/dotfiles/$BRANCH/installer.sh
curl -O https://raw.githubusercontent.com/$GITHUB_USER/dotfiles/$BRANCH/aur.sh

chmod +x installer.sh
chmod x+a aur.sh

./installer.sh
