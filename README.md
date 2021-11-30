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

## `/dev/i2c` permissions
In order to work, the user executing the code should have full permissions on `/dev/i2c-` devices. By default only root has full access to them, and all other users are denied access.

To allow members of the group `alarm` write to the `i2c` devices create file `/etc/udev/rules.d/lcd.rules` with the following content:

```
SUBSYSTEM == "i2c-dev", TAG+="systemd", GROUP="alarm", MODE="0660"
```
