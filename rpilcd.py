#!/usr/bin/env python3

# rpilcd: LCD Display "driver" for Raspberry Pi
# This application should have two modes of operation
# 1. One-off execution: display a text on the LCD and exit
#    Optionally provide a timer for how long the message should be displayed
#    before screen is switched off
# 2. Daemon mode: listen on some sort of a socket (preferraby D-Bus)
#    for messages to display

import lcddisplay


def main():
    print("hello")
    screen = lcddisplay.LCD()
    screen.display_message("Hello")


if __name__ == '__main__':
    main()
