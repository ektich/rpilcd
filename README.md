# Controlling Adafruit LCD on Raspberry PI

This is a personal project, and there is no guarantee this will ever work at all

## Pre-requisites
 2. export CFLAGS=-fcommon
 2. sudo pip3 install --upgrade RPi.GPIO
 3. sudo pip3 isntall --upgrade adafruit-blinka
 4. sudo pip3 install adafruit-circuitpython-charlcd

(potentially might also need sudo pip3 install --upgrade adafruit-python-shell)

## Emulation mode
This repository contains "stub" files for necessary Python libraries `board`, `busio` and `adafruit_character_lcd` that allows development to happen on a normal computer instead of RPi. The LCD is emulated, and messages are printed on the standard output. Make sure NOT to copy those three directories onto a RPi device
