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

# global class representing the LCD screen
screen = lcddisplay.LCD()


async def receive_message(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    # close the connection to the client so it can exit
    writer.close()

    await display_message(message)


async def blank_screen(delay, screen):
    await asyncio.sleep(delay)
    screen.clear()
    screen.off()


async def display_message(message):
    screen.display_message(message)


async def main():

    parser = argparse.ArgumentParser(description="Display LCD message")
    parser.add_argument('-m', dest='msg',  help='Message to display')
    parser.add_argument('-d', dest='delay',
                        help='Time (in sec) before removing the message',
                        default=0, type=int)
    parser.add_argument('-b', dest='blank', action='store_true',
                        help='Blank the screen and exit')
    args = parser.parse_args()

    # set UNIX socket
    # TODO: path to socket should be either configurable
    #       or recevied from the systemd invocation
    server = await asyncio.start_unix_server(
        receive_message, path='rpilcd.socket')

    # blank screen and exit
    if args.blank:
        await blank_screen(0, screen)
        return
    # using asyncio: if msg was set, immediately display it
    if args.msg:
        await display_message(args.msg)

    # if delay is not 0 set up timer and execute the blanking of the sceen
    # and powering down of it after that time.
    # else just exit (leaving display "on" with the message)
    if args.delay:
        await blank_screen(args.delay, screen)
        return

    # start the socket server and wait forever
    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())
