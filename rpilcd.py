#!/usr/bin/env python3

# rpilcd: LCD Display "driver" for Raspberry Pi
# This application should have two modes of operation
# 1. One-off execution: display a text on the LCD and exit
#    Optionally provide a timer for how long the message should be displayed
#    before screen is switched off
# 2. Daemon mode: listen on some sort of a socket (preferraby D-Bus)
#    for messages to display

import lcddisplay
import argparse
import asyncio


async def blank_screen(delay, screen):
    await asyncio.sleep(delay)
    screen.clear()
    screen.off()


async def main():
    screen = lcddisplay.LCD()

    parser = argparse.ArgumentParser(description="Display LCD message")
    parser.add_argument('-m', dest='msg',  help='Message to display')
    parser.add_argument('-d', dest='delay',
                        help='Time (in sec) before removing the message',
                        default=0, type=int)
    parser.add_argument('-b', dest='blank', action='store_true',
                        help='Blank the screen and exit')
    args = parser.parse_args()

    # blank screen and exit
    if args.blank:
        await blank_screen(0, screen)
        return
    # using asyncio: if msg was set, immediately display it
    if args.msg:
        screen.display_message(args.msg)

    # if delay is not 0 set up timer and execute the blanking of the sceen
    # and powering down of it after that time.
    # else just exit (leaving display "on" with the message)
    if args.delay:
        await blank_screen(args.delay, screen)


if __name__ == '__main__':
    asyncio.run(main())
