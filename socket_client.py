#!/usr/bin/env python3

import asyncio


async def socket_client(message):
    reader, writer = await asyncio.open_unix_connection(path='rpilcd.socket')
    
    print(f'Send: {message}')
    writer.write(message.encode())
    
    data = await reader.read(100)
    print(f'Received: {data.decode()}')
    
    print('Closing connection')
    writer.close()
    
asyncio.run(socket_client('Hello World!'))
