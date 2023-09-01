#!/usr/bin/python
# -*- coding: utf8 -*-

import os
from time import sleep
import sys
import subprocess

def color(string, color=None):
    attr = []
    attr.append('1')
    
    if color:
        if color.lower() == "red":
            attr.append('31')
        elif color.lower() == "green":
            attr.append('32')
        elif color.lower() == "blue":
            attr.append('34')
        elif color.lower() == "yellow":
            attr.append('33')
        return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)

def is_cmd_installed(cmd):
    return any(
        os.access(os.path.join(path, cmd), os.X_OK)
        for path in os.environ["PATH"].split(os.pathsep)
    )

def commands_linux(command):
    saida = subprocess.check_output(command, shell=True)

    saida_str = saida.decode('utf-8')

    return saida_str

os.system("sudo apt-get install git gcc wget curl libcurl4-gnutls-dev rustc cargo")

def install_spotify():
    # Adicionar o repositório do Spotify
    os.system("curl -sS https://download.spotify.com/debian/pubkey_7A3A762FAFD4A51F.gpg | sudo gpg --dearmor --yes -o /etc/apt/trusted.gpg.d/spotify.gpg")
    os.system("echo 'deb http://repository.spotify.com stable non-free' | sudo tee /etc/apt/sources.list.d/spotify.list")
    
    # Atualizar a lista de pacotes
    os.system("sudo apt-get update -y")
    
    # Instalar o Spotify
    os.system("sudo apt-get install spotify-client -y")

    print(color("Spotify installed!","blue"))

if is_cmd_installed('spotify'):
    print(color("Spotify installed!.", "green"))
else:
    print(color("Installing spotify...", "blue"))
    install_spotify()

if is_cmd_installed('make'):
    print(color("Make installed!","green"))
else:
    print(color("Installing make..."))
    sleep(1)
    os.system("sudo apt-get install make")
    print(color("Make installed!","green"))

os.system("git clone https://github.com/abba23/spotify-adblock.git -b main spotifyad")
os.system("cd spotifyad && sudo make install")
os.system("curl https://cdn.discordapp.com/attachments/1040331064465440808/1147288479873630260/spotify-adblock.desktop > spotify-adblock.desktop")
os.system("rm -rf spotifyad/")
os.system("clear")
sleep(1)
print("")
print(color("Spotify-Adblock has been successfully installed!","green"))
print("")
print(color("Attention!", "red"))
print(color('Whenever you want to start spotify-adblock always start it through "spotify-adblock.desktop" which is located at: '+commands_linux("echo $(pwd)/spotify-adblock.desktop"), "yellow"))
print("")
